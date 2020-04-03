# -*- coding: utf-8 -*-
"""
读取yaml测试数据,并初始化测试参数

"""
import yaml
import os
import os.path
import random
from https_20190709.common.common_method import *
from copy import deepcopy
from https_20190709.common.Log_z import mylog
logger = mylog.get_log().get_logger()

class params:
    def __init__(self,yaml_file,func_name):
        self.yaml_file = os.path.join(os.path.abspath(os.pardir),'Params\\Param\\',yaml_file)
        self.func_name = func_name
        try:
            self.url = self.load_yaml()["url"]
        except:
            logger.error("func_name:%s  can not find in yaml", self.func_name)
            os._exit(0)
        self.data = self.load_yaml()["data"]
        self.all_params = self.get_all_params()
        self.must_params = self.get_must_params()

    def load_yaml(self):
        pages = {}
        try:
            with open(self.yaml_file, 'rb') as f:
                page = yaml.safe_load(f)
                pages.update(page)
        except:
            logger.error("yaml_file:%s  can not open",self.yaml_file)
            os._exit(0)
        pages = pages[self.func_name]
        return pages

    def get_single_param(self,name):
        value = self.load_yaml()
        try:
            value = value["data"][name]
        except:
            logger.error("key:%s not exist",name)
            value = ""
        return value
    def get_all_params(self):
        all_params = {}
        params = self.data
        for key,value in self.data.items():
                all_params.update({key:value[0]})
        return all_params

    def get_must_params(self):
        must_params = {}
        params = self.data
        for key,value in self.data.items():
            if self.data[key][1] == 1:
                must_params.update({key:value[0]})
        return must_params


class init_params(params):
    def __init__(self,yaml_file,func_name):
        super().__init__(yaml_file,func_name)

        self.idcard8k = r"D:\workfile\zhongkeyuan_workspace\test_photoes\idcard8k"
        self.picture8k = r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture8k"
        pho_file = os.listdir(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)")
        self.jpg_name = pho_file[random.randint(0,len(pho_file)-1)]
        feature_files = os.listdir(self.idcard8k)
        self.feature_file = feature_files[random.randint(0,len(feature_files)-1)]
        self.photo_base64 = to_base64(os.path.join(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)",self.jpg_name))
        self.all_params = self.create()

    def create(self):
        # params_instance = params("my_interface_test.yml","test_api_face_security_face_check")
        params_instance = params(self.yaml_file,self.func_name)
        for key in list(self.get_must_params().keys()):
            if key == "reqId":
                self.all_params[key] = get_uuid()
            elif key == "birthDate":
                self.all_params[key] = get_birthday(self.all_params["idCard"])
            elif key == "scenePhoto":
                self.all_params[key] = self.photo_base64
            elif key == "sceneFeature":
                self.all_params[key] = read_feature(os.path.join(self.picture8k, self.feature_file))
            elif key == "cardPhoto":
                self.all_params[key] = self.photo_base64
            elif key == "cardFeature":
                self.all_params[key] = read_feature(os.path.join(self.idcard8k, self.feature_file))
            elif key == "largePhoto":
                self.all_params[key] = self.photo_base64
        return self.all_params


def change_params(yml_file,func_name):
    changed_params = []
    tmp_inst =init_params(yml_file,func_name)
    changed_params = [tmp_inst.all_params]
    for i in list(tmp_inst.must_params.keys()):
        tmp_value = tmp_inst.all_params[i]
        tmp_inst.all_params[i] = ""
        tmp = deepcopy(tmp_inst.all_params)
        changed_params.append(tmp)
        tmp_inst.all_params[i] = tmp_value
    return changed_params


def get_params_list(yml_file,func_name):
    params_list = []
    tmp_inst =init_params(yml_file,func_name)
    tmp_inst.yaml_file
    with open(tmp_inst.yaml_file, "rb") as f:
        for i in f.readlines():
            line = i.decode('utf-8')
            for j in tmp_inst.all_params.keys():
                if j in line:
                    l = line.split(":")[0].strip()
                    params_list.append(l)
    return params_list

def stru_params_tuple(yml_file,func_name):
    params_list = []
    dict_list = change_params(yml_file,func_name)
    for i in dict_list:  #i:{'gateNo': 'T1AJ1', 'deviceId': 'T1AJ001', 'cardType': 0}
        params_tuple = ()
        for k in i.keys(): #k: {'gateNo', 'deviceId', 'cardType'}
            for j in get_params_list(yml_file,func_name): #j: yml读出来的参数
                if j == k:
                    params_tuple = params_tuple + (i[j],)
            # logger.debug(params_tuple)
        params_list.append(params_tuple)
    return params_list


if __name__ == '__main__':
    # data = init_params("my_interface_test.yml","test_api_face_security_face_check")
    # a = change_params("my_interface_test.yml","test_api_face_security_face_check")
    # print(len(a))
    # print(a)
    #
    # params_list = get_params_list("my_interface_test.yml","test_api_face_security_face_check")
    test_param = change_params("my_interface_test.yml","test_api_face_security_face_check")
    logger.debug(test_param[0]["birthDate"])