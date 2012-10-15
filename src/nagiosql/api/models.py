# Copyright 2012 NagiosQL-API authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

#encoding: utf-8
from django.db import models

class TblCommand(models.Model):
    command_name = models.CharField(unique=True, max_length=255)
    command_line = models.TextField()
    command_type = models.IntegerField()
    register = models.CharField(max_length=3)
    active = models.CharField(max_length=3)
    last_modified = models.DateTimeField()
    access_group = models.IntegerField()
    config_id = models.IntegerField(unique=False)
    class Meta:
        db_table = u'tbl_command'
# 
# class TblConfigtarget(models.Model):
#     id = models.IntegerField(primary_key=True)
#     target = models.TextField(unique=True)
#     alias = models.CharField(max_length=765)
#     server = models.CharField(max_length=765)
#     method = models.CharField(max_length=765)
#     user = models.CharField(max_length=765)
#     password = models.CharField(max_length=765)
#     ssh_key_path = models.CharField(max_length=765)
#     basedir = models.CharField(max_length=765)
#     hostconfig = models.CharField(max_length=765)
#     serviceconfig = models.CharField(max_length=765)
#     backupdir = models.CharField(max_length=765)
#     hostbackup = models.CharField(max_length=765)
#     servicebackup = models.CharField(max_length=765)
#     nagiosbasedir = models.CharField(max_length=765)
#     importdir = models.CharField(max_length=765)
#     picturedir = models.CharField(max_length=765)
#     commandfile = models.CharField(max_length=765)
#     binaryfile = models.CharField(max_length=765)
#     pidfile = models.CharField(max_length=765)
#     conffile = models.CharField(max_length=765)
#     version = models.IntegerField()
#     access_group = models.IntegerField()
#     active = models.CharField(max_length=3)
#     nodelete = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     class Meta:
#         db_table = u'tbl_configtarget'
# 
# class TblContact(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact_name = models.TextField(unique=True)
#     alias = models.CharField(max_length=765)
#     contactgroups = models.IntegerField()
#     contactgroups_tploptions = models.IntegerField()
#     host_notifications_enabled = models.IntegerField()
#     service_notifications_enabled = models.IntegerField()
#     host_notification_period = models.IntegerField()
#     service_notification_period = models.IntegerField()
#     host_notification_options = models.CharField(max_length=60)
#     service_notification_options = models.CharField(max_length=60)
#     host_notification_commands = models.IntegerField()
#     host_notification_commands_tploptions = models.IntegerField()
#     service_notification_commands = models.IntegerField()
#     service_notification_commands_tploptions = models.IntegerField()
#     can_submit_commands = models.IntegerField()
#     retain_status_information = models.IntegerField()
#     retain_nonstatus_information = models.IntegerField()
#     email = models.CharField(max_length=765)
#     pager = models.CharField(max_length=765)
#     address1 = models.CharField(max_length=765)
#     address2 = models.CharField(max_length=765)
#     address3 = models.CharField(max_length=765)
#     address4 = models.CharField(max_length=765)
#     address5 = models.CharField(max_length=765)
#     address6 = models.CharField(max_length=765)
#     name = models.CharField(max_length=765)
#     use_variables = models.IntegerField()
#     use_template = models.IntegerField()
#     use_template_tploptions = models.IntegerField()
#     register = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     access_group = models.IntegerField()
#     config_id = models.IntegerField(unique=True)
#     class Meta:
#         db_table = u'tbl_contact'
# 
# class TblContactgroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contactgroup_name = models.TextField(unique=True)
#     alias = models.CharField(max_length=765)
#     members = models.IntegerField()
#     contactgroup_members = models.IntegerField()
#     register = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     access_group = models.IntegerField()
#     config_id = models.IntegerField(unique=True)
#     class Meta:
#         db_table = u'tbl_contactgroup'
# 
# class TblContacttemplate(models.Model):
#     id = models.IntegerField(primary_key=True)
#     template_name = models.TextField(unique=True)
#     alias = models.CharField(max_length=765)
#     contactgroups = models.IntegerField()
#     contactgroups_tploptions = models.IntegerField()
#     host_notifications_enabled = models.IntegerField()
#     service_notifications_enabled = models.IntegerField()
#     host_notification_period = models.IntegerField()
#     service_notification_period = models.IntegerField()
#     host_notification_options = models.CharField(max_length=60)
#     service_notification_options = models.CharField(max_length=60)
#     host_notification_commands = models.IntegerField()
#     host_notification_commands_tploptions = models.IntegerField()
#     service_notification_commands = models.IntegerField()
#     service_notification_commands_tploptions = models.IntegerField()
#     can_submit_commands = models.IntegerField()
#     retain_status_information = models.IntegerField()
#     retain_nonstatus_information = models.IntegerField()
#     email = models.CharField(max_length=765)
#     pager = models.CharField(max_length=765)
#     address1 = models.CharField(max_length=765)
#     address2 = models.CharField(max_length=765)
#     address3 = models.CharField(max_length=765)
#     address4 = models.CharField(max_length=765)
#     address5 = models.CharField(max_length=765)
#     address6 = models.CharField(max_length=765)
#     use_variables = models.IntegerField()
#     use_template = models.IntegerField()
#     use_template_tploptions = models.IntegerField()
#     register = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     access_group = models.IntegerField()
#     config_id = models.IntegerField(unique=True)
#     class Meta:
#         db_table = u'tbl_contacttemplate'
# 
# class TblDatadomain(models.Model):
#     id = models.IntegerField(primary_key=True)
#     domain = models.TextField(unique=True)
#     alias = models.CharField(max_length=765)
#     targets = models.IntegerField()
#     version = models.IntegerField()
#     enable_common = models.IntegerField()
#     utf8_decode = models.IntegerField()
#     access_group = models.IntegerField()
#     active = models.CharField(max_length=3)
#     nodelete = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     class Meta:
#         db_table = u'tbl_datadomain'
# 
# class TblGroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     groupname = models.CharField(max_length=765)
#     description = models.CharField(max_length=765)
#     users = models.IntegerField()
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     class Meta:
#         db_table = u'tbl_group'
# 

