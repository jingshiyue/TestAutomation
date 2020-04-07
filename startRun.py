import os,django,sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestAutomation.settings')
django.setup()
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
import pytest
import requests
import traceback

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

from product_manage.models import Product,Notifier,Modular
from testcase_manage.models import TestCase
import time
import json
import json,re
from django.forms.models import model_to_dict


def get_uuid(json=None):
    if json:
        return json.get("name","bbbbbbbbbbbbbb")
    return "aaaaaaaaaaaaaa"

obj = TestCase.objects.all().get(casename='人脸识别记录-列表-条件查询')
_body = obj.body
caseDict = model_to_dict(obj)
logger.info(caseDict)
'''
{'user': 1, 'id': 6, 'casename': '人脸识别记录-列表-条件查询', 'modular_name': 4, 'product_name': 3, 
'case_type': '单接口', 'method': 'POST', 'body_type': 'json', 'url': '/api/v1/face/record/search/list', 
'body': '{\r\n\t"reqId":{{get_uuid()}},\r\n\t"pageSize":10,\r\n\t"pageIndex":1,\r\n\t"isStranger":1\r\n}', 'file_path': '', 
'check_list': '{"status":0,"msg":"Success"}', 'desc': '第一个正式的单接口测试', 'level': '重要', 'skip': False}
'''
logger.info(_body)
'''
{
        "reqId":{{get_uuid()}},
        "pageSize":10,
        "pageIndex":1,
        "isStranger":1
}
'''
logger.info(obj.product_name) #动态布控
logger.info(obj.modular_name) #动态布控 -> 数据平台
logger.info('=================================')
host = obj.modular_name.host
api = caseDict.get('url')
url = host + api
logger.info(url)  #http://172.18.2.128:9091/face-bussiness-server/api/v1/face/record/search/list

pattern = re.compile(r'^\${(.+(\(.*\)))}', re.I)

if '单接口' in caseDict.get('case_type'):
    logger.info('单接口测试开始...')
    if 'GET' in caseDict.get('method'):
        logger.info('GET 请求，功能暂时没开放！')
    if 'POST' in caseDict.get('method'):
        logger.info(type(_body))
        ### 请求参数处理
        logger.info(_body)
        _body = json.loads(_body)
        for k,v in _body.items():
            try:
                rst = pattern.match(v)  #v 为字符串类型时，才可以匹配，为整型时不可匹配
            except:
                rst = None
            if rst:  #处理匹配到的 "${get_uuid({'name':1,'name1':'nam1'})}"
                fun_name = rst.group(1)[:rst.group(1).find('(')]
                parmsStr = rst.group(2).strip('(').strip(')') #string {"name":1,"name1":"nam1"}
                # logger.info(parmsStr) #{'name':1,'name1':'nam1'}
                if parmsStr:
                    parmsStr = parmsStr.replace("'","\"")
                    # logger.info(parmsStr)
                    parmsDict = json.loads(parmsStr)
                    v = globals().get(fun_name)(parmsDict)
                else:
                    v = globals().get(fun_name)()
                _body[k] = v
        logger.info(_body)
else:
    logger.info('流程测试开始...')
logger.info(url)
logger.info('=================================')

