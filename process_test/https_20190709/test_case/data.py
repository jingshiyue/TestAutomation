#!/usr/bin/python3
# Time : 2020/05/18 10:48 
# Author : zcl

"""
因为pytest框架,conftest中的变量不能被改写，所以放到data.py,供修改
将测试所需的变量都写入到该文件，便于后期维护管理
"""

flightInfo = {} #{'flight_no': 'DR6562', 'bdno': '02', 'date': '2020-05-09'}

# import configparser
# config = configparser.ConfigParser()
# config.read(r"process_test\https_20190709\test_case\pytest.ini")

