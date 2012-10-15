# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.utils import simplejson
from time import sleep
import re
import os

from django.views.decorators.http import require_http_methods

from nagiosql.api.models import TblHost as Host
from nagiosql.api.models import TblHosttemplate as HostTemplate
from nagiosql.api.models import TblLnkservicetohost as ServicelnkHost
from nagiosql.api.models import TblCommand as Command
from nagiosql.api.models import TblService as Service
from nagiosql.api.models import TblLnkservicetoservicetemplate as Servicetoservicetemplate

from nagiosql.api.script_utils import exec_script
from nagiosql.client.service import ServiceNagiosQLAPI
from nagiosql.client.host import HostNagiosQLAPI
from nagiosql.client.nagios import *

from django.conf import settings

import logging
logger = logging.getLogger(__name__)


def get_template_id(templateName):
    logger.debug("Consulting if template %s exists" % templateName)
    templateObj = HostTemplate.objects.get(template_name=templateName)
    return templateObj.id


def get_host(hostname, ip):
    logger.debug("Consulting if hostname %s-%s exists" % (hostname, ip))
    hostname = hostname + "-" + ip
    host = Host.objects.get(host_name=hostname, address=ip)
    return host

def build_response_with_message(msg, status=400, extra={}):
    data = {'message': msg}
    data.update(extra)
    response = HttpResponse(simplejson.dumps(data), status=status, mimetype="application/json")
    return response
    
def service_client(request):
    client = ServiceNagiosQLAPI(settings.NAGIOSQL, request.user.username, request.user.password)
    return client

def host_client(request):
    client = HostNagiosQLAPI(settings.NAGIOSQL, request.user.username, request.user.password)
    return client


