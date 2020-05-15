#!/usr/bin/python3
# Time : 2019/10/15 15:33 
# Author : zcl
# import pytest,random,os,sys
# from https_20190709.API_https.AirportProcess import *
# import os
# import logging

import pytest,random,os,sys,pymysql
from https_20190709.common.common_method import *
from BaiTaAirport2_month.common import Idcardnumber
from https_20190709.API_https.AirportProcess import *
from BaiTaAirport2_month.msgQueue import Autosendlk
from BaiTaAirport2_month.common.mysql_class import *


def printRes(res):
    logging.info("------------------------------------------------")
    logging.info(res.text)
    logging.info("------------------------------------------------")



@pytest.mark.skip(reason="仅安检值机")
@pytest.mark.parametrize("insert_data_into_mysql", [{"bdno":"10","date":"20191023","flight_no":"3U8747"}], indirect=True)
@pytest.mark.parametrize("creat_zhiji_random", [{"lk_bdno": "10","lk_date":"20191023","lk_flight": "3U8747"}],indirect=True)
def test_anjian_and_zhiji(insert_data_into_mysql,creat_zhiji_random):
    logging.info("安检+值机完成")


# @pytest.mark.skip(reason="先值机，然后A门前刷身份证,当前时间若已经超过飞机起飞时间，则判定为该旅客已误机")
@pytest.mark.parametrize("insert_data_into_mysql", [{"bdno": "09", "date": "20191023", "flight_no": "CA1553"}],indirect=True)
@pytest.mark.parametrize("creat_zhiji_random", [{"lk_bdno": "09", "lk_date": "20191023", "lk_flight": "CA1553"}],indirect=True)
def test_01(insert_data_into_mysql,creat_zhiji_random,struct_pho):
    logging.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logging.info("测试的身份证号码:%s" % zhiji_dic["idNo"])
    """2.3.20自助验证闸机A门接口（二期）"""
    res = AirportProcess().api_security_ticket_check(
        reqId=get_uuid(),  # 必填
        gateNo="T1AJ1",  # 必填,A B门T1AJ1，复核对应T1AF1
        deviceId="T1AJ001",  # 必填
        cardType="0",  # 必填
        idCard=zhiji_dic["idNo"],  # 必填
        nameZh="大西瓜",
        nameEn="XIGUA",
        age=get_age(zhiji_dic["idNo"]),
        sex=1,
        birthDate=get_birthday(zhiji_dic["idNo"]),  # 必填
        address="重庆市",
        certificateValidity="20120101-20230202",  # 必填
        nationality="CHina",
        ethnic="汉族",
        contactWay="13512134390",
        cardPhoto=pho_dic["cardPhoto"],  # 必填
        fId=get_uuid()  # 必填
    )
    printRes(res.text)
    logging.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)



# @pytest.mark.skip(reason="在人工通道刷身份证的同时，当前时间若已经超过飞机起飞时间,则判定为该旅客已误机。")
@pytest.mark.parametrize("insert_data_into_mysql", [{"bdno": "09", "date": "20191023", "flight_no": "CA1553"}],indirect=True)
@pytest.mark.parametrize("creat_zhiji_random", [{"lk_bdno": "09", "date": "20191023", "lk_flight": "CA1553"}],indirect=True)
def test_02(insert_data_into_mysql,creat_zhiji_random,struct_pho):
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
    res = AirportProcess().api_face_security_manual_check(
                                reqId=get_uuid(),
                                flightNo=zhiji_dic["lk_flight"],
                                faceImage=pho_dic["scenePhoto"],
                                gateNo="T1AJ1",
                                deviceCode="T1AJ002",
                                boardingNumber=zhiji_dic["lk_bdno"],
                                seatId=zhiji_dic["lk_bdno"],
                                startPort="HET",
                                flightDay=zhiji_dic["lk_date"][-2:],
                                faceFeature=pho_dic["sceneFeature"],
                                kindType=0,  # 类型：0：刷票 1：刷票放行
                                largePhoto=pho_dic["largePhoto"])
    printRes(res.text)
    logging.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)


