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

from django.core.mail import send_mail

def send_email(product_name:str, urlStr:str):
    notifiers = Product.objects.all().get(name=product_name).notifier.all()
    to_email = []
    for notifier in notifiers:
        to_email.append(notifier.email)

    subject = '自动化测试平台'
    message = ''
    sender = settings.EMAIL_FROM
    receiver = to_email
    html_message = """<h1>%s, 自动化测试平台</h1>
    自动化测试平台<br/><a href="http://fresh.skychar.cn/user/active/">%s</a>""" % (urlStr, urlStr)
    send_mail(subject, message, sender, receiver, html_message=html_message)


head = """
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
"""

content = """
class Testcase_%s(object):
    def setup_method(self, method):
        super().__init__()
        self.pattern = re.compile(r'^\${(.+(\(.*\)))}', re.I)
        self.certificate = None
        self.obj = TestCase.objects.all().get(casename="%s")
        self.caseDict = model_to_dict(self.obj)
        self.url = self.generate_url()
        self.method = self.caseDict.get("method")
        self.header = self.generate_header()
        self.body = self.generate_body()
        logger.info("setup_method...")


    def teardown_method(self, method):
        logger.info("teardown_method...")

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
                        parmsStr = parmsStr.replace("'","\\"")
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
"""
foot = """


if __name__=="__main__":
    pytest.main(["-vv", "-s", "runCase.py", "--color=no", "--alluredir=./report/xml"])
"""

if __name__=="__main__":
    product = "动态布控"
    modular = "数据平台"
    cases = TestCase.objects.all().filter(product_name__name=product,modular_name__name=modular)
    f = open("runCase.py","w",encoding='utf-8')
    f.write(head)
    for case in cases:
        f.write(content %(case.casename.replace("-","_"),case.casename))
    f.write(foot)
    f.close()
    os.system("runCase.py")
    # send_email(product, "hello spring")