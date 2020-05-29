#!/usr/bin/python3
# Time : 2019/8/22 10:48 
# Author : zcl
"""
这个conftest,用于执行runcase.py,定制runcase.py生成的html报告
"""
import pytest
import time
from datetime import datetime
from py._xmlgen import html
# from py.xml import html
import os,django,sys
import logging
logger = logging.getLogger(__name__)


import pytest
# from py.xml import html
d1 = html.p('"值机信息":"航班日期、航班号、登机口、登机序号、座位号、身份证号、姓名"')
d2 =  html.p('"系统安检":"A门传入身份证+证件照，B门传入身份证+现场照A、现场照特征A+证件照、证件照特征"')





def read_from_config(configfile,secion_name, item_name):
    import configparser
    config = configparser.ConfigParser()
    config.read(configfile,encoding='utf-8')
    return config.get(secion_name, item_name)

def write_to_config(confPath,secion_name, item_name, value):
    import configparser
    config = configparser.ConfigParser()
    config.read(confPath,encoding='utf-8')
    if(config.has_section(secion_name) == False):
        config.add_section(secion_name)
    config.set(secion_name,item_name,value)
    with open(confPath, 'w', encoding="utf-8") as config_file:
        config.write(config_file)

def pytest_configure(config):
    try:
        config._metadata["系统环境"] = "Windows Server 2008 Enterprise"
        config._metadata["项目名称"] = read_from_config("testbed.ini","Product","name")
    except Exception as e:
        logger.info(e)
    config._metadata.pop("JAVA_HOME")
    config._metadata.pop("Packages")
    config._metadata.pop("Plugins")
    config._metadata.pop("Python")
    config._metadata.pop("Platform")
    

    
def pytest_html_results_table_header(cells):
    #设置table的header
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Test Data'))
    cells.pop(-1)
def pytest_html_results_table_row(report, cells):
    #加第二、三列,移除最后一列
    caseName = report.nodeid.split("::")[1][9:]
    from startRun import testCaseInputData
    inputData = ""
    for k,v in testCaseInputData.items():
        if k ==caseName:
            inputData = testCaseInputData[caseName]
    cells.insert(2, html.td(report.description))
    cells.insert(3,html.td(inputData))
    cells.pop(-1)
    

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)


if __name__ == "__main__":
    t1 = "[2020-05-29 10:52:45,212] INFO [https_20190709.test_case.test_process_01:104] {'值机信息': {'idNo': '450125196506047580', 'sex': 2, 'lk_flight': '9D5671', 'lk_gateno': '19', 'lk_date': '20200529', 'lk_chkt': '20200529105244', 'lk_inf': '', 'lk_outtime': '20200529135244', 'lk_cname': '二师兄017', 'lk_ename': 'DAXIGUA7', 'lk_seat': '017A', 'lk_desk': 'CTU', 'lk_bdno': '017'}}\n"
    t2 = (t1.split("值机信息")[1][2:-2].replace("'","\""))
    import json
    tj = json.loads(t2)
    print(tj)