def check_data(hostname,ip):
    invalid = False
    # checa se o IP é um IP valido
    if not re.match(r"([0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
       logger.debug("invalid IP")
       invalid = True
    # # checa se o host é valido
    if re.search(r"[\W]", hostname):
        logger.debug("invalid hostname")
        invalid = True
    return invalid

@require_http_methods(["GET","DELETE"])
def status_or_delete(request, hostname, ip=None):
    
    if request.method == "GET":
        return status(request, hostname, ip)
    elif request.method == "DELETE":
        if not ip:
            return build_response_with_message('Ip required')
        return delete(request, hostname, ip)


@require_http_methods(["DELETE"])
def delete(request, hostname, ip):
    host = get_host(hostname, ip)
    service = ServicelnkHost.objects.filter(idslave=host.id)
    if service:
        logger.warning("hostname %s-%s associated to service yet" % (hostname,ip))
        return build_response_with_message('hostname %s-%s associated to service' % (hostname,ip))

    logger.debug("Deleting hostname %s-%s" % (hostname, ip) )
    client = host_client(request)
    client.delete_host(host.id)
    sleep(1)
    # grava o hostgroup para nao gerar inconsistencia
    logger.debug("writing hostgroup")
    client.write_hostgroups()
    logger.info("hostname %s-%s successfully deleted by %s" % (hostname,ip,request.user.username))
    return build_response_with_message('hostname %s-%s successfully deleted' % (hostname,ip), 200)


@require_http_methods(["GET"])
def status(request, hostname, ip=None):
    if ip:
        host = get_host(hostname, ip)
        logger.info("hostname found %s-%s" % (hostname,ip))
        return build_response_with_message('hostname %s-%s found' % (hostname,ip), 200, {'active': host.act})
    hosts = Host.objects.filter(host_name__icontains=hostname)
    h = []
    for host in hosts:
        h.append({'message': 'hostname %s found' % host.host_name, 'active': host.act})
    return HttpResponse(simplejson.dumps(h), status=200, mimetype="application/json")    


@require_http_methods(["POST"])
def host(request):
    json_data = simplejson.loads(request.raw_post_data)
    
    for check in json_data['hostname']:
        # verifica se o host e ip estao corretos
        if check_data(check["name"], check["ip"]):
            return build_response_with_message('invalid parameters')
    
    for host in json_data['hostname']:
        try:            
            if Host.objects.get(host_name="%s-%s"% (host["name"], host["ip"])):
                logger.warning("hostname %s-%s already exist" % (host["name"], host["ip"]))
        except Host.DoesNotExist:
            # pega o templateId
            templateId = get_template_id(host['template'])
            # chama o metodo para criar o host
            logger.debug("Creating the hostname %s-%s" % (host["name"], host["ip"]))
            client = host_client(request)
            client.create_host("%s-%s" % (host["name"],host["ip"]), host["ip"], str(templateId) + "::1")
            # pegando o id do host criado
            hostId = Host.objects.get(host_name="%s-%s" % (host["name"], host["ip"])).id
            # ecrevendo o arquivo em disco
            logger.debug("Writing the hostname %s-%s hostID: %s" % (host["name"], host["ip"], hostId))
            sleep(1)
            client.write_host(hostId)
            logger.info("hostname %s-%s successfully created by %s" % (host["name"],host["ip"],request.user.username))            
    return build_response_with_message('host(s) successfully created', 200)


#
# metodos para servico
#

@require_http_methods(["POST","PUT"])
def alter_or_create_service(request):
    if request.method == "POST":
        return service(request)
    if request.method == "PUT":
        return alter_host_service(request)


def get_command_id(commandName):
    logger.debug("consulting if command %s exists" % commandName)
    command = Command.objects.get(command_name=commandName)
    return command.id


@require_http_methods(["POST"])
def service(request):
    hosts = []
    try:
        json_data = simplejson.loads(request.raw_post_data)
        
        for check in json_data['hostname']:
            # verifica se o host e ip estao corretos
            if check_data(check["name"], check["ip"]):
                return build_response_with_message('invalid parameters')
        
        for host in json_data['hostname']:
            # verifica se o host existe
            h = get_host(host['name'],host['ip'])
            # apenda os hosts
            hosts.append(h.id)
        # verifica se ja existe o servico
        if Service.objects.get(service_description=json_data["service"]["name"]):
            logger.warning("service exists")
            return build_response_with_message('service already exists')
    except Service.DoesNotExist:
        # ve se o command informado existe
        commandId = get_command_id(json_data["service"]["command"])
        # cria o servico
        logger.debug("Creating service %s" % json_data["service"]["name"])
        client = service_client(request)
        client.create_service(hosts, json_data["service"]["name"], commandId, json_data["service"]["args"])
        sleep(1)
        # pegando o id do host criado
        serviceId = Service.objects.get(service_description=json_data["service"]["name"]).id
        # escreve o servico em disco
        logger.debug("Writing service")
        client.write_service(serviceId)
        logger.info("service %s successfully created by %s" % (json_data["service"]["name"],request.user.username))
        sleep(1)
        # faz reload no nagios
        reload_nagios()
    return build_response_with_message('service successfully created', 200)


@require_http_methods(["PUT"])
def alter_host_service(request):
    hosts = []
    hprint = []
    json_data = simplejson.loads(request.raw_post_data)

    for check in json_data['hostname']:
        # verifica se o host e ip estao corretos
        if check_data(check["name"], check["ip"]):
            return build_response_with_message('invalid parameters')
    
    for host in json_data['hostname']:
        # verifica se o host existe
        h = get_host(host['name'],host['ip'])
        # apenda os hosts
        hosts.append(h.id)
        hprint.append(host['name'] + "-" + host['ip'])

    # verifica se ja existe o servico
    srv = Service.objects.get(service_description=json_data["service"]["name"])
    # recupera os hosts ja associados ao servico
    SrvlnkHost = ServicelnkHost.objects.filter(idmaster=srv.id)
    for s in SrvlnkHost:
        hosts.append(s.idslave)
    # separa o commandId dos argumentos
    command = srv.check_command.split("!")
    # recuperando o templateService
    template = Servicetoservicetemplate.objects.filter(idmaster=srv.id)
    if template:
        templateId = str(template[0].idslave) + "::1"
    else:
        templateId = "4::1" # se nao tiver o template coloca o padrao de 1 min.

    # incluindo hosts ao servico
    logger.debug("Including the host(s) to the service %s" % srv.service_description)
    client = service_client(request)
    client.alter_service(srv.config_name, hosts, srv.service_description, command[0], command[1], srv.id, templateId)
    sleep(1)
    # escreve o arquivo em disco
    logger.debug("Writing the service")
    client.write_service(srv.id)
    logger.info("host(s) %s associated successfully by %s" % (hprint,request.user.username))
    sleep(1)
    # faz reload no nagios
    reload_nagios()
    return build_response_with_message('host(s) associated successfully', 200)


@require_http_methods(["DELETE"])
def remove_service(request, service):
    srv = Service.objects.get(service_description=service)
    logger.debug("deleting service %s" % service)
    client = service_client(request)
    client.delete_service(srv.id)
    sleep(1)
    # grava o servicegroup para nao gerar inconsistencia
    logger.debug("writing servicegroups")
    client.write_servicegroups()
    logger.info("service %s deleted successfully by %s" % (service,request.user.username))
    sleep(1)
    # faz reload no nagios
    reload_nagios()
    return build_response_with_message('service deleted successfully', 200)


@require_http_methods(["DELETE"])
def remove_host_service(request, service, hostname, ip):
    hosts = []
    check = False
    srv = Service.objects.get(service_description=service)
    host = get_host(hostname,ip)
    # recupera os hosts
    SrvlnkHost = ServicelnkHost.objects.filter(idmaster=srv.id)
    for s in SrvlnkHost:
        hosts.append(s.idslave)
        if s.idslave == host.id:
            check = True
    if check:
        logger.debug("removing hostname %s-%s from service %s" % (hostname,ip,service))
    else:
        return HttpResponse(simplejson.dumps({'message': 'hostname %s-%s not associated to the service: %s' % (hostname,ip,service)}), status=404, mimetype="application/json")          
    hosts.remove(host.id)
    template = Servicetoservicetemplate.objects.filter(idmaster=srv.id)
    if template:
        templateId = str(template[0].idslave) + "::1"
    else:
        templateId = "4::1" # se nao tiver o template coloca o padrao de 1 min.            
    command = srv.check_command.split("!")
    client = service_client(request)
    client.alter_service(srv.config_name, hosts, srv.service_description, command[0], command[1], srv.id, templateId)
    sleep(1)
    # escreve o arquivo em disco
    logger.debug("writing service to disk")
    client.write_service(srv.id)
    logger.info("hostname %s-%s dissociated successfully by %s" % (hostname,ip,request.user.username))
    sleep(1)
    # faz reload no nagios
    reload_nagios()
    return build_response_with_message('hostname dissociated successfully', 200)


#
# commands
#

def command(request,command):
    commands = os.listdir("/opt/nagios/lib/plugins/")
    if command in commands:
        code, stdout, stderr = exec_script("/opt/nagios/lib/plugins/%s" % command)
        return HttpResponse(stdout, content_type="text/plain")
    else:
        logger.debug("Command Unauthorized")
        return build_response_with_message('Command Unauthorized', 401)


#
# Downtime
#

@require_http_methods(["PUT"])
def downtime(request,action):
    json_data = simplejson.loads(request.raw_post_data)
    
    for check in json_data['hostname']:
        # verifica se o host e ip estao corretos
        if check_data(check["name"], check["ip"]):
            return build_response_with_message('invalid parameters')

    try:    
        for host in json_data['hostname']:
            # verifica se o host existe
            h = get_host(host['name'],host['ip'])
            if action == "enable":
                if get_downtime_id(h.host_name) == "id_not_found":
                    enable = downtime_enable(h.host_name,request.user.username,json_data['comment'])
                    logger.debug("enable downtime host: %s" % h.host_name)
                else:
                    logger.warning("host is already with downtime")
            if action == "disable":
                disable = downtime_disable(h.host_name)
                logger.debug("disable downtime host: %s" % h.host_name)
                if disable == "id_not_found":
                    logger.warning("downtime not scheduled for this host")
        logger.info("scheduled downtime %s successfully fot host: %s by %s" % (action,h.host_name,request.user.username))
        return build_response_with_message('scheduled downtime %s successfully' %action, 200)
    except KeyError:
        return build_response_with_message('invalid parameters')