class TblHost(models.Model):
    host_name = models.CharField(unique=True, max_length=255)
    alias = models.CharField(max_length=765)
    display_name = models.CharField(max_length=765)
    address = models.CharField(max_length=765)
    parents = models.IntegerField()
    parents_tploptions = models.IntegerField()
    hostgroups = models.IntegerField()
    hostgroups_tploptions = models.IntegerField()
    check_command = models.TextField()
    use_template = models.IntegerField()
    use_template_tploptions = models.IntegerField()
    initial_state = models.CharField(max_length=60)
    max_check_attempts = models.IntegerField(null=True, blank=True)
    check_interval = models.IntegerField(null=True, blank=True)
    retry_interval = models.IntegerField(null=True, blank=True)
    active_checks_enabled = models.IntegerField()
    passive_checks_enabled = models.IntegerField()
    check_period = models.IntegerField()
    obsess_over_host = models.IntegerField()
    check_freshness = models.IntegerField()
    freshness_threshold = models.IntegerField(null=True, blank=True)
    event_handler = models.IntegerField()
    event_handler_enabled = models.IntegerField()
    low_flap_threshold = models.IntegerField(null=True, blank=True)
    high_flap_threshold = models.IntegerField(null=True, blank=True)
    flap_detection_enabled = models.IntegerField()
    flap_detection_options = models.CharField(max_length=60)
    process_perf_data = models.IntegerField()
    retain_status_information = models.IntegerField()
    retain_nonstatus_information = models.IntegerField()
    contacts = models.IntegerField()
    contacts_tploptions = models.IntegerField()
    contact_groups = models.IntegerField()
    contact_groups_tploptions = models.IntegerField()
    notification_interval = models.IntegerField(null=True, blank=True)
    notification_period = models.IntegerField()
    first_notification_delay = models.IntegerField(null=True, blank=True)
    notification_options = models.CharField(max_length=60)
    notifications_enabled = models.IntegerField()
    stalking_options = models.CharField(max_length=60)
    notes = models.CharField(max_length=765)
    notes_url = models.CharField(max_length=765)
    action_url = models.CharField(max_length=765)
    icon_image = models.CharField(max_length=1500)
    icon_image_alt = models.CharField(max_length=765)
    vrml_image = models.CharField(max_length=765)
    statusmap_image = models.CharField(max_length=765)
    number_2d_coords = models.CharField(max_length=765, db_column=u'2d_coords') # Field renamed because it wasn't a valid Python identifier.
    number_3d_coords = models.CharField(max_length=765, db_column=u'3d_coords') # Field renamed because it wasn't a valid Python identifier.
    use_variables = models.IntegerField()
    name = models.CharField(max_length=765)
    register = models.CharField(max_length=3)
    active = models.CharField(max_length=3)
    last_modified = models.DateTimeField()
    access_group = models.IntegerField()
    config_id = models.IntegerField(unique=False)
    class Meta:
        db_table = u'tbl_host'
        
    @property
    def act(self):
        return self.active == "1"
        
    def __str__(self):
        return 'Host(%s)' % self.host_name
        
