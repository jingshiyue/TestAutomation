import logging

import pytest
import requests

from testcase_manage.utils.dictUitl import dict_in
from testcase_manage.utils.getTestData import get_test_data

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

data = get_test_data()


@pytest.mark.parametrize(*data)
def test_api(case_info):
    log.info(case_info)
    input_data = case_info.get("input")
    log.info("测试用例输入数据为：{}".format(input_data))
    output_data = case_info.get("output")
    log.info("测试用例期望输出数据为：{}".format(output_data))
    url = input_data.get("url")
    log.info("请求发送的地址:{}".format(url))
    method = input_data.get("method")
    log.info("请求发送的方法:{}".format(method))
    role = input_data.get("role")
    log.info("token:{}".format(role))
    json_data = input_data.get("json_data")
    log.info("请求发送的json为:{}".format(json_data))
    res = requests.request(method, url, json=json_data)
    actual_json = res.json()
    log.info("响应体json转换后的信息为：{}".format(actual_json))

    assert res.status_code in output_data.get("status_code")
    expect_list = output_data.get("expect_body")
    # [{'message': 'OK'}, {'data': {'phone': '18780373592', 'realname': '完美'}}]
    for expect_json in expect_list:
        log.info("正在断言响应体数据 {} ".format(expect_json))
        assert dict_in(expect_json, actual_json)
