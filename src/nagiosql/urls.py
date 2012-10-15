# Copyright 2012 NagiosQL-API authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^api/?', include('nagiosql.api.urls')),
)