# 
# class TblHostdependency(models.Model):
#     id = models.IntegerField(primary_key=True)
#     config_name = models.TextField(unique=True)
#     dependent_host_name = models.IntegerField()
#     dependent_hostgroup_name = models.IntegerField()
#     host_name = models.IntegerField()
#     hostgroup_name = models.IntegerField()
#     inherits_parent = models.IntegerField()
#     execution_failure_criteria = models.CharField(max_length=60)
#     notification_failure_criteria = models.CharField(max_length=60)
#     dependency_period = models.IntegerField()
#     register = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     access_group = models.IntegerField()
#     config_id = models.IntegerField(unique=True)
#     import_hash = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'tbl_hostdependency'
# 
# class TblHostescalation(models.Model):
#     id = models.IntegerField(primary_key=True)
#     config_name = models.TextField(unique=True)
#     host_name = models.IntegerField()
#     hostgroup_name = models.IntegerField()
#     contacts = models.IntegerField()
#     contact_groups = models.IntegerField()
#     first_notification = models.IntegerField(null=True, blank=True)
#     last_notification = models.IntegerField(null=True, blank=True)
#     notification_interval = models.IntegerField(null=True, blank=True)
#     escalation_period = models.IntegerField()
#     escalation_options = models.CharField(max_length=60)
#     register = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     access_group = models.IntegerField()
#     config_id = models.IntegerField(unique=True)
#     import_hash = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'tbl_hostescalation'
# 
# class TblHostextinfo(models.Model):
#     id = models.IntegerField(primary_key=True)
#     host_name = models.IntegerField(unique=True)
#     notes = models.CharField(max_length=765)
#     notes_url = models.CharField(max_length=765)
#     action_url = models.CharField(max_length=765)
#     statistik_url = models.CharField(max_length=765)
#     icon_image = models.CharField(max_length=1500)
#     icon_image_alt = models.CharField(max_length=765)
#     vrml_image = models.CharField(max_length=765)
#     statusmap_image = models.CharField(max_length=765)
#     number_2d_coords = models.CharField(max_length=765, db_column=u'2d_coords') # Field renamed because it wasn't a valid Python identifier.
#     number_3d_coords = models.CharField(max_length=765, db_column=u'3d_coords') # Field renamed because it wasn't a valid Python identifier.
#     register = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     access_group = models.IntegerField()
#     config_id = models.IntegerField(unique=True)
#     class Meta:
#         db_table = u'tbl_hostextinfo'
# 
# class TblHostgroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     hostgroup_name = models.TextField(unique=True)
#     alias = models.CharField(max_length=765)
#     members = models.IntegerField()
#     hostgroup_members = models.IntegerField()
#     notes = models.CharField(max_length=765)
#     notes_url = models.CharField(max_length=765)
#     action_url = models.CharField(max_length=765)
#     register = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     access_group = models.IntegerField()
#     config_id = models.IntegerField(unique=True)
#     class Meta:
#         db_table = u'tbl_hostgroup'
# 
class TblHosttemplate(models.Model):
    template_name = models.CharField(unique=True, max_length=255)
    alias = models.CharField(max_length=765)
    parents = models.IntegerField()
    parents_tploptions = models.IntegerField()
    hostgroups = models.IntegerField()
    hostgroups_tploptions = models.IntegerField()
    check_command = models.TextField()
    use_template = models.IntegerField()
    use_template_tploptions = models.IntegerField()
    initial_state = models.CharField(max_length=60)
    max_check_attempts = models.IntegerField(null=True, blank=True)
    check_interval = models.IntegerField(null=True, blank=True)
    retry_interval = models.IntegerField(null=True, blank=True)
    active_checks_enabled = models.IntegerField()
    passive_checks_enabled = models.IntegerField()
    check_period = models.IntegerField()
    obsess_over_host = models.IntegerField()
    check_freshness = models.IntegerField()
    freshness_threshold = models.IntegerField(null=True, blank=True)
    event_handler = models.IntegerField()
    event_handler_enabled = models.IntegerField()
    low_flap_threshold = models.IntegerField(null=True, blank=True)
    high_flap_threshold = models.IntegerField(null=True, blank=True)
    flap_detection_enabled = models.IntegerField()
    flap_detection_options = models.CharField(max_length=60)
    process_perf_data = models.IntegerField()
    retain_status_information = models.IntegerField()
    retain_nonstatus_information = models.IntegerField()
    contacts = models.IntegerField()
    contacts_tploptions = models.IntegerField()
    contact_groups = models.IntegerField()
    contact_groups_tploptions = models.IntegerField()
    notification_interval = models.IntegerField(null=True, blank=True)
    notification_period = models.IntegerField()
    first_notification_delay = models.IntegerField(null=True, blank=True)
    notification_options = models.CharField(max_length=60)
    notifications_enabled = models.IntegerField()
    stalking_options = models.CharField(max_length=60)
    notes = models.CharField(max_length=765)
    notes_url = models.CharField(max_length=765)
    action_url = models.CharField(max_length=765)
    icon_image = models.CharField(max_length=1500)
    icon_image_alt = models.CharField(max_length=765)
    vrml_image = models.CharField(max_length=765)
    statusmap_image = models.CharField(max_length=765)
    number_2d_coords = models.CharField(max_length=765, db_column=u'2d_coords') # Field renamed because it wasn't a valid Python identifier.
    number_3d_coords = models.CharField(max_length=765, db_column=u'3d_coords') # Field renamed because it wasn't a valid Python identifier.
    use_variables = models.IntegerField()
    register = models.CharField(max_length=3)
    active = models.CharField(max_length=3)
    last_modified = models.DateTimeField()
    access_group = models.IntegerField()
    config_id = models.IntegerField(unique=False)
    class Meta:
        db_table = u'tbl_hosttemplate'
