Nagiosql Restful API
====================

The api was developed in order to interface NagiosQL model (version 3.2.0) for manage nagios files.

Instalation
===========
	
	pip install -r src/nagiosql/requirements.txt

Running
=======

	./manage.py runserver

Documentation
=============

Method Host
===========

/host/< hostname >-< ip >
========================

Description: Check if one or more hosts exist on NagiosQL database.

Method: GET

URL: http://localhost/api/host/< hostmame >
	
Parameters:

*   hostname: hostname 
*   IP: Service IP

`Example`:
	
	# search for 1 specific host
	$ curl -u [USER:PASSWORD] -s http://localhost/api/host/host123
	     {"active": true, "message": "hostname host123 found"}

	# search for multiple hosts
	$ curl -u [USER:PASSWORD] -s http://localhost/api/host/host
	     [{"active": true, "message": "hostname host123 found"},
	     {"active": true, "message": "hostname host1234 found"},
	     {"active": true, "message": "hostname hostname found"},
	     {"active": true, "message": "hostname host_123 found"}]



/host
=====

Description: Creating one or more host entries. Use the list format to define the host(s) and its parameter(s)

Method: POST

URL: http://localhost/api/host

Parameters:

*    name: hostname
*    ip: Service IP ( bind )
*    template: Server Template.

`Example`:

	# Add a host
	$ curl -u [USER:PASSWORD] -s -H 'Content-type: application/json' http://localhost/api/host -X POST -d '{"hostname":[{"name":"teste", "ip": "110.120.10.10", "template": "linux-server"}]}'
	{"message": "host(s) successfully created"}

	# Add a list of hosts
	$ curl -u [USER:PASSWORD] -s -H 'Content-type: application/json' http://localhost/api/host -X POST -d '{"hostname":[{"name":"teste", "ip": "120.110.10.10", "template": "linux-server"},{"name":"teste", "ip": "230.220.210.20", "template": "sun-server"}]}'
	{"message": "host(s) successfully created"}'
	


/host/< hostname >-< ip >
=====================

Description: Deletes the  hostname, when it’s not associated with a service.

Method: DELETE

URL: http://localhost/api/host/hostname

Parameters:

*    hostname: hostname
*    IP: Service IP

`Example`:
	
	$ curl -u [USER:PASSWORD]  -s http://localhost/api/host/hostname-220.210.120.210 -X DELETE
	{"message": "hostname hostname-220.210.120.210 successfully deleted"}
	


Service
=======

/service
========

Description: Creates a service and associates to one or more hosts (parameters passed in a list format on post).

Method: POST

URL: http://localhost/api/service

Parameters:

hostname

*   name: hostname
*   ip: Service IP

service

*   name: service name
*   command: type of check to be performed
*   args: Check the options chosen

`Example`:

	# Creating the "http check port 8080" service and associating to a host
	$ curl -u [USER:PASSWORD] -s -H 'Content-type: application/json' http://localhost/api/service -X POST -d '{"hostname":[{"name":"hostname", "ip": "110.120.10.10"}], "service": {"name": "http check port 8080", "command": "check_http", "args": "-p 8080 -u /healthcheck.html -s WORKING"}}

	# Creating "ana maria braga port 8080" service and associating to a list of hosts
	$ curl -u [USER:PASSWORD] -s -H 'Content-type: application/json' http://localhost/api/service -X POST -d '{"hostname":[{"name":"hostname", "ip": "110.120.10.10"},{"name":"hostname", "ip": "210.220.230.20"}], "service": {"name": "http check port 8080", "command": "check_http", "args": "-p 8080 -u /healthcheck.html -s WORKING"}}'
	{"message": "service successfully created"}
	


/service
========

Description: associating one or more hosts to an existing service

Method: PUT

URL: http://localhost/api/service

Parameters:

hostname

*  name: hostname
*  ip: Serice IP

service

*  name: service name

