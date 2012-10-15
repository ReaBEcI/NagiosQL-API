# Copyright 2012 NagiosQL-API authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

#encoding: utf-8
from django.test import TransactionTestCase
from django.utils import simplejson
from nagiosql.api.models import TblService, TblHost
import nagiosql.api.views
import nagiosql.api.tests
import datetime
import base64

class ServiceTest(TransactionTestCase):
    fixtures = ['api/fixtures/tests_service.yaml', 'api/fixtures/tests_service_delete.yaml', 'api/fixtures/test_lnkservice_to_host.yaml']
    
    def setUp(self):
        self.service_original = nagiosql.api.views.ServiceNagiosQLAPI
        nagiosql.api.views.ServiceNagiosQLAPI = MockServiceNagiosQLAPI
        
        credentials = base64.b64encode('username:password')
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Basic ' + credentials
        
    def tearDown(self):
        nagiosql.api.views.ServiceNagiosQLAPI = self.service_original
        
    def postJSON(self, url, data):
        return self.client.post(url, data=simplejson.dumps(data), content_type='application/json')
        
    def putJSON(self, url, data):
        return self.client.put(url, data=simplejson.dumps(data), content_type='application/json')
    
    def deleteJSON(self, url):
        return self.client.delete(url, content_type='application/json')
        
    def assertResponseMessage(self, msg, response):
        data = simplejson.loads(response.content)
        self.assertEquals(data['message'], msg)

    def test_create_service_return_successfully_create_message(self):
        service_data = {"hostname": [ {"name":"test141", "ip": "10.1.30.8"} ] , "service": {"name": "http porta 8080", "command": "check_http", "args": "-p 8080 -u /healthcheck.html -s WORKING" } }
        print "#"*50, TblHost.objects.all()
        response = self.postJSON('/api/service/', service_data)
        self.assertEqual(response.status_code, 200)
        self.assertResponseMessage(u'service successfully created', response)

    def test_create_service_with_host_not_exists_returns_error(self):
        HOSTNAME="NOHOST"
        HOSTIP="1.1.1.2"
        service_data = {"hostname": [ {"name":HOSTNAME, "ip": HOSTIP} ] , "service": {"name": "http porta 8080", "command": "check_http", "args": "-p 8080 -u /healthcheck.html -s WORKING" } }
        response = self.postJSON('/api/service/', service_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content, "TblHost matching query does not exist.")

    def test_create_service_with_invalid_host_returns_error(self):
        HOSTNAME="teste%$"
        HOSTIP="1.1.1.2"
        service_data = {"hostname": [ {"name":HOSTNAME, "ip": HOSTIP} ] , "service": {"name": "http porta 8080", "command": "check_http", "args": "-p 8080 -u /healthcheck.html -s WORKING" } }
        response = self.postJSON('/api/service/', service_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, '{"message": "invalid parameters"}')

    def test_create_service_with_invalid_ip_returns_error(self):
        HOSTNAME="teste"
        HOSTIP="1.1.1.2000"
        service_data = {"hostname": [ {"name":HOSTNAME, "ip": HOSTIP} ] , "service": {"name": "http porta 8080", "command": "check_http", "args": "-p 8080 -u /healthcheck.html -s WORKING" } }
        response = self.postJSON('/api/service/', service_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, '{"message": "invalid parameters"}')
                    
    def test_delete_with_valid_service_return_success(self):
        VALID_SERVICE = "deleteservice"
        response = self.deleteJSON('/api/service/%s' % VALID_SERVICE)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '{"message": "service deleted successfully"}')
        
    def test_delete_invalid_service_return_error(self):
        INVALID_SERVICE = "INVALID"
        response = self.deleteJSON('/api/service/%s' % INVALID_SERVICE)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content, 'TblService matching query does not exist.')

    def test_remove_invalid_host_from_service_return_error(self):
        response = self.deleteJSON('/api/service/deleteservice/test242-10.1.30.8')
        self.assertEqual(response.content, 'TblHost matching query does not exist.')
        self.assertEqual(response.status_code, 404)
        
    def test_remove_not_associated_host_from_service_return_error(self):
        response = self.deleteJSON('/api/service/deleteservice/test142-10.1.30.8')
        self.assertEqual(response.content, '{"message": "hostname test142-10.1.30.8 not associated to the service: deleteservice"}')
        self.assertEqual(response.status_code, 404)
        
    def test_remove_valid_host_from_service_return_success(self):
        service_data = {"hostname": [ {"name":"test141", "ip": "10.1.30.8"} ] , "service": {"name": "deleteservice"}}
        response = self.deleteJSON('/api/service/deleteservice/test141-10.1.30.8')
        self.assertEqual(response.content, '{"message": "hostname dissociated successfully"}')
        self.assertEqual(response.status_code, 200)
        
    def test_associate_host_valid_service_return_success(self):
        service_data = {"hostname": [ {"name":"test141", "ip": "10.1.30.8"} ] , "service": {"name": "deleteservice"}}
        response = self.putJSON('/api/service/', service_data)
        self.assertEqual(response.status_code, 200)

    def test_associate_host_not_exists_to_service_return_error(self):
        service_data = {"hostname": [ {"name":"test242", "ip": "10.1.30.8"} ] , "service": {"name": "deleteservice"}}
        response = self.putJSON('/api/service/', service_data)
        self.assertEqual(response.content, 'TblHost matching query does not exist.')
        self.assertEqual(response.status_code, 404)

    def test_associate_invalid_host_to_service_return_error(self):
        service_data = {"hostname": [ {"name":"teste%$", "ip": "10.1.30.8"} ] , "service": {"name": "deleteservice"}}
        response = self.putJSON('/api/service/', service_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, '{"message": "invalid parameters"}')

    def test_associate_invalid_ip_to_service_return_error(self):
        service_data = {"hostname": [ {"name":"teste", "ip": "10.1000.30.80"} ] , "service": {"name": "deleteservice"}}
        response = self.putJSON('/api/service/', service_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, '{"message": "invalid parameters"}')

    def test_associate_valid_host_to_invalid_service_return_error(self):
        service_data = {"hostname": [ {"name":"test141", "ip": "10.1.30.8"} ] , "service": {"name": "invalid"}}
        response = self.putJSON('/api/service/', service_data)
        self.assertEqual(response.content, 'TblService matching query does not exist.')
        self.assertEqual(response.status_code, 404)