# 
# class TblInfo(models.Model):
#     id = models.IntegerField(primary_key=True)
#     key1 = models.CharField(max_length=300)
#     key2 = models.CharField(max_length=300)
#     version = models.CharField(max_length=150)
#     language = models.CharField(max_length=150)
#     infotext = models.TextField()
#     class Meta:
#         db_table = u'tbl_info'
# 
# class TblLanguage(models.Model):
#     id = models.IntegerField(primary_key=True)
#     language = models.CharField(max_length=765)
#     locale = models.CharField(max_length=765)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     class Meta:
#         db_table = u'tbl_language'
# 
# class TblLnkcontacttocommandhost(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkContactToCommandHost'
# 
# class TblLnkcontacttocommandservice(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkContactToCommandService'
# 
# class TblLnkcontacttocontactgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkContactToContactgroup'
# 
# class TblLnkcontacttocontacttemplate(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     idsort = models.IntegerField(db_column='idSort') # Field name made lowercase.
#     idtable = models.IntegerField(primary_key=True, db_column='idTable') # Field name made lowercase.
#     class Meta:
#         db_table = u'tbl_lnkContactToContacttemplate'
# 
# class TblLnkcontacttovariabledefinition(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     class Meta:
#         db_table = u'tbl_lnkContactToVariabledefinition'
# 
# class TblLnkcontactgrouptocontact(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkContactgroupToContact'
# 
# class TblLnkcontactgrouptocontactgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkContactgroupToContactgroup'
# 
# class TblLnkcontacttemplatetocommandhost(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkContacttemplateToCommandHost'
# 
# class TblLnkcontacttemplatetocommandservice(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkContacttemplateToCommandService'
# 
# class TblLnkcontacttemplatetocontactgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkContacttemplateToContactgroup'
# 
# class TblLnkcontacttemplatetocontacttemplate(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     idsort = models.IntegerField(db_column='idSort') # Field name made lowercase.
#     idtable = models.IntegerField(primary_key=True, db_column='idTable') # Field name made lowercase.
#     class Meta:
#         db_table = u'tbl_lnkContacttemplateToContacttemplate'
# 
# class TblLnkcontacttemplatetovariabledefinition(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     class Meta:
#         db_table = u'tbl_lnkContacttemplateToVariabledefinition'
# 
# class TblLnkgrouptouser(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     read = models.CharField(max_length=3)
#     write = models.CharField(max_length=3)
#     link = models.CharField(max_length=3)
#     class Meta:
#         db_table = u'tbl_lnkGroupToUser'
# 
# class TblLnkhosttocontact(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostToContact'
# 
# class TblLnkhosttocontactgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostToContactgroup'
# 
# class TblLnkhosttohost(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostToHost'
# 
# class TblLnkhosttohostgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostToHostgroup'
# 
# class TblLnkhosttohosttemplate(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     idsort = models.IntegerField(db_column='idSort') # Field name made lowercase.
#     idtable = models.IntegerField(primary_key=True, db_column='idTable') # Field name made lowercase.
#     class Meta:
#         db_table = u'tbl_lnkHostToHosttemplate'
# 
# class TblLnkhosttovariabledefinition(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     class Meta:
#         db_table = u'tbl_lnkHostToVariabledefinition'
# 
# class TblLnkhostdependencytohostDh(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostdependencyToHost_DH'
# 
# class TblLnkhostdependencytohostH(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostdependencyToHost_H'
# 
# class TblLnkhostdependencytohostgroupDh(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostdependencyToHostgroup_DH'
# 
# class TblLnkhostdependencytohostgroupH(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostdependencyToHostgroup_H'
# 
# class TblLnkhostescalationtocontact(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostescalationToContact'
# 
# class TblLnkhostescalationtocontactgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostescalationToContactgroup'
# 
# class TblLnkhostescalationtohost(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostescalationToHost'
# 
# class TblLnkhostescalationtohostgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostescalationToHostgroup'
# 
# class TblLnkhostgrouptohost(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostgroupToHost'
# 
# class TblLnkhostgrouptohostgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHostgroupToHostgroup'
# 
# class TblLnkhosttemplatetocontact(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHosttemplateToContact'
# 
# class TblLnkhosttemplatetocontactgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHosttemplateToContactgroup'
# 
# class TblLnkhosttemplatetohost(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHosttemplateToHost'
# 
# class TblLnkhosttemplatetohostgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkHosttemplateToHostgroup'
# 
# class TblLnkhosttemplatetohosttemplate(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     idsort = models.IntegerField(db_column='idSort') # Field name made lowercase.
#     idtable = models.IntegerField(primary_key=True, db_column='idTable') # Field name made lowercase.
#     class Meta:
#         db_table = u'tbl_lnkHosttemplateToHosttemplate'
# 
# class TblLnkhosttemplatetovariabledefinition(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     class Meta:
#         db_table = u'tbl_lnkHosttemplateToVariabledefinition'
# 
# class TblLnkservicetocontact(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServiceToContact'
# 
# class TblLnkservicetocontactgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServiceToContactgroup'
# 
class TblLnkservicetohost(models.Model):
    idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
    idslave = models.IntegerField(db_column='idSlave') # Field name made lowercase.
    exclude = models.IntegerField()
    class Meta:
        db_table = u'tbl_lnkServiceToHost'
