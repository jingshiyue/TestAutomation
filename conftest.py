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
import os,django,sys
import logging
logger = logging.getLogger(__name__)

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
        config._metadata["Platform"] = "Windows Server 2008 Enterprise"
        config._metadata["项目名称"] = read_from_config("testcase.ini","Product","name")
    except Exception as e:
        logger.info(e)
    config._metadata.pop("JAVA_HOME")
    config._metadata.pop("Plugins")

# Windows Server 2008 R2 企业版

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Test Data'))
    cells.pop(-1)

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.pop(-1)

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)