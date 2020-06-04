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
from django.core.mail import send_mail
from conftest import read_from_config


caseNameList = read_from_config("testbed.ini","TestCase","name").split(",")

testCaseInputData = {}

"""

tasklist
	1、登陆，主页修改
	2、邮件内容修改  done
	3、报告表格内容修改  done
	4、后台加校验  done
		1、单接口 需要哪些必填 ，字段格式要求
		2、流程 需要哪些必填
	5、获取svn版本 
	6、输入参数加入到报告列表里 done
    7、增加 用例添加界面，后台数据太多，编辑起来不方便 appending

"""

def send_email(que,product_name:str,timeStr:str):
    if "COMPLATE" in que.get():
        notifiers = Product.objects.all().get(name=product_name).notifier.all()
        to_email = []
        for notifier in notifiers:
            to_email.append(notifier.email)

        subject = product_name + "测试报告"
        message = ''
        sender = settings.EMAIL_FROM
        receiver = to_email
        filePath = "report/report_"+timeStr+".html"
        url = read_from_config("testbed.ini","Url","host") + ":" + \
              read_from_config("testbed.ini","Url","port")
        html_message = generate_mail_html_content(filePath,product_name+"测试报告",url+"/"+filePath)
        if html_message:
            send_mail(subject, message, sender, receiver, html_message=html_message)
            logger.info("发送邮件成功 ...")
        exit()

def find_str_idx(content:str,keyword:str):
    """
    查找字符串，返回字符串索引位置
    """
    index = content.find(keyword)
    return index

def generate_mail_html_content(file:str,title:str,reportHtmlPath:str):
    content = ""
    newContent = ""
    try:
        with open(file,mode='r',encoding='UTF-8') as f:
            content = f.read()
    except:
        return None
    newContent = content[:find_str_idx(content,"<h1>")] + "<h1>" + title + "</h1>" + \
                content[find_str_idx(content,"</h1>") + 
                len("</h1>"):find_str_idx(content,"<h2>Results</h2>")] + "<h2>Results</h2>" + \
                '<span style="color:coral;font-size:16px;">报告详情: <a href="{0}" target="_blank">{0}</a></span></body></html>'.format("http://"+reportHtmlPath)
    return newContent

head = """
import os,django,sys
from utils.inner import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestAutomation.settings')
django.setup()
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
import requests
import traceback
from product_manage.models import Product,Notifier,Modular
from testcase_manage.models import TestCase
from django.forms.models import model_to_dict
import time
import json
import re
import pytest
from startRun import testCaseInputData 
"""

content_danjiekou = """
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
        self.checkList = self.generate_checkList()
        logger.info(self.__class__.__name__)

    def teardown_method(self, method):
        logger.info("teardown_method...")


    def generate_url(self):
        host = self.obj.modular_name.host
        api = self.caseDict.get('api')
        return host + api

    def generate_header(self):
        return get_headers(self.caseDict.get('api'))
        
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

    def generate_checkList(self):
        checkList = self.obj.check_list
        checkList = json.loads(checkList) #{'status': 0, 'msg': 'Success'}
        return checkList

    def test_run(self):
        '''
        %s
        '''
        logger.info("测试开始 ...") 
        if self.caseDict.get("case_type") == '单接口':
            testCaseInputData.setdefault(self.__class__.__name__[9:],self.body)
            if self.method == 'POST':
                # logger.info(self.url)
                res = requests.post(url=self.url,
                                    headers=self.header,
                                    json=self.body,
                                    verify=self.certificate
                                    )
                res.close()
                logger.info("url: {}".format(self.url))
                logger.info("请求参数: {}".format(self.body))
                logger.info("响应: {}".format(res.text))
                self.result = json.loads(res.text)
                for k,v in self.checkList.items():
                    if isinstance(v, int):
                        assert self.result[k] == v,"结果校验不通过"
                    if isinstance(v, str):
                        matchObj = re.search(v,self.result[k],re.I)
                        assert matchObj,"结果校验不通过"
                logger.info("测试完成 ...")
                return res
            if self.method == 'GET':
                logger.info("GET 单接口暂没有！")
                return None
        else:
            pass
"""

content_liucheng = """

class Testcase_{0}(object):
    def test_run(self):
        '''
        {2}
        '''
        logger.info("测试开始 ...")
        import subprocess
        s=subprocess.Popen(['python', r'process_test\{1}'],bufsize=0,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) 
        inputData = ""  #流程的输入数据
        FAILED = False
        try:
            while True:
                nextline_err = s.stderr.readline()
                if nextline_err.strip():
                    logger.info(nextline_err.strip())

                nextline=s.stdout.readline()
                # logger.info(nextline.strip())
                if "值机信息" in nextline_err:  #从日志中提取输入数据，便于后期放进report
                    inputData = nextline_err.split("值机信息")[1][2:-2]
                if "输入数据" in nextline_err:  #从日志中提取输入数据，便于后期放进report
                    inputData = nextline_err.split("输入数据")[1][2:-2]
                if "AssertionError" in nextline_err or "Errno" in nextline_err or "Error" in nextline_err:
                    FAILED = True
                    break
                if "AssertionError" in nextline or "Errno" in nextline or "Error" in nextline:
                    FAILED = True
                    break
                if "Aborting transport connection" in nextline:
                    break
                if nextline=="" and scan.poll()!=None:
                    logger.info("测试完成  ...")
                    break
        except:
            pass
        testCaseInputData.setdefault(self.__class__.__name__[9:],inputData)
        if FAILED:
            raise Exception('测试失败 ...')
        logger.info("测试完成  ...")
"""

foot = """


if __name__=="__main__":
    pytest.main([
        "runCase.py",
        "-v","-s","--reruns=0","--color=yes","--self-contained-html","--html=./report/report_{0}.html",
        ])
"""

if __name__=="__main__":
    # file = r"D:\workfile\zhongkeyuan_workspace\TestAutomation\logs\youjian.txt"
    # content = ""
    # newContent = ""
    # with open(file,mode='r',encoding='UTF-8') as f:
    #     content = f.read()
    # newContent = content[:find_str_idx(content,"<h1>")] + "<h1>动态布控测试报告</h1>" + \
    #             content[find_str_idx(content,"</h1>") + 
    #             len("</h1>"):find_str_idx(content,"<h2>Results</h2>")] + "<h2>Results</h2>" + \
    #             '<h3>报告详情: <a href="http://192.168.1.42:8000/report/report_20200527124022.html" style="color:coral;">http://192.168.1.42:8000/report/report_20200527124022.html</a></h3>' + \
    #             "</body></html>"
    # logger.info(newContent)
    reportHtmlPath = "http://192.168.1.99:8000/report/report_20200527124022.html"
    con = '<span style="color:coral;font-size:16px;">报告详情: <a href="{0}" target="_blank">{0}</a></span></body></html>'.format(reportHtmlPath)
    print(con)
