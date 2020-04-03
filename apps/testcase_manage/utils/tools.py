# 与业务有关的工具
import requests

from testcase_manage.utils.AESUtil import AESUtil


def rm2token(role, modular):
    """
    通过给定的角色和模块获取token
    :param role: 角色对象
    :param modular: 模块对象
    :return: token
    """
    if role is None:
        return ""
    post_data = {"data": {
        "userid": role.account,
        "appid": modular.appid,
        "password": AESUtil(modular.key).encrypt(role.password)
    }}
    url = modular.host + modular._authapi
    res = requests.post(url, json=post_data)
    token = res.json().get("data").get("token") if res.json().get("code") in [200, 501] else ""
    return token


def str_status_code_to_list(status_code):
    """
    处理status_code为int列表
    :param status_code: status_code
    :return: int列表
    """
    return [int(s) for s in status_code.split(".") if s.isdigit()]
