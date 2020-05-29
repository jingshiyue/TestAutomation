# -*- coding:utf-8 -*- 
# Time : 2020/4/28 09:49
# Author : zcl

"""
用于测试流程: 安检(系统)->复核(系统)->登机口复核(系统)
"""

import pytest,os,sys
sys.path.extend([sys.path[0] + r"\..\..",sys.path[0] + r"\..\..\..",sys.path[0] + r"\.."])
import threading
import xlwt
from https_20190709.common.Autosendlk import *
from https_20190709.API_https.AirportProcess import AirportProcess
from https_20190709.common.common_method import *
import json,time
import logging
logger = logging.getLogger(__name__)
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestAutomation.settings')
django.setup()
from django.conf import settings
from conftest import get_useful_flight,read_from_config,write_to_config
from data import flightInfo
from process_test.https_20190709.test_case.data import *  #{'flight_no': 'DR6562', 'bdno': '02', 'date': '2020-05-09'}
from myAssert import assert_parm


def assert_backQuery_byId(**kwargs):
    from https_20190709.API_https.AirportProcess import AirportProcess
    from process_test.https_20190709.common.common_method import to_base64
    """ 按身份证回查 """
    res = AirportProcess().api_face_data_flowback_query(
        reqId=get_uuid(),
        cardId=kwargs["idNo"],
        flightDay=kwargs["lk_date"],
        isFuzzyQuery=0,
        seatId="0INF"
    )
    return res.text

def assert_backQuery_byTicket(**kwargs):
    from https_20190709.API_https.AirportProcess import AirportProcess
    from process_test.https_20190709.common.common_method import to_base64
    """ 按票回查"""
    res = AirportProcess().api_face_data_flowback_query(
        reqId=get_uuid(),
        # cardId="142724198605103941",
        flightNo=kwargs["lk_flight"],
        boardingNumber=kwargs["lk_bdno"],
        flightDay=kwargs["lk_date"],  # 航班dd
        isFuzzyQuery=0,
        seatId="0INF"
    )
    return res.text
    
def assert_backQuery(**kwargs):
    from https_20190709.API_https.AirportProcess import AirportProcess
    from process_test.https_20190709.common.common_method import to_base64
    """ 按身份证回查  2、按票回查"""
    res = AirportProcess().api_face_data_flowback_query(
        reqId=get_uuid(),
        # cardId=zhiji_dic["idNo"],
        cardId=kwargs["idNo"],
        # flightDay=zhiji_dic["lk_date"][-2:],  # 航班dd
        flightDay=kwargs["lk_date"],
        isFuzzyQuery=0,
        # seatId="0INF"
    )
    return res.text

    # res = AirportProcess().api_face_data_flowback_query(
    #     reqId=get_uuid(),
    #     # cardId="142724198605103941",
    #     flightNo=zhiji_dic["lk_flight"],
    #     boardingNumber=zhiji_dic["lk_bdno"],
    #     flightDay=zhiji_dic["lk_date"][-2:],  # 航班dd
    #     isFuzzyQuery=0,
    #     # seatId="0INF"
    # )
    # logger.info({"票回查":res.text})


def setup_function():
    # flight = get_useful_flight(config.get("config","gateNoList").split(","))
    flight = get_useful_flight(read_from_config(r"process_test\https_20190709\test_case\pytest.ini","config","gateNoList").split(","))
    flightInfo["flight_no"] = str(flight[2])[2:-1]
    flightInfo["bdno"] = str(flight[3])[2:-1]
    flightInfo["date"] = str(flight[0])[2:-1]
    data_ini = read_from_config(r"process_test\https_20190709\test_case\pytest.ini","config","data")
    flight_ini = read_from_config(r"process_test\https_20190709\test_case\pytest.ini","config","flight")
    if flightInfo["date"] not in data_ini:
        write_to_config(r"process_test\https_20190709\test_case\pytest.ini","config","data",flightInfo["date"])
        write_to_config(r"process_test\https_20190709\test_case\pytest.ini","config","idx_feature","699")
        write_to_config(r"process_test\https_20190709\test_case\pytest.ini","config","lk_bdno","000")
    if flightInfo["flight_no"] not in flight_ini:
        write_to_config(r"process_test\https_20190709\test_case\pytest.ini","config","flight",flightInfo["flight_no"])
        write_to_config(r"process_test\https_20190709\test_case\pytest.ini","config","lk_bdno","000")

    res = AirportProcess().api_face_boarding_start(
        flightNo=flightInfo["flight_no"],
        boardingGate=flightInfo["bdno"],
        deviceCode="T1ZZ002",
        gateNo="01",
        flightDay=flightInfo["date"]
    )
    logger.info({"开始登机[res.text]":res.text})
    assert_parm(res.text,status=0)
    assert_parm(res.text,msg="Success")
    logger.info({"[正在登机]航班":flightInfo}) #{'flight_no': '9D5671', 'bdno': '19', 'date': '2020-05-26'}
    
