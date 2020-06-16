
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


class Testcase_系统安检_系统复核_人脸复核登机(object):
    def test_run(self):
        '''
        <p>【系统安检】:A门传入身份证+证件照，B门传入身份证+安检现场照、现场照特征A+证件照、证件照特征</p>
<p>【系统复核】:传入复核现场照、现场特征B</p>
<p>【系统登机口复核】:传入登机口复核现场照、现场特征B</p>
        '''
        logger.info("测试开始 ...")
        import subprocess
        s=subprocess.Popen(['python', r'process_test\https_20190709\test_case\test_process_01.py'],bufsize=0,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) 
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


class Testcase_系统安检_系统复核_刷票快速登机(object):
    def test_run(self):
        '''
        <p>【系统安检】:A门传入身份证+证件照，B门传入身份证+现场照A、现场照特征A+证件照、证件照特征</p>
<p>【系统复核】:传入现场照B、现场特征B</p>
<p>【系统登机口复核】:传入机票</p>
        '''
        logger.info("测试开始 ...")
        import subprocess
        s=subprocess.Popen(['python', r'process_test\https_20190709\test_case\test_process_03.py'],bufsize=0,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) 
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

class Testcase_人员回查接口(object):
    def setup_method(self, method):
        super().__init__()
        self.pattern = re.compile(r'^\${(.+(\(.*\)))}', re.I)
        self.certificate = None
        self.obj = TestCase.objects.all().get(casename="人员回查接口")
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
                        parmsStr = parmsStr.replace("'","\"")
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
        2.3.24	人员回查-安检、登机口接口（二期）
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


class Testcase_系统安检_系统复核_刷证快速登机(object):
    def test_run(self):
        '''
        <p>【系统安检】:A门传入身份证+证件照，B门传入身份证+安检现场照、现场照特征A+证件照、证件照特征 </p>
<p>【系统复核】:传入复核现场照、现场特征B </p>
<p>【系统登机口复核】:传入身份证</p>
        '''
        logger.info("测试开始 ...")
        import subprocess
        s=subprocess.Popen(['python', r'process_test\https_20190709\test_case\test_process_02.py'],bufsize=0,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) 
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


class Testcase_系统安检_系统复核_登机口人工放行(object):
    def test_run(self):
        '''
        <p>【系统安检】:A门传入身份证+证件照，B门传入身份证+安检现场照、安检现场照特征+证件照、证件照特征 </p>
<p>【系统复核】:传入复核现场照、复核现场特征 </p>
<p>【登机口人工放行】:传入登机口现场照+身份证</p>
        '''
        logger.info("测试开始 ...")
        import subprocess
        s=subprocess.Popen(['python', r'process_test\https_20190709\test_case\test_process_04.py'],bufsize=0,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True) 
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



if __name__=="__main__":
    pytest.main([
        "runCase.py",
        "-v","-s","--reruns=0","--color=yes","--self-contained-html","--html=./report/report_20200616113307.html",
        ])
