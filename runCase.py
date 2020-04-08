import os,django,sys
from utils.inner import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestAutomation.settings')
django.setup()
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
import pytest
import requests
import traceback
from product_manage.models import Product,Notifier,Modular
from testcase_manage.models import TestCase
from django.forms.models import model_to_dict
import time
import json
import re
import pytest

# from testcase_manage.utils.dictUitl import dict_in
# from testcase_manage.utils.getTestData import get_test_data

# logging.basicConfig(level=logging.DEBUG)
# log = logging.getLogger()
# data = get_test_data()

# @pytest.mark.parametrize(*data)
# def test_api(case_info):
#     log.info(case_info)
#     input_data = case_info.get("input")
#     log.info("测试用例输入数据为：{}".format(input_data))
#     output_data = case_info.get("output")
#     log.info("测试用例期望输出数据为：{}".format(output_data))
#     url = input_data.get("url")
#     log.info("请求发送的地址:{}".format(url))
#     method = input_data.get("method")
#     log.info("请求发送的方法:{}".format(method))
#     role = input_data.get("role")
#     log.info("token:{}".format(role))
#     json_data = input_data.get("json_data")
#     log.info("请求发送的json为:{}".format(json_data))
#     res = requests.request(method, url, json=json_data)
#     actual_json = res.json()
#     log.info("响应体json转换后的信息为：{}".format(actual_json))

#     assert res.status_code in output_data.get("status_code")
#     expect_list = output_data.get("expect_body")
#     # [{'message': 'OK'}, {'data': {'phone': '18780373592', 'realname': '完美'}}]
#     for expect_json in expect_list:
#         log.info("正在断言响应体数据 {} ".format(expect_json))
#         assert dict_in(expect_json, actual_json)
# sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

class Testcase(object):
    def __init__(self,casename,certificate=None):
        super().__init__()
        self.pattern = re.compile(r'^\${(.+(\(.*\)))}', re.I)
        self.certificate = certificate
        self.obj = TestCase.objects.all().get(casename=casename)
        self.caseDict = model_to_dict(self.obj)
        self.url = self.generate_url()
        self.method = self.caseDict.get("method")
        self.header = self.generate_header()
        self.body = self.generate_body()
        logger.info(self.caseDict)
        logger.info(self.obj)


    def generate_url(self):
        host = self.obj.modular_name.host
        api = self.caseDict.get('url')
        return host + api

    def generate_header(self):
        return get_headers(self.caseDict.get('url'))
        
    def generate_body(self):
        # if '单接口' in self.caseDict.get('case_type'):
        #     logger.info('单接口测试开始...')
        #     if 'GET' in self.caseDict.get('method'):
        #         logger.info('GET 请求，功能暂时没开放！')
        #     if 'POST' in self.caseDict.get('method'):
        #         logger.info(type(_body))
                ### 请求参数处理
                # logger.info(_body)
        if self.caseDict.get("body",None):
            _body = json.loads(self.obj.body)
            for k,v in _body.items():
                try:
                    rst = self.pattern.match(v)  #v 为字符串类型时，才可以匹配，为整型时不可匹配
                except:
                    rst = None
                if rst:  #处理匹配到的 "${get_uuid({'name':1,'name1':'nam1'})}"
                    fun_name = rst.group(1)[:rst.group(1).find('(')]
                    parmsStr = rst.group(2).strip('(').strip(')') #string {"name":1,"name1":"nam1"}
                    if parmsStr:
                        parmsStr = parmsStr.replace("'","\"")
                        parmsDict = json.loads(parmsStr)
                        v = globals().get(fun_name)(parmsDict)
                    else:
                        v = globals().get(fun_name)()
                        _body[k] = v
            return _body
        return None

    def test_run(self):
        if self.caseDict.get("case_type") == '单接口':
            if self.method == 'POST':
                logger.info(self.url)
                logger.info(self.url)
                res = requests.post(url=self.url,
                                    headers=self.header,
                                    json=self.body,
                                    verify=self.certificate
                                    )
                res.close()
                logger.info(res.text)
                return res.text
            if self.method == 'GET':
                logger.info("GET 单接口暂没有！")
                return None
        else:
            logger.info("流程测试！！！")


if __name__=="__main__":
    cases = TestCase.objects.all().filter(casename='人脸识别记录-列表-条件查询')
    casesList = []
    for case in cases:
        casesList.append(Testcase(case))
        pytest.main(["-vv", "-s", "startRun.py", "--color=no", "--alluredir=./report/xml"])
