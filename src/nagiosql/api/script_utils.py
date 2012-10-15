# Copyright 2012 NagiosQL-API authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding:utf-8 -*-
'''
Title: Infrastructure NetworkAPI
Author: globo.com / TQI
Copyright: ( c )  2009 globo.com todos os direitos reservados.
'''

import os

from subprocess import Popen, PIPE, STDOUT


class ScriptError(Exception):
    """Representa um erro ocorrido durante a chamada do script."""
    def __init__(self, cause, message):
        self.cause = cause
        self.message = message
        
    def __str__(self):
        msg = u'Erro ao executar o SCRIPT: Causa: %s, Mensagem: %s' % (self.cause, self.message)
        return msg.encode('utf-8', 'replace')

def exec_script(command):
    
    try:
                
        p = Popen(command, shell=True, executable="/bin/bash", stdout=PIPE, stderr=PIPE)
        child_stdout, child_stderr = p.communicate()
        
        child_stdout = unicode(child_stdout, 'utf-8', 'replace')
        child_stderr = unicode(child_stderr, 'utf-8', 'replace')

        return p.returncode, child_stdout, child_stderr
    except OSError, o:
        return o.args[0], '', o.args[1]
    except ValueError, v:
        raise ScriptError(v, u'Falha ao executar o comando %s.' % command)