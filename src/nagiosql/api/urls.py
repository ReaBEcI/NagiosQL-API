# Copyright 2012 NagiosQL-API authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^host/(?P<hostname>[\w]+)\-(?P<ip>([0-9]{1,3}\.){3}[0-9]{1,3})/?$', 'nagiosql.api.views.status_or_delete'), #GET e DELETE
    (r'^host/(?P<hostname>[\w]+)/?$', 'nagiosql.api.views.status_or_delete'), #GET
    (r'^host/?$', 'nagiosql.api.views.host'), # POST
    
    (r'^service/(?P<service>([\w]+[\s+]?)+)/(?P<hostname>[\w]+)\-(?P<ip>([0-9]{1,3}\.){3}[0-9]{1,3})/?$', 'nagiosql.api.views.remove_host_service'), #DELETE
    (r'^service/(?P<service>([\w]+[\s+]?)+)/?$', 'nagiosql.api.views.remove_service'), #DELETE
    (r'^service/?$', 'nagiosql.api.views.alter_or_create_service'), # POST # PUT
    
    (r'^command/(?P<command>[\w]+)/?$', 'nagiosql.api.views.command'), #GET
    
    (r'^downtime/(?P<action>[\w]+)/?$', 'nagiosql.api.views.downtime'), #PUT
)