`Example`:

	# associating a host to "http check port 8080" service
	$ curl -u [USER:PASSWORD] -s -H 'Content-type: application/json' http://localhost/api/service -X PUT -d '{"hostname":[{"name":"hostname", "ip": "220.201.202.20"}], "service": {"name": "http check port 8080"}}'
	{"message": "host(s) associated successfully"}

	# associating a lot of hosts to the "http check port 8080" service
	$ curl -u [USER:PASSWORD] -s -H 'Content-type: application/json' http://localhost/api/service -X PUT -d '{"hostname":[{"name":"hostname", "ip": "120.110.10.10"},{"name":"hostname", "ip": "220.210.210.20"}], "service": {"name": "http check port 8080"}}'
	{"message": "host(s) associated successfully"}
	
	
/service/< service >
====================

Description: Delete an entire service

Method: DELETE

URL: http://localhost/api/service/http check port 8080

Parameters:

*  service: name/service description

`Example`:

	$ curl -u [USER:PASSWORD] -s -H 'Content-type: application/json' http://localhost/api/service/http%20check%20port%208080 -X DELETE
	{"message": "service deleted successfully"}
	

/service/< service >/< hostname >-< ip >
========================================

Description: disassociating a hostname of “Admin Novo Gera Cache” service

Method: DELETE

URL: http://localhost/api/service/http check port 8080/hostname-120.110.110.10

Parameters:

*    service: name/service description
*    hostname: hostname
*    ip: Service IP

`Example`:

	$ curl -u [USER:PASSWORD] -s -H 'Content-type: application/json' http://localhost/api/service/http%20check%20port%208080/hostname-220.210.210.20 -X DELETE
	{"message": "hostname dissociated successfully"}
	

Command
=======

/command/< command >
====================

Description: help command plugins nagios

Method: GET

URL: http://localhost/api/command/check_http

Parameters:

*   command: plugin nagios

`Example`:

	$ curl -u [USER:PASSWORD] http://localhost/api/command/check_http
	Usage:
	 check_http -H <vhost> | -I <IP-address> [-u <uri>] [-p <port>]
	       [-w <warn time>] [-c <critical time>] [-t <timeout>] [-L] [-a auth]
	       [-b proxy_auth] [-f <ok|warning|critcal|follow|sticky|stickyport>]
	       [-e <expect>] [-s string] [-l] [-r <regex> | -R <case-insensitive regex>]
	       [-P string] [-m <min_pg_size>:<max_pg_size>] [-4|-6] [-N] [-M <age>]
	       [-A string] [-k string] [-S] [--sni] [-C <age>] [-T <content-type>]
	       [-j method]
	

Downtime
========

/downtime/enable
================

Description: enable host downtime

Method: PUT

URL: http://localhost/api/downtime/enable

Parameters:

*   name: hostname
*   ip: Serice IP
*   comment: downtime comments

`Example`:

	# 1 specific host
	$ curl -u [USER:PASSWORD] http://localhost/api/downtime/enable -X PUT -d '{"hostname":[{"name":"hostname", "ip": "120.210.20.112"}], "comment":  "comment for disable"}'
	{"message": "scheduled downtime enable successfully"}

	# add a list of hosts
	$ curl -u [USER:PASSWORD] http://localhost/api/downtime/enable -X PUT -d '{"hostname":[{"name":"hostname", "ip": "120.210.20.112"}, {"name":"hostname", "ip": "110.248.41.6"}], "comment":  "comment for disable"}'
	{"message": "scheduled downtime enable successfully"}
	
	
/downtime/disable
=================

Description: disable host downtime

Method: PUT

URL: http://localhost/api/downtime/disable

Parameters:

*   name: hostname
*   ip: Serice IP

`Example`:

	# for 1 specific host
	$ curl -u [USER:PASSWORD] http://localhost/api/downtime/disable -X PUT -d '{"hostname":[{"name":"hostname", "ip": "110.220.20.112"}]}'
	{"message": "scheduled downtime disable successfully"}

	# add list of hosts
	$ curl -u [USER:PASSWORD] http://localhost/api/downtime/disable -X PUT -d '{"hostname":[{"name":"hostname", "ip": "120.210.210.112"}, {"name":"hostname", "ip": "110.248.41.6"}]}'
	{"message": "scheduled downtime disable successfully"}