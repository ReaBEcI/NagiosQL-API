# Copyright 2012 NagiosQL-API authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

#encoding: utf-8
import requests
import logging

logger = logging.getLogger(__name__)

class NagiosQLAPI(object):
    
    def __init__(self, hostname, username, password):
        self._session = None
        self.username = username
        self.password = password
        self.hostname = hostname
        
    def do_login(self):
        logger.debug(u"Authenticating on Nagiosql at %s with login %s" % (self.hostname, self.username))
        r = requests.post(self.url('/nagiosql320/index.php'), {"tfUsername": self.username, "tfPassword": self.password} )
        logger.debug("Authentcation status code: %s" % r.status_code)
        if r.text.find("Login failed") != -1:
            ##### FIXME Assert to success. Anything else is fail!
            logger.warning("Authentication failed!!!")
            self._session = None
            raise NagiosQLInvalidAuthentication()

        logger.debug('Authentication successful')
        self._session = r.cookies.get('PHPSESSID', None)
        return self._session
        
    def session(self):
        """ Returns NagiosQL authorized cookie session. Raise NagiosQLInvalidAuthentication if authentication fail. """
        if not self._session:
            self.do_login()
        return self._session
        
    def cookies(self):
        return { 'PHPSESSID' : self.session() }
                    
    def url(self, path):
        """ Complements NagiosQL path with protocol and hostname """
        return "http://%s%s" % (self.hostname, path)
        
    def GET(self, path):
        """ Make a GET request in Nagios with a authenticated session """
        complete_url = self.url(path)
        r = requests.get(complete_url, cookies=self.cookies())
        logger.debug(u'GET %s: status code=%d' % (complete_url, r.status_code))
        r.raise_for_status()
        return r
        
    def POST(self, path, data):
        complete_url = self.url(path)
        r = requests.post(complete_url, data, cookies=self.cookies())
        logger.debug(u'POST %s: status code=%d' % (complete_url, r.status_code))
        r.raise_for_status()
        return r


class NagiosQLInvalidAuthentication(Exception):
    pass