def teardown_function():
    # logger.info({"teardown":"-------"})
    flightInfo = {}


"""
"lk_gateno":"10" ,    登机口
"lk_flight": "CA1645",  航班号
"lk_bdno":"001",  登机序号
"""
# @pytest.mark.repeat(2)
# @pytest.mark.skip(reason="根据登机口自动查找到航班(起飞时间间隔>1h )A-> B-> 复核(分为自助和人工两种)-> 发送开始登机-> 登机复核")
@pytest.mark.parametrize("creat_zhiji_byFlight", [{"lk_cname":"二师兄"}],indirect=True)
def test_01(creat_zhiji_byFlight,struct_pho):    #{'flight_no': 'CA8295', 'bdno': '02', 'date': '2020-05-09'}
    """
    fixture parameters.
    """
    zhiji_dic = creat_zhiji_byFlight
    pho_dic = struct_pho
    logger.info({"值机信息":zhiji_dic})

    ############################################################################
    """2.3.20自助验证闸机A门接口（二期）"""
    res = AirportProcess().api_security_ticket_check(
        reqId=get_uuid(),  # 必填
        gateNo="T1AJ1",  # 必填,A B门T1AJ1，复核对应T1AF1
        deviceId="T1AJ001",  # 必填
        cardType=0,  # 必填
        idCard=zhiji_dic["idNo"],  # 必填
        nameZh=zhiji_dic["lk_cname"],
        nameEn=zhiji_dic["lk_ename"],
        age=get_age(zhiji_dic["idNo"]),
        sex=zhiji_dic["sex"],
        birthDate=get_birthday(zhiji_dic["idNo"]),  # 必填
        address="重庆市",
        certificateValidity="20120101-20230202",  # 必填
        nationality="CHina",
        ethnic="汉族",
        contactWay="13512134390",
        cardPhoto=pho_dic["cardPhoto"],  # 必填
        fId=get_uuid()  # 必填
    )
    logger.info({"A门[res.text]":res.text})
    assert_parm(res.text,result=0)


    """2.3.21自助验证闸机B门接口（二期）"""
    res = AirportProcess().api_face_security_face_check(
        reqId=get_uuid(),  # 必填
        gateNo="T1AJ1",  # 必填
        deviceId="T1AJ001",  # 必填
        cardType=0,  # 必填
        idCard=zhiji_dic["idNo"],  # 必填
        nameZh=zhiji_dic["lk_cname"],
        nameEn=zhiji_dic["lk_ename"],
        age=get_age(zhiji_dic["idNo"]),
        sex=zhiji_dic["sex"],
        birthDate=get_birthday(zhiji_dic["idNo"]),  # 必填
        address="重庆市",
        certificateValidity="20180101-20260203",  # 必填
        nationality="China",  # 必填
        ethnic="汉族",  # 必填
        contactWay="13512134390",
        scenePhoto=pho_dic["scenePhoto"],  # 必填
        sceneFeature=pho_dic["sceneFeature"],  # 必填
        cardPhoto=pho_dic["cardPhoto"],  # 必填
        cardFeature=pho_dic["cardFeature"],  # 必填
        largePhoto=pho_dic["largePhoto"]  # 必填
    )
    logger.info({"B门[res.text]":res.text})
    assert_parm(res.text,result=0)
    # logger.info({"第一次安检时间:":time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())})
    time.sleep(3)
    ############################################################################
    """2.3.22	自助闸机复核接口（二期）  [1:N]"""
    res = AirportProcess().api_face_review_self_check(
        reqid=get_uuid(),  # 必填
        gateno = "T1AF1",  # 必填 对应T1AJ1
        deviceid = "T1AJ002",  # 必填
        scenephoto = pho_dic["scenePhoto_fuhe"],  # 必填,可以不用2K
        scenefeature = pho_dic["sceneFeature_2k"]  # 必填,需要2K文件夹里
    )
    assert_parm(res.text,result=0)
    result = json.loads(res.text)
    del result['userInfo']['basePhoto']
    logger.info({"系统复核[res.text]":result})

    # """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    # res = AirportProcess().api_face_review_manual_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF002",
    #     scenePhoto=pho_dic["scenePhoto"],
    #     cardNo=zhiji_dic["idNo"],
    #     passengerName=zhiji_dic["lk_cname"],
    #     passengerEnglishName=zhiji_dic["lk_ename"],
    #     securityStatus=2,  # 安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
    #     securityPassTime=zhiji_dic["lk_chkt"],
    #     securityGateNo="",
    #     securityDeviceNo="",
    #     flightNo=zhiji_dic["lk_flight"],
    #     boardingNumber=zhiji_dic["lk_bdno"],
    #     sourceType=0,
    #     flightDay=zhiji_dic["lk_date"])
    # logger.info({"人工复核":res.text})
    ############################################################################
    time.sleep(60*1)
    """2.3.11登机口复核接口（二期优化）"""
    res = AirportProcess().api_face_boarding_review_check(
        faceImage=pho_dic["scenePhoto_fuhe_dengji"],
        faceFeature=pho_dic["sceneFeature_2k"],
        deviceCode="T1DJ001",
        boardingGate=zhiji_dic["lk_gateno"],
        flightNo=zhiji_dic["lk_flight"],
        flightDay=zhiji_dic["lk_date"],  # （yyyyMMdd）
        gateNo=zhiji_dic["lk_gateno"],
    )
    logger.info({"登机口系统复核[res.text]":res.text})
    assert_parm(res.text,result=0)

    #############################################################################
    # D:\workfile\zhongkeyuan_workspace\TestAutomation\process_test\https_20190709\common\common_method.py
    from process_test.https_20190709.common.common_method import to_base64
    """ 1、按身份证回查  2、按票回查"""
    res = assert_backQuery_byId(idNo=zhiji_dic["idNo"],lk_date=zhiji_dic["lk_date"][-2:])

    # res = AirportProcess().api_face_data_flowback_query(
    #     reqId=get_uuid(),
    #     cardId=zhiji_dic["idNo"],
    #     flightDay=zhiji_dic["lk_date"][-2:],  # 航班dd
    #     isFuzzyQuery=0,
    #     # seatId="0INF"
    # )
    # logger.info({"身份证回查":res.text})


    # res = AirportProcess().api_face_data_flowback_query(
    #     reqId=get_uuid(),
    #     # cardId="142724198605103941",
    #     flightNo=zhiji_dic["lk_flight"],
    #     boardingNumber=zhiji_dic["lk_bdno"],
    #     flightDay=zhiji_dic["lk_date"][-2:],  # 航班dd
    #     isFuzzyQuery=0,
    #     # seatId="0INF"
    # )
    # logger.info({"票回查":res.text})


if __name__ == '__main__':
    """
    --capture=sys : 捕获print，将print写入到html里;
    logging和--capture=no实现运行测试用例的实时输出所有的log信息;
    """
    filePath = os.path.realpath(__file__).split("TestAutomation")[1][1:].replace("\\","\\\\")
    pytest.main([
                r"process_test\https_20190709\test_case\test_process_01.py",
                "-v","-s",
                # '--count=6',    #重复执行用例次数
                "--log-cli-level=INFO",     #能将日志写进html报告里
                "--log-cli-date-format=%Y-%m-%d %H:%M:%S",
                "--log-cli-format=[%(asctime)s %(filename)s line:%(lineno)d]%(levelname)s:  %(message)s",
                "--self-contained-html","--html=./report/report.html",
    ])