class MockServiceNagiosQLAPI(object):

    def __init__(self, hostname, username, password):
        self.create_service_count = 0
        self.write_service_count = 0
        self.alter_service_count = 0
        self.delete_service_count = 0
        self.write_servicegroups_count = 0

    def create_service(self, hostId, name, commandId, args, templateId="4::1"):
        print "*"*30, locals()

        service = TblService.objects.create(service_description=name, host_name=hostId[0], register=u'1', active_checks_enabled=2L, \
            icon_image_alt=u'', access_group=0L, flap_detection_options=u'', obsess_over_service=2L, action_url=u'', config_id=1L, is_volatile=2L, import_hash=u'', low_flap_threshold=None, process_perf_data=2L, check_period=0L, display_name=u'', notification_interval=None, hostgroup_name_tploptions=2L, notification_period=0L, retry_interval=None, retain_status_information=2L, icon_image=u'', stalking_options=u'', event_handler_enabled=2L, contact_groups_tploptions=2L, initial_state=u'', first_notification_delay=None, flap_detection_enabled=2L, notification_options=u'', use_variables=0L, parallelize_check=2L, retain_nonstatus_information=2L, notifications_enabled=2L, event_handler=0L, contacts=0L, contact_groups=0L, freshness_threshold=None, last_modified=datetime.datetime(2012, 7, 3, 14, 27, 35), use_template=1L, active=u'1', config_name=u'admin-novo_gera_cache', name=u'', host_name_tploptions=2L, notes=u'', check_command=u'6!DataCenter!0:40!0:40', use_template_tploptions=2L, contacts_tploptions=2L, hostgroup_name=0L, servicegroups=0L, passive_checks_enabled=2L, check_interval=None, high_flap_threshold=None, notes_url=u'', max_check_attempts=None, servicegroups_tploptions=2L, check_freshness=2L)
        self.create_service_count += 1
        return service.id

    def write_service(self, serviceId):
        self.write_service_count += 1

    def alter_service(self, configName, hostId, description, commandId, args, servicoId, templateId):
        self.alter_service_count += 1

    def delete_service(self, servicoId):
        self.delete_service_count += 1

    def write_servicegroups(self):
        self.write_servicegroups_count += 1

