# Copyright 2012 NagiosQL-API authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding:utf-8 -*-
import logging
from nagiosql.client import NagiosQLAPI

logger = logging.getLogger(__name__)

class HostNagiosQLAPI(NagiosQLAPI):

    def create_host(self, hostname, ip, templateId):
        params = {"tfValue1": hostname, "tfValue3": hostname,"tfValue5": ip, "radValue1": 2, "radValue2": 2, 
                  "selValue1": 14, "chbRegister": 1, "chbActive": 1, "selTemplate": templateId, "modus": "insert",
                  "hidLimit": 0, "radValue5": 2, "radValue6": 2, "selValue2": 0, "radValue7": 2, "radValue8": 2,
                  "selValue3": 0, "radValue9": 2, "radValue10": 2, "radValue11": 2, "radValue12": 2, "radValue13": 2,
                  "radValue4": 2, "radValue3": 2, "selValue4": 0, "radValue14": 2, "selAccGr": 0}

        logger.debug("Saving hostname %s on nagiosql" % hostname)
        rget = self.GET("/nagiosql320/admin/templatedefinitions.php?dataId=&type=host&mode=add&def=%s" % templateId)
        rpost = self.POST("/nagiosql320/admin/hosts.php", params)

    def write_host(self, host_id):
        params = {"txtSearch": "", "modus": "checkform", "hidModify": "config", "hidListId": host_id, "hidLimit": 0, "hidSortBy": 1, "hidSortDir": "ASC", 
                  "hidSort": 0, "selModify": "none", "selTargetDomain": 1 }
        logger.debug("Calling method to write the file in disk")
        r = self.POST("/nagiosql320/admin/hosts.php", params)

    def delete_host(self, host_id):
        params = {"modus": "checkform", "hidModify": "delete", "hidListId": host_id, "hidLimit": 0, "hidSortBy": 1, "hidSortDir": "ASC",  "hidSort": 0, 
                  "selModify": "none", "selTargetDomain": 1 }
        logger.debug("Calling delete method")
        d = self.POST("/nagiosql320/admin/hosts.php", params)

    def write_hostgroups(self):
        params = {"modus":"make", "hidLimit": 0, "hidSortBy": 1, "hidSortDir": "ASC", "hidSort": 0, "selModify": "none", "selTargetDomain": 1}
        logger.debug("Calling write method of hostgroups")
        d = self.POST("/nagiosql320/admin/hostgroups.php", params)