# 
# class TblLnkservicetohostgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServiceToHostgroup'
# 
# class TblLnkservicetoservicegroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServiceToServicegroup'
# 
class TblLnkservicetoservicetemplate(models.Model):
    idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
    idslave = models.IntegerField(db_column='idSlave') # Field name made lowercase.
    idsort = models.IntegerField(db_column='idSort') # Field name made lowercase.
    idtable = models.IntegerField(db_column='idTable') # Field name made lowercase.
    class Meta:
        db_table = u'tbl_lnkServiceToServicetemplate'
# 
# class TblLnkservicetovariabledefinition(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     class Meta:
#         db_table = u'tbl_lnkServiceToVariabledefinition'
# 
# class TblLnkservicedependencytohostDh(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicedependencyToHost_DH'
# 
# class TblLnkservicedependencytohostH(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicedependencyToHost_H'
# 
# class TblLnkservicedependencytohostgroupDh(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicedependencyToHostgroup_DH'
# 
# class TblLnkservicedependencytohostgroupH(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicedependencyToHostgroup_H'
# 
# class TblLnkservicedependencytoserviceDs(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     strslave = models.CharField(max_length=765, db_column='strSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicedependencyToService_DS'
# 
# class TblLnkservicedependencytoserviceS(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     strslave = models.CharField(max_length=765, db_column='strSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicedependencyToService_S'
# 
# class TblLnkservicedependencytoservicegroupDs(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicedependencyToServicegroup_DS'
# 
# class TblLnkservicedependencytoservicegroupS(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicedependencyToServicegroup_S'
# 
# class TblLnkserviceescalationtocontact(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServiceescalationToContact'
# 
# class TblLnkserviceescalationtocontactgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServiceescalationToContactgroup'
# 
# class TblLnkserviceescalationtohost(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServiceescalationToHost'
# 
# class TblLnkserviceescalationtohostgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServiceescalationToHostgroup'
# 
# class TblLnkserviceescalationtoservice(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     strslave = models.CharField(max_length=765, db_column='strSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServiceescalationToService'
# 
# class TblLnkserviceescalationtoservicegroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServiceescalationToServicegroup'
# 
# class TblLnkservicegrouptoservice(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslaveh = models.IntegerField(primary_key=True, db_column='idSlaveH') # Field name made lowercase.
#     idslavehg = models.IntegerField(primary_key=True, db_column='idSlaveHG') # Field name made lowercase.
#     idslaves = models.IntegerField(primary_key=True, db_column='idSlaveS') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicegroupToService'
# 
# class TblLnkservicegrouptoservicegroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicegroupToServicegroup'
# 
# class TblLnkservicetemplatetocontact(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicetemplateToContact'
# 
# class TblLnkservicetemplatetocontactgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicetemplateToContactgroup'
# 
# class TblLnkservicetemplatetohost(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicetemplateToHost'
# 
# class TblLnkservicetemplatetohostgroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicetemplateToHostgroup'
# 
# class TblLnkservicetemplatetoservicegroup(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkServicetemplateToServicegroup'
# 
# class TblLnkservicetemplatetoservicetemplate(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     idsort = models.IntegerField(db_column='idSort') # Field name made lowercase.
#     idtable = models.IntegerField(primary_key=True, db_column='idTable') # Field name made lowercase.
#     class Meta:
#         db_table = u'tbl_lnkServicetemplateToServicetemplate'
# 
# class TblLnkservicetemplatetovariabledefinition(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     class Meta:
#         db_table = u'tbl_lnkServicetemplateToVariabledefinition'
# 
# class TblLnktimeperiodtotimeperiod(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkTimeperiodToTimeperiod'
# 
# class TblLnktimeperiodtotimeperioduse(models.Model):
#     idmaster = models.IntegerField(primary_key=True, db_column='idMaster') # Field name made lowercase.
#     idslave = models.IntegerField(primary_key=True, db_column='idSlave') # Field name made lowercase.
#     exclude = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_lnkTimeperiodToTimeperiodUse'
# 
# class TblLogbook(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     time = models.DateTimeField()
#     user = models.CharField(max_length=765)
#     ipadress = models.CharField(max_length=765)
#     domain = models.CharField(max_length=765)
#     entry = models.TextField()
#     class Meta:
#         db_table = u'tbl_logbook'
# 
# class TblMenu(models.Model):
#     mnuid = models.IntegerField(primary_key=True, db_column='mnuId') # Field name made lowercase.
#     mnutopid = models.IntegerField(db_column='mnuTopId') # Field name made lowercase.
#     mnugrpid = models.IntegerField(db_column='mnuGrpId') # Field name made lowercase.
#     mnucntid = models.IntegerField(db_column='mnuCntId') # Field name made lowercase.
#     mnuname = models.CharField(max_length=765, db_column='mnuName') # Field name made lowercase.
#     mnulink = models.CharField(max_length=765, db_column='mnuLink') # Field name made lowercase.
#     mnuactive = models.IntegerField(db_column='mnuActive') # Field name made lowercase.
#     mnuorderid = models.IntegerField(db_column='mnuOrderId') # Field name made lowercase.
#     class Meta:
#         db_table = u'tbl_menu'
# 
# class TblRelationinformation(models.Model):
#     id = models.IntegerField(primary_key=True)
#     master = models.CharField(max_length=765)
#     tablename1 = models.CharField(max_length=765, db_column='tableName1') # Field name made lowercase.
#     tablename2 = models.CharField(max_length=765, db_column='tableName2') # Field name made lowercase.
#     fieldname = models.CharField(max_length=765, db_column='fieldName') # Field name made lowercase.
#     linktable = models.CharField(max_length=765, db_column='linkTable') # Field name made lowercase.
#     target1 = models.CharField(max_length=765)
#     target2 = models.CharField(max_length=765)
#     targetkey = models.CharField(max_length=765, db_column='targetKey') # Field name made lowercase.
#     fullrelation = models.IntegerField(db_column='fullRelation') # Field name made lowercase.
#     flags = models.CharField(max_length=765)
#     type = models.IntegerField()
#     class Meta:
#         db_table = u'tbl_relationinformation'
# 
class TblService(models.Model):
    config_name = models.CharField(max_length=765)
    host_name = models.IntegerField()
    host_name_tploptions = models.IntegerField()
    hostgroup_name = models.IntegerField()
    hostgroup_name_tploptions = models.IntegerField()
    service_description = models.CharField(max_length=765)
    display_name = models.CharField(max_length=765)
    servicegroups = models.IntegerField()
    servicegroups_tploptions = models.IntegerField()
    use_template = models.IntegerField()
    use_template_tploptions = models.IntegerField()
    check_command = models.TextField()
    is_volatile = models.IntegerField()
    initial_state = models.CharField(max_length=60)
    max_check_attempts = models.IntegerField(null=True, blank=True)
    check_interval = models.IntegerField(null=True, blank=True)
    retry_interval = models.IntegerField(null=True, blank=True)
    active_checks_enabled = models.IntegerField()
    passive_checks_enabled = models.IntegerField()
    check_period = models.IntegerField()
    parallelize_check = models.IntegerField()
    obsess_over_service = models.IntegerField()
    check_freshness = models.IntegerField()
    freshness_threshold = models.IntegerField(null=True, blank=True)
    event_handler = models.IntegerField()
    event_handler_enabled = models.IntegerField()
    low_flap_threshold = models.IntegerField(null=True, blank=True)
    high_flap_threshold = models.IntegerField(null=True, blank=True)
    flap_detection_enabled = models.IntegerField()
    flap_detection_options = models.CharField(max_length=60)
    process_perf_data = models.IntegerField()
    retain_status_information = models.IntegerField()
    retain_nonstatus_information = models.IntegerField()
    notification_interval = models.IntegerField(null=True, blank=True)
    first_notification_delay = models.IntegerField(null=True, blank=True)
    notification_period = models.IntegerField()
    notification_options = models.CharField(max_length=60)
    notifications_enabled = models.IntegerField()
    contacts = models.IntegerField()
    contacts_tploptions = models.IntegerField()
    contact_groups = models.IntegerField()
    contact_groups_tploptions = models.IntegerField()
    stalking_options = models.CharField(max_length=60)
    notes = models.CharField(max_length=765)
    notes_url = models.CharField(max_length=765)
    action_url = models.CharField(max_length=765)
    icon_image = models.CharField(max_length=1500)
    icon_image_alt = models.CharField(max_length=765)
    use_variables = models.IntegerField()
    name = models.CharField(max_length=765)
    register = models.CharField(max_length=3)
    active = models.CharField(max_length=3)
    last_modified = models.DateTimeField()
    access_group = models.IntegerField()
    config_id = models.IntegerField()
    import_hash = models.CharField(max_length=765)
    class Meta:
        db_table = u'tbl_service'

