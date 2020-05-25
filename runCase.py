
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


class Testcase_系统安检通过_系统复核通过_系统登机口复核通过(object):
    def test_run(self):
        '''
        【系统安检】:A门传入身份证+证件照，B门传入身份证+现场照A、现场照特征A+证件照、证件照特征
【系统复核】:传入现场照B、现场特征B
【系统登机口复核】:传入[身份证号]+机票
        '''
        logger.info("测试开始 ...")
        import subprocess
        s=subprocess.Popen(['python', r'process_test\https_20190709\test_case\test_process_01.py'],bufsize=0,stdout=subprocess.PIPE,universal_newlines=True)   
        FAILED = False
        try:
            while True:
                nextline=s.stdout.readline()
                logger.info(nextline.strip())
                if "AssertionError" in nextline or "FileNotFoundError" in nextline:
                    FAILED = True
                    break
                if nextline=="" and scan.poll()!=None:
                    logger.info("测试完成  ...")
                    break
        except:
            pass
        if FAILED:
            logger.info("测试失败  ...")
            assert 0
        logger.info("测试完成  ...")



if __name__=="__main__":
    pytest.main([
        "runCase.py",
        "-v","-s","--reruns=0","--color=yes","--self-contained-html","--html=./report/report_20200525142819.html",
        ])
