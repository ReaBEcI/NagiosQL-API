#encoding: utf-8
from django.test import TransactionTestCase
from django.utils import simplejson
from nagiosql.api.models import TblHost
import nagiosql.api.views
import datetime
import base64


class CreateHostTest(TransactionTestCase):
    fixtures = ['api/fixtures/tests_host.yaml']
    
    def setUp(self):
        self.host_original = nagiosql.api.views.HostNagiosQLAPI
        nagiosql.api.views.HostNagiosQLAPI = MockHostNagiosQLAPI
        credentials = base64.b64encode('admin:admin')
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Basic ' + credentials
        
    def tearDown(self):
        nagiosql.api.views.HostNagiosQLAPI = self.host_original

    def postJSON(self, url, data):
        return self.client.post(url, data=simplejson.dumps(data), content_type='application/json')

    def getJSON(self, url):
        return self.client.get(url, content_type='application/json')
        
    def deleteJSON(self, url):
        return self.client.delete(url, content_type='application/json')

    def assertResponseMessage(self, msg, response):
        data = simplejson.loads(response.content)
        self.assertEquals(data['message'], msg)        

    def test_create_host_return_successfully_create_message(self):
        host_data = {"hostname":[{"name":"hostname", "ip": "110.110.120.15", "template": "linux-server"}]}
        print "#"*50, TblHost.objects.all()
        response = self.postJSON('/api/host/', host_data)
        self.assertEqual(response.status_code, 200)
        self.assertResponseMessage(u'host(s) successfully created', response)

    def test_create_multiple_hosts_return_successfully_create_message(self):
        host_data = {"hostname":[{"name":"hostname", "ip": "110.110.120.15", "template": "linux-server"},{"name":"hostname", "ip": "110.110.120.16", "template": "sun-server"}]}
        print "#"*50, TblHost.objects.all()
        response = self.postJSON('/api/host/', host_data)
        self.assertEqual(response.status_code, 200)
        self.assertResponseMessage(u'host(s) successfully created', response)

    def test_create_host_with_invalid_template_returns_error(self):
        host_data = {"hostname":[{"name":"hostname", "ip": "120.110.110.10", "template": "TEMPLATE"}]}
        response = self.postJSON('/api/host/', host_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content, "TblHosttemplate matching query does not exist.")

    def test_create_host_with_invalid_ip_returns_error(self):
        host_data = {"hostname":[{"name":"hostname", "ip": "120.110.10.1000", "template": "linux-server"}]}
        response = self.postJSON('/api/host/', host_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, '{"message": "invalid parameters"}')

    def test_create_host_with_invalid_host_returns_error(self):
        host_data = {"hostname":[{"name":"teste$%", "ip": "120.110.110.10", "template": "linux-server"}]}
        response = self.postJSON('/api/host/', host_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, '{"message": "invalid parameters"}')
                
    def test_search_multiple_hosts(self):
        host_name = "hostname"
        response = self.getJSON('/api/host/%s' % host_name)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '[{"active": true, "message": "hostname hostname2-120.110.120.11 found"}, {"active": true, "message": "hostname hostname-110.110.120.15 found"}]')

    def test_search_host(self):
        host_name = "hostname-110.110.120.15"
        response = self.getJSON('/api/host/%s' % host_name)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '{"active": true, "message": "hostname hostname-110.110.120.15 found"}')

    def test_delete_host_return_associated_to_service(self):
        host_name = "hostna-10.249.31.24"
        response = self.deleteJSON('/api/host/%s' % host_name)
        self.assertEqual(response.content, '{"message": "hostname %s associated to service"}' % host_name)
        self.assertEqual(response.status_code, 400)
        
    def test_delete_host_return_ip_required(self):
        host_name = "hostname"
        response = self.deleteJSON('/api/host/%s' % host_name)
        self.assertEqual(response.content, '{"message": "Ip required"}')
        self.assertEqual(response.status_code, 400)

    def test_delete_host_successfully(self):
        host_name = "hostname-110.110.120.15"
        response = self.deleteJSON('/api/host/%s' % host_name)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '{"message": "hostname %s successfully deleted"}' % host_name)

class MockHostNagiosQLAPI(object):

    def __init__(self, hostname, username, password):
        self.create_host_count = 0
        self.write_host_count = 0
        self.alter_host_count = 0
        self.delete_host_count = 0
        self.write_hostgroups_count = 0

    def create_host(self, hostname, ip, template):
        print "*"*30, locals()

        host = TblHost.objects.create(host_name=hostname,address=ip, parents=0, parents_tploptions=2, hostgroups=1,hostgroups_tploptions=2,use_template=1,use_template_tploptions=2,active_checks_enabled=2,passive_checks_enabled=2,check_period=0,obsess_over_host=2,check_freshness=2,event_handler=0,event_handler_enabled=2,flap_detection_enabled=2,process_perf_data=2,retain_status_information=2,retain_nonstatus_information=2,contacts=0,contacts_tploptions=2,contact_groups=1, contact_groups_tploptions=2,notification_period=0, notifications_enabled=2, use_variables=0,last_modified=datetime.datetime.now(), access_group=0, config_id=1, register=1, active=1)
        self.create_host_count += 1
        return host.id

    def write_host(self, serviceId):
        self.write_host_count += 1

#    def alter_host(self, host_name, addess):
#        self.alter_host_count += 1
    
    def write_hostgroups(self):
        self.write_hostgroups_count += 1

    def delete_host(self, hostId):
        self.delete_host_count += 1


