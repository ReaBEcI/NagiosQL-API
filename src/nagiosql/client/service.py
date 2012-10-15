# -*- coding:utf-8 -*-
import logging
from nagiosql.client import NagiosQLAPI

logger = logging.getLogger(__name__)

class ServiceNagiosQLAPI(NagiosQLAPI):

    def create_service(self, hostId, name, commandId, args, templateId="4::1"):
        config_name = name.replace (" ", "-")
        params = {"tfValue1": config_name, "mselValue1[]": hostId, "radValue1": 2, "radValue2": 2, "tfValue3": name, "chbRegister": 1, "chbActive": 1,
                  "radValue3": 2, "selValue1": commandId, "tfArg1": args, "selTemplate": templateId, "modus": "insert", "hidLimit": 0, "radValue4": 2,
                  "radValue5": 2, "radValue6": 2, "selValue2": 0, "radValue7": 2, "radValue8": 2, "selValue3": 0, "radValue9": 2, "radValue10": 2,
                  "radValue11": 2, "radValue12": 2, "radValue13": 2, "radValue14": 2, "radValue16": 2, "radValue15": 2, "selValue4": 0, "radValue17": 2,
                  "selAccGr": 0}
        logger.debug("create_service - parameters %s" % params)
        template = self.GET("/nagiosql320/admin/templatedefinitions.php?dataId=&type=service&mode=add&def=%s" % templateId)
        check = self.GET("/nagiosql320/admin/commandline.php?cname=%s" % commandId)
        rpost = self.POST("/nagiosql320/admin/services.php", params)
        

    def write_service(self, serviceId):
        params = {"selCnfName": "All configs", "modus": "checkform", "hidModify": "config",  "hidListId": serviceId, "hidLimit": 0, "hidSortBy": 1,
                  "hidSortDir": "ASC", "hidSort": 0, "selModify": "none", "selTargetDomain": 1}
        logger.debug("write_host - parameters %s" % params)
        rpost = self.POST("/nagiosql320/admin/services.php", params)

    def alter_service(self, configName, hostId, description, commandId, args, servicoId, templateId):
        params = {"tfValue1": configName, "tfValue2": configName, "mselValue1[]": hostId, "radValue1": 2, "radValue2": 2, "tfValue3": description,
                  "chbRegister": 1, "chbActive": 1, "radValue3": 2, "selValue1": commandId, "tfArg1": args, "selTemplate": templateId,
                  "modus": "modify", "hidId": servicoId, "hidLimit": 0, "radValue4": 2, "radValue5": 2, "radValue6": 2, "selValue2": 0, "radValue7": 2,
                  "radValue8": 2, "selValue3": 0, "radValue9": 2, "radValue10": 2, "radValue11": 2,  "radValue12": 2, "radValue13": 2, "radValue14": 2,
                  "radValue16": 2, "radValue15": 2, "selValue4": 0, "radValue17": 2, "selAccGr": 0}
        logger.debug("alter_service - parameters %s" % params)
        template = self.GET("/nagiosql320/admin/templatedefinitions.php?dataId=&type=service&mode=add&def=%s" % templateId)
        rpost = self.POST("/nagiosql320/admin/services.php", params)

    def delete_service(self, servicoId):
        params = {"selCnfName": "All configs", "modus": "checkform", "hidModify": "delete", "hidListId": servicoId, "hidLimit": 0, "hidSortBy": 1,
                  "hidSortDir": "ASC", "hidSort": 0, "selModify": "none", "selTargetDomain": 1}
        logger.debug("delete_service - parameters %s" % params)
        rpost = self.POST("/nagiosql320/admin/services.php", params)

    def write_servicegroups(self):
        params = {"modus": "make", "hidLimit": 0, "hidSortBy": 1, "hidSortDir": "ASC", "hidSort": 0, "selModify": "none", "selTargetDomain": 1}
        logger.debug("write_servicegroups - parameters %s" % params)
        rpost = self.POST("/nagiosql320/admin/servicegroups.php", params)
