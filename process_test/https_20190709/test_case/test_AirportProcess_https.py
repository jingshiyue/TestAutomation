#!/usr/bin/python3
# Time : 2019/7/23 8:57 
# Author : zcl
# from https_20190709.API_https.BlackList import *
import pytest
from https_20190709.common.common_method import *
from https_20190709.common.params_init_z import *
from https_20190709.API_https.AirportProcess import *
from https_20190709.common.Log_z import mylog
logger = mylog.get_log().get_logger()



# host = "https://192.168.5.15:4433/security-server"
# certificate_file = "D:/workfile/workspace/https_20190709/API_https/cacert.crt"

test_param = change_params("my_interface_test.yml","test_api_face_security_face_check")
# print(test_param)

params_list = get_params_list("my_interface_test.yml","test_api_face_security_face_check")



class Test_AirportProcess():

    def setup_class(self):
        self.ap = AirportProcess()

    @pytest.mark.parametrize("params",test_param)
    def test_api_face_security_face_check(self,params):
        logged_param = ""
        for key,value in params.items():
            if params[key] == "":
                log_param = key
        if log_param:
            logger.debug("当前参数:%s 为空" %logged_param)
        else:
            logger.debug("所有参数已准备")

        res = self.ap.api_face_security_face_check(
                                 reqId=params["reqId"],
                                 gateNo=params["gateNo"],
                                 deviceId=params["deviceId"],
                                 cardType=params["cardType"],
                                 idCard=params["idCard"],
                                 nameZh=params["nameZh"],
                                 nameEn=params["nameEn"],
                                 age=params["age"],
                                 sex=params["sex"],
                                 birthDate=params["birthDate"],
                                 address=params["address"],
                                 certificateValidity=params["certificateValidity"],
                                 nationality=params["nationality"],
                                 ethnic=params["ethnic"],
                                 contactWay=params["contactWay"],
                                 scenePhoto=params["scenePhoto"],
                                 sceneFeature=params["sceneFeature"],
                                 cardPhoto=params["cardPhoto"],
                                 cardFeature=params["cardFeature"],
                                 largePhoto=params["largePhoto"]
        )
        logger.debug(res.text)

if __name__=="__main__":
    pytest.main(["-s","test_AirportProcess_https.py"])