# class TblServicedependency(models.Model):
#     id = models.IntegerField(primary_key=True)
#     config_name = models.TextField(unique=True)
#     dependent_host_name = models.IntegerField()
#     dependent_hostgroup_name = models.IntegerField()
#     dependent_service_description = models.IntegerField()
#     dependent_servicegroup_name = models.IntegerField()
#     host_name = models.IntegerField()
#     hostgroup_name = models.IntegerField()
#     service_description = models.IntegerField()
#     servicegroup_name = models.IntegerField()
#     inherits_parent = models.IntegerField()
#     execution_failure_criteria = models.CharField(max_length=60)
#     notification_failure_criteria = models.CharField(max_length=60)
#     dependency_period = models.IntegerField()
#     register = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     access_group = models.IntegerField()
#     config_id = models.IntegerField(unique=True)
#     import_hash = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'tbl_servicedependency'
# 
# class TblServiceescalation(models.Model):
#     id = models.IntegerField(primary_key=True)
#     config_name = models.CharField(max_length=765)
#     host_name = models.IntegerField()
#     hostgroup_name = models.IntegerField()
#     service_description = models.IntegerField()
#     servicegroup_name = models.IntegerField()
#     contacts = models.IntegerField()
#     contact_groups = models.IntegerField()
#     first_notification = models.IntegerField(null=True, blank=True)
#     last_notification = models.IntegerField(null=True, blank=True)
#     notification_interval = models.IntegerField(null=True, blank=True)
#     escalation_period = models.IntegerField()
#     escalation_options = models.CharField(max_length=60)
#     register = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     access_group = models.IntegerField()
#     config_id = models.IntegerField()
#     import_hash = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'tbl_serviceescalation'
# 
# class TblServiceextinfo(models.Model):
#     id = models.IntegerField(primary_key=True)
#     host_name = models.IntegerField(unique=True)
#     service_description = models.IntegerField(unique=True)
#     notes = models.CharField(max_length=765)
#     notes_url = models.CharField(max_length=765)
#     action_url = models.CharField(max_length=765)
#     statistic_url = models.CharField(max_length=765)
#     icon_image = models.CharField(max_length=1500)
#     icon_image_alt = models.CharField(max_length=765)
#     register = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     access_group = models.IntegerField()
#     config_id = models.IntegerField(unique=True)
#     import_hash = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'tbl_serviceextinfo'
# 
# class TblServicegroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     servicegroup_name = models.TextField(unique=True)
#     alias = models.CharField(max_length=765)
#     members = models.IntegerField()
#     servicegroup_members = models.IntegerField()
#     notes = models.CharField(max_length=765, blank=True)
#     notes_url = models.CharField(max_length=765, blank=True)
#     action_url = models.CharField(max_length=765, blank=True)
#     register = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     access_group = models.IntegerField()
#     config_id = models.IntegerField(unique=True)
#     class Meta:
#         db_table = u'tbl_servicegroup'
# 
# class TblServicetemplate(models.Model):
#     id = models.IntegerField(primary_key=True)
#     template_name = models.TextField(unique=True)
#     host_name = models.IntegerField()
#     host_name_tploptions = models.IntegerField()
#     hostgroup_name = models.IntegerField()
#     hostgroup_name_tploptions = models.IntegerField()
#     service_description = models.CharField(max_length=765)
#     display_name = models.CharField(max_length=765)
#     servicegroups = models.IntegerField()
#     servicegroups_tploptions = models.IntegerField()
#     use_template = models.IntegerField()
#     use_template_tploptions = models.IntegerField()
#     check_command = models.TextField()
#     is_volatile = models.IntegerField()
#     initial_state = models.CharField(max_length=60)
#     max_check_attempts = models.IntegerField(null=True, blank=True)
#     check_interval = models.IntegerField(null=True, blank=True)
#     retry_interval = models.IntegerField(null=True, blank=True)
#     active_checks_enabled = models.IntegerField()
#     passive_checks_enabled = models.IntegerField()
#     check_period = models.IntegerField()
#     parallelize_check = models.IntegerField()
#     obsess_over_service = models.IntegerField()
#     check_freshness = models.IntegerField()
#     freshness_threshold = models.IntegerField(null=True, blank=True)
#     event_handler = models.IntegerField()
#     event_handler_enabled = models.IntegerField()
#     low_flap_threshold = models.IntegerField(null=True, blank=True)
#     high_flap_threshold = models.IntegerField(null=True, blank=True)
#     flap_detection_enabled = models.IntegerField()
#     flap_detection_options = models.CharField(max_length=60)
#     process_perf_data = models.IntegerField()
#     retain_status_information = models.IntegerField()
#     retain_nonstatus_information = models.IntegerField()
#     notification_interval = models.IntegerField(null=True, blank=True)
#     first_notification_delay = models.IntegerField(null=True, blank=True)
#     notification_period = models.IntegerField()
#     notification_options = models.CharField(max_length=60)
#     notifications_enabled = models.IntegerField()
#     contacts = models.IntegerField()
#     contacts_tploptions = models.IntegerField()
#     contact_groups = models.IntegerField()
#     contact_groups_tploptions = models.IntegerField()
#     stalking_options = models.CharField(max_length=60)
#     notes = models.CharField(max_length=765)
#     notes_url = models.CharField(max_length=765)
#     action_url = models.CharField(max_length=765)
#     icon_image = models.CharField(max_length=1500)
#     icon_image_alt = models.CharField(max_length=765)
#     use_variables = models.IntegerField()
#     register = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     access_group = models.IntegerField()
#     config_id = models.IntegerField(unique=True)
#     import_hash = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'tbl_servicetemplate'
# 
# class TblSettings(models.Model):
#     id = models.IntegerField(primary_key=True)
#     category = models.CharField(max_length=60)
#     name = models.CharField(max_length=90, unique=True)
#     value = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'tbl_settings'
# 
# class TblTablestatus(models.Model):
#     id = models.IntegerField(primary_key=True)
#     tablename = models.CharField(max_length=765, db_column='tableName') # Field name made lowercase.
#     domainid = models.IntegerField(db_column='domainId') # Field name made lowercase.
#     updatetime = models.DateTimeField(db_column='updateTime') # Field name made lowercase.
#     class Meta:
#         db_table = u'tbl_tablestatus'
# 
# class TblTimedefinition(models.Model):
#     id = models.IntegerField(primary_key=True)
#     tipid = models.IntegerField(db_column='tipId') # Field name made lowercase.
#     definition = models.CharField(max_length=765)
#     range = models.TextField()
#     last_modified = models.DateTimeField()
#     class Meta:
#         db_table = u'tbl_timedefinition'
# 
# class TblTimeperiod(models.Model):
#     id = models.IntegerField(primary_key=True)
#     timeperiod_name = models.TextField(unique=True)
#     alias = models.CharField(max_length=765)
#     exclude = models.IntegerField()
#     use_template = models.IntegerField()
#     name = models.CharField(max_length=765)
#     register = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     last_modified = models.DateTimeField()
#     access_group = models.IntegerField()
#     config_id = models.IntegerField(unique=True)
#     class Meta:
#         db_table = u'tbl_timeperiod'
# 
# class TblUser(models.Model):
#     id = models.IntegerField(primary_key=True)
#     username = models.TextField(unique=True)
#     alias = models.CharField(max_length=765)
#     password = models.CharField(max_length=765)
#     admin_enable = models.CharField(max_length=3)
#     wsauth = models.CharField(max_length=3)
#     active = models.CharField(max_length=3)
#     nodelete = models.CharField(max_length=3)
#     language = models.CharField(max_length=60)
#     domain = models.IntegerField()
#     last_login = models.DateTimeField()
#     last_modified = models.DateTimeField()
#     class Meta:
#         db_table = u'tbl_user'
# 
# class TblVariabledefinition(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=765)
#     value = models.CharField(max_length=765)
#     last_modified = models.DateTimeField()
#     class Meta:
#         db_table = u'tbl_variabledefinition'

