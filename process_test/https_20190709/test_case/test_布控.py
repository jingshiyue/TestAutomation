#!/usr/bin/python3
# Time : 2019/12/20 14:56 
# Author : zcl
import pytest,random,os,sys,pymysql
from https_20190709.common.common_method import *
from BaiTaAirport2_month.common import Idcardnumber
from https_20190709.API_https.BlackList import BlackListApi
from BaiTaAirport2_month.msgQueue import Autosendlk
from BaiTaAirport2_month.common.mysql_class import *


def printRes(res):
    logging.info("------------------------------------------------")
    logging.info(res)
    logging.info("------------------------------------------------")

blackListApi = BlackListApi()

# @pytest.mark.skip(reason="黑名单新增/更新")
def test_01():
    logging.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    res = blackListApi.api_black_list_save(  # 姓名、身份证号、布控类别
        certificateNumber="500335195507025050",
        peopleName="黑名单01",  # 必须
        focusType=0,  # 必须int 0：布控人员  1：失信人员  2：重点检查人员  3：本场关注人员  4：嫌疑人  5：上访人员  6：其他人员
    )
    printRes(res)
    logging.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)

if __name__ == '__main__':
    pytest.main(["-s", "test_布控.py"])