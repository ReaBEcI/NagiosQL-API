#encoding: utf-8
import re
import base64
import logging
from django.http import HttpResponse
from django.utils import simplejson
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from nagiosql.client import NagiosQLInvalidAuthentication


class StatusErrorMiddleware(object):
    
    def process_exception(self, request, exception):
        if isinstance(exception, ObjectDoesNotExist):
            return HttpResponse(", ".join(exception.args), status=404, mimetype="application/json")

        elif isinstance(exception, NagiosQLInvalidAuthentication):
            return HttpResponse('Not authorized', status=401, mimetype="application/json")

        return None


class NagiosQLAuthentication(object):
    """ Create django User object with username and password from HTTP basic authentication. """
    
    logger = logging.getLogger(__name__)
    NO_AUTH = HttpResponse(simplejson.dumps({'message': 'login and/or password is invalid'}), status=401, mimetype="application/json")
    
    def process_request(self, request):
        
        if request.GET.get('auth_request') == '1':
            self.logger.debug('Invite to request authentication')
            response = HttpResponse(status=401)
            response['WWW-Authenticate'] = 'Basic realm="NagiosQL User"'
            return response

        auth = request.META.get('HTTP_AUTHORIZATION')
        username = None
        password = None
        if auth:
            self.logger.debug(u'Header => Authorization: %s' % auth)
            m = re.match('Basic (.*)', auth)
            if m and m.group(1):
                username, password = base64.b64decode(m.group(1)).split(':')

        if username and password:
            self.logger.debug('Username=%s password=*** (len=%d)' % (username, len(password)))
            # create a new user objects and put it in request to emulate real authentication
            request.user = User(username=username, password=password)
        else:
            self.logger.debug('Invalid authorization header')
            return self.NO_AUTH

