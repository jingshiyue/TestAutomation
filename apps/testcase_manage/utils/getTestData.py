import yaml

from testcase_manage.models import TestCase
from testcase_manage.utils.tools import str_status_code_to_list, rm2token


def get_test_data():
    all_testcases = TestCase.objects.all()
    desc_list = []
    for test_case in all_testcases:
        # 请求地址
        url = test_case.api_name.modular_name.host + test_case.api_name.api_path
        # 请求方法
        method = test_case.method
        # 对应角色
        role = test_case.role
        # 被转换成python对象的yaml文本
        json_data = yaml.safe_load(test_case.body)
        # 响应码
        res_code = test_case.res_code
        # 需要检查的response body的列表
        check_list = yaml.safe_load(test_case.check_list)
        # 获取注入token
        token = rm2token(role, test_case.api_name.modular_name)
        if token:
            json_data["data"]["token"] = token

        data_dict = {"input": {"url": url, "method": method, "role": role or "无角色", "json_data": json_data},
                     "output": {"status_code": str_status_code_to_list(res_code),
                                "expect_body": check_list}}

        desc_list.append([data_dict, test_case.casename])

    return "case_info", [item[0] for item in desc_list], False, [item[1] for item in desc_list]