# @pytest.mark.skip(reason="A-> B-> 复核(分为自助和人工两种)-> 发送开始登机-> 登机复核")
@pytest.mark.parametrize("creat_zhiji_random", [{"lk_gateno":"05" ,"lk_flight": "AQ1096"}],indirect=True)
def test_03(creat_zhiji_random,struct_pho): #02表示第二行
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logging.info("测试的身份证号码:%s" %zhiji_dic["idNo"])
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
    logging.info(res.text)

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
    logging.info(res.text)
    time.sleep(5)

    """2.3.22	自助闸机复核接口（二期）  [1:N]"""
    res = AirportProcess().api_face_review_self_check(
        reqid=get_uuid(),  # 必填
        gateno = "T1AF1",  # 必填 对应T1AJ1
        deviceid = "T1AJ002",  # 必填
        scenephoto = pho_dic["scenePhoto_fuhe"],  # 必填,可以不用2K
        scenefeature = pho_dic["sceneFeature_2k"])  # 必填,需要2K文件夹里
    logging.info(res.text)
    time.sleep(8)
    # """2.3.22	自助闸机复核接口（二期）  [1:N]"""
    # res = AirportProcess().api_face_review_self_check(
    #     reqid=get_uuid(),  # 必填
    #     gateno = "T1AF1",  # 必填 对应T1AJ1
    #     deviceid = "T1AJ002",  # 必填
    #     scenephoto = pho_dic["scenePhoto_fuhe"],  # 必填,可以不用2K
    #     scenefeature = pho_dic["sceneFeature_2k"])  # 必填,需要2K文件夹里
    # logging.info(res.text)

    time.sleep(60)
    """2.3.11登机口复核接口（二期优化）"""
    res = AirportProcess().api_face_boarding_review_check(
                                                            faceImage=pho_dic["scenePhoto_fuhe"],
                                                            faceFeature=pho_dic["sceneFeature_2k"],
                                                            deviceCode="T1DJ001",
                                                            boardingGate=zhiji_dic["lk_gateno"],
                                                            flightNo=zhiji_dic["lk_flight"],
                                                            flightDay=zhiji_dic["lk_date"],  # （yyyyMMdd）
                                                            gateNo=zhiji_dic["lk_gateno"],
                                                            )
    logging.info(res.text)



    # """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    # res = AirportProcess().api_face_review_manual_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF002",
    #     scenePhoto=pho_dic["scenePhoto"],
    #     cardNo=zhiji_dic["idNo"],
    #     passengerName="大西瓜",
    #     passengerEnglishName="XIGUA",
    #     securityStatus=2,  # 安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
    #     securityPassTime=zhiji_dic["lk_chkt"],
    #     securityGateNo="",
    #     securityDeviceNo="",
    #     flightNo=zhiji_dic["lk_flight"],
    #     boardingNumber=zhiji_dic["lk_bdno"],
    #     sourceType=0,
    #     flightDay=zhiji_dic["lk_date"])
    # logging.info(res.text)
    logging.info("test_03测试完成")


# @pytest.mark.skip(reason="人工通道： 刷票-> 1:1安检-> 复核(分为自助和人工两种)")
@pytest.mark.parametrize("insert_data_into_mysql", [{"bdno": "10","flight_no": "3U8747"}],indirect=True)
@pytest.mark.parametrize("creat_zhiji_random", [{"lk_bdno": "10","lk_flight": "3U8747"}],indirect=True)
def test_04(insert_data_into_mysql,creat_zhiji_random,struct_pho):
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logging.info("测试的身份证号码:%s" %zhiji_dic["idNo"])
    another_pho = to_base64(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\1.jpg")

    """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
    res = AirportProcess().api_face_security_manual_check(
                                reqId=get_uuid(),
                                flightNo=zhiji_dic["lk_flight"],
                                faceImage=pho_dic["scenePhoto"],
                                gateNo="T1AJ1",
                                deviceCode="T1AJ002",
                                boardingNumber=zhiji_dic["lk_bdno"],
                                seatId=zhiji_dic["lk_bdno"],
                                startPort="HET",
                                flightDay=zhiji_dic["lk_date"],
                                faceFeature=pho_dic["sceneFeature"],
                                kindType=1,  # 类型：0：刷票 1：刷票放行
                                largePhoto=pho_dic["largePhoto"])
    logging.debug(res.text)
    """安检1:1"""
    res = AirportProcess().api_anjian(
        anjiangateNo="T1AJ1",
        anjiandeviceId="T1AJ001",
        cardType=0,
        idCard=zhiji_dic["idNo"],
        nameZh="大西瓜",
        nameEn="XIGUA",
        age=get_age(zhiji_dic["idNo"]),
        sex=zhiji_dic["sex"],
        birthDate=get_birthday(zhiji_dic["idNo"]),
        address="重庆市大竹林街道",
        nationality="中国",
        ethnic="汉族",
        scenePhoto=pho_dic["scenePhoto"],
        sceneFeature=pho_dic["sceneFeature"],
        cardPhoto=pho_dic["cardPhoto"],
        cardFeature=pho_dic["cardFeature"],
        largePhoto=pho_dic["largePhoto"]
    )
    logging.debug(res.text)

    time.sleep(5)
    # """2.3.22	自助闸机复核接口（二期）  [1:N]"""
    # res = AirportProcess().api_face_review_self_check(
    #     reqid=get_uuid(),  # 必填
    #     gateno = "T1AF1",  # 必填 对应T1AJ1
    #     deviceid = "T1AJ002",  # 必填
    #     scenephoto = pho_dic["scenePhoto"],  # 必填,可以不用2K
    #     scenefeature = pho_dic["sceneFeature_2k"])  # 必填,需要2K文件夹里
    # logging.info(res.text)

    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF002",
        scenePhoto=pho_dic["scenePhoto"],
        cardNo=zhiji_dic["idNo"],
        passengerName="大西瓜",
        passengerEnglishName="XIGUA",
        securityStatus=0,  # 安检的状态(0人证1:1,  1 人工放行,  2闸机B门通过,3-未知)
        securityPassTime=zhiji_dic["lk_chkt"],
        securityGateNo="",
        securityDeviceNo="",
        flightNo=zhiji_dic["lk_flight"],
        boardingNumber=zhiji_dic["lk_bdno"],
        sourceType=0,
        flightDay=zhiji_dic["lk_date"])
    logging.info(res.text)
    logging.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)



# @pytest.mark.skip(reason="旅客带婴儿,人工刷票-> 人工复核-> 登机口走人工放行-> 回查")
@pytest.mark.parametrize("creat_zhiji_random", [{"lk_bdno": "13","lk_flight": "3U8748","lk_inf":"INF"}],indirect=True)
def test_011(creat_zhiji_random,struct_pho):
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logging.info("测试的身份证号码:%s" %zhiji_dic["idNo"])
    # """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
    res = AirportProcess().api_face_security_manual_check(
                                reqId=get_uuid(),
                                flightNo=zhiji_dic["lk_flight"],
                                faceImage=pho_dic["scenePhoto"],
                                gateNo=zhiji_dic["lk_bdno"],
                                deviceCode="T1AJ002",
                                boardingNumber=zhiji_dic["lk_bdno"],
                                seatId="INF",
                                startPort="呼和浩特",
                                flightDay=zhiji_dic["lk_date"],
                                faceFeature=pho_dic["sceneFeature"],
                                kindType=1,  # 类型：0：刷票 1：刷票放行
                                largePhoto=pho_dic["largePhoto"])
    logging.info(res.text)

    # """2.3.17 人员回查-安检、登机口接口（二期）"""
    # res = AirportProcess().api_face_data_flowback_query(
    #     cardId=zhiji_dic["idNo"],
    #     flightNo=zhiji_dic["lk_flight"],
    #     flightDay=zhiji_dic["lk_date"],
    #     boardingNumber=zhiji_dic["lk_bdno"],
    #     seatId=zhiji_dic["lk_inf"]

    time.sleep(5)
    # """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    # res = AirportProcess().api_face_review_manual_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF002",
    #     scenePhoto=pho_dic["scenePhoto"],
    #     cardNo=zhiji_dic["idNo"],
    #     passengerName="大西瓜",
    #     passengerEnglishName="XIGUA",
    #     securityStatus=1,  # 安检的状态(0人证1:1,  1 人工放行,  2闸机B门通过,3-未知)
    #     securityPassTime=zhiji_dic["lk_chkt"],
    #     securityGateNo="",
    #     securityDeviceNo="",
    #     flightNo=zhiji_dic["lk_flight"],
    #     boardingNumber=zhiji_dic["lk_bdno"],
    #     sourceType=0,
    #     flightDay=zhiji_dic["lk_date"])
    # logging.info(res.text)
    #
    # res = AirportProcess().api_face_boarding_start(
    #     flightNo=zhiji_dic["lk_flight"],
    #     boardingGate=zhiji_dic["lk_bdno"],
    #     deviceCode="T1ZZ002",
    #     gateNo=zhiji_dic["lk_bdno"],
    #     flightDay="2019-11-01"
    # )
    # logging.info(res.text)
    #
    # """2.3.13登机口人工放行、报警接口（二期）"""
    # res = AirportProcess().api_face_boarding_manual_check(
    #     flightNo=zhiji_dic["lk_flight"],
    #     date="20191101",
    #     boardingGate=zhiji_dic["lk_bdno"],
    #     deviceCode="T1ZZ002",
    #     gateNo=zhiji_dic["lk_bdno"],
    #     sourceType=0, #0 放行
    #     cardId=zhiji_dic["idNo"],
    #     scenePhoto=pho_dic["scenePhoto"],
    #     passengerName="大西瓜",
    #     boardingNumber=zhiji_dic["lk_bdno"]
    # )
    # logging.info(res.text)

    """2.3.17 人员回查-安检、登机口接口（二期）"""
    res = AirportProcess().api_face_data_flowback_query(
        cardId="",
        flightNo=zhiji_dic["lk_flight"],
        flightDay=zhiji_dic["lk_date"],
        boardingNumber=zhiji_dic["lk_bdno"],
        seatId=""
    )
    logging.info(res.text)
    logging.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)




if __name__ == '__main__':
    pytest.main(["-s", "test_miss_flight.py"])
