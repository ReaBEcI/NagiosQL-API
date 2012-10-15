# Copyright 2012 NagiosQL-API authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding:utf-8 -*-

import os,re,sys
import logging
import calendar
from datetime import datetime

from nagiosql.api.script_utils import exec_script

logger = logging.getLogger(__name__)


def downtime_enable(host, author, comment):
    utcnow = calendar.timegm(datetime.utcnow().utctimetuple())
    code, stdout, stderr = exec_script('/usr/bin/printf "[%%lu] SCHEDULE_HOST_DOWNTIME;%s;%s;1893456000;1;0;0;%s;%s\n" > /var/nagios/rw/nagios.cmd' %(host, utcnow, author, comment))    
    return code
    

def downtime_disable(host):
    utcnow = calendar.timegm(datetime.utcnow().utctimetuple())
    downtime_id = get_downtime_id(host)
    if downtime_id == "id_not_found":
        return downtime_id
    else:
        code, stdout, stderr = exec_script('/usr/bin/printf "[%%lu] DEL_HOST_DOWNTIME;%s\n" %s > /var/nagios/rw/nagios.cmd' % (downtime_id,utcnow))
        return code


def get_downtime_id(host):
   # Variaveis de controle de fluxo
   find_host = False
   find_downfield = False

   # Tenta abrir o arquivo
   try:
      f = open('/var/nagios/status/status.dat')
   except:
      raise

   # Itera linha a linha.
   for line in f:

      # Se encontrar a parte de dowtime do arquivo fica esperto.
      # Vai procurar o Host agora.
      if re.search('hostdowntime', line):
         find_downfield = True

      # Se estamos no campo de downtime, procura o bloco do host.
      if find_downfield and re.search(host, line):
         find_host = True

      # Estamos no campo downtime e no host. Vamos pegar o id e para o For.
      if find_host and find_downfield:
         if (re.search('downtime_id', line)):
            id_dirty = re.compile('downtime_id=').sub('', line)
            id = re.sub(r'\s', '', id_dirty)
            f.close()
            break

   # Se o id nao foi encontrado a variavel nao esta setada.
   # Setamos para string de erro e retornamos.
   try:
      id
   except NameError:
      id = "id_not_found"

   return id


def reload_nagios():
    code, stdout, stderr = exec_script('/etc/init.d/nagios reload')
    if code != 0:
        logger.warning("%s" % stderr)
    else:
        logger.info("reload_nagios successfully")
    return code, stdout, stderr
    

   
