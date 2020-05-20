import pytest
import os
import sys
sys.path.append(r"D:\workfile\zhongkeyuan_workspace\TestAutomation\process_test")

import threading
import xlwt
from BaiTaAirport2_month.msgQueue.Autosendlk import *
from https_20190709.API_https.AirportProcess import AirportProcess
from https_20190709.common.common_method import *
import json
import logging

# @pytest.mark.skip(reason="经停(刷票) ->买票过安检1:1")
def test_03(struct_pho):    #{'flight_no': 'CA8295', 'bdno': '02', 'date': '2020-05-09'}
    pho_dic = struct_pho
    from .conftest import creat_zhiji_byFlight_useInFunc
    lk_flight_before = "CA8888"    #中转、备降、经停 航班
    lk_flight = "CA8128"     #重新买票值机的航班
    lk_gateno = "10"  #登机口 
    lk_bdno = "03"  #登机序号
    res = AirportProcess().api_face_transfergate_face_collect(   #分为刷票 刷证，二选一
        reqId=get_uuid(),
        flightNo=lk_flight_before, # 刷票
        faceImage=pho_dic["scenePhoto"],
        faceFeature=pho_dic["sceneFeature"],
        deviceCode="T1ZZ002",
        gateNo=lk_gateno, # 刷票
        seatId=lk_bdno+"A", # 刷票
        startPort="HET",
        boardingNumber=lk_bdno,  #
        flightDay="11",   # 传Dd
        sourceType=1,    #0,中转；1，经停；2、备降采集；3、中转人工放行；4、经停人工放行；5、备降人工放行 6、经停证件采集（废弃）
        endPort="",
        cardId="",       #非必须  sourceType为6-经停证采集必给
        nameZh="",       #非必须  sourceType 为6-经停证采集必给
        mainFlightNo="", #非必须  主航班
        cardPhoto="",    #非必须  身份证件照base64编码
        cardFeature="",  #非必须  证件照特征base64
        largePhoto="",   #非必须  大图（口罩检测用）
        facePst=""       #非必须  人脸坐标（口罩检测用）
    )
    logging.info({"中转通道：刷票: ":res.text})
    time.sleep(20)
    zhiji_dic_testDate = {
        "lk_flight":lk_flight,  #航班号
        "lk_gateno":lk_gateno,  #登机口        
        "lk_bdno":lk_bdno,   #登机序号
    }
    zhiji_dic = creat_zhiji_byFlight_useInFunc(request=zhiji_dic_testDate)
    logging.info({"值机信息: ":zhiji_dic})
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
    logging.info({"A门:":res.text})


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
    logging.info({"B门: ":res.text})
    ############################################################################
    logging.info("test_03测试完成")

if __name__ == '__main__':
    pytest.main([
                 r"process_test\https_20190709\test_case\test_process.py",
                 "-v","-s",
                 "--log-cli-level=INFO",
                 ])