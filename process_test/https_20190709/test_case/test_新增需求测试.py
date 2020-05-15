#!/usr/bin/python3
# Time : 2019/11/1 10:39 
# Author : zcl
import pytest,random,os,sys,pymysql
from https_20190709.common.common_method import *
from BaiTaAirport2_month.common import Idcardnumber
from https_20190709.API_https.AirportProcess import *
from BaiTaAirport2_month.msgQueue import Autosendlk
from BaiTaAirport2_month.common.mysql_class import *


@pytest.mark.skip(reason="激活昨天序列号（sec_passenger_checkin表里的boarding_number）和航班号一致的航班")
def test_active_flight_AB(struct_pho):
        logging.info("**************%s 测试开始**************" % sys._getframe().f_code.co_name)
        pho_dic = struct_pho
        res = AirportProcess().api_data_flight_activate(flightDate="20191031",flightNo="NV54433")
        logging.info(res.text)
        time.sleep(3)
        """2.3.20自助验证闸机A门接口（二期）"""
        res = AirportProcess().api_security_ticket_check(
            reqId=get_uuid(),  # 必填
            gateNo="T1AJ1",  # 必填,A B门T1AJ1，复核对应T1AF1
            deviceId="T1AJ001",  # 必填
            cardType="0",  # 必填
            idCard="611022196411194877",  # 必填
            nameZh="周志喜457",
            nameEn="HHHH",
            age=get_age("611022196411194877"),
            sex=1,
            birthDate=get_birthday("611022196411194877"),  # 必填
            address="重庆市",
            certificateValidity="20120101-20230202",  # 必填
            nationality="CHina",
            ethnic="",
            contactWay="",
            cardPhoto=pho_dic["cardPhoto"],  # 必填
            fId=get_uuid()  # 必填
        )
        logging.info(res.text)
        time.sleep(3)
        """2.3.21自助验证闸机B门接口（二期）"""

        res = AirportProcess().api_face_security_face_check(
            reqId=get_uuid(),  # 必填
            gateNo="T1AJ1",  # 必填
            deviceId="T1AJ001",  # 必填
            cardType=0,  # 必填
            idCard="611022196411194877",  # 必填
            nameZh="西瓜",
            nameEn="HHHH",
            age=get_age("611022196411194877"),
            sex="1",
            birthDate=get_birthday("611022196411194877"),  # 必填
            address="重庆市",
            certificateValidity="20180101-20260203",  # 必填
            nationality="China",  # 必填
            ethnic="",  # 必填
            contactWay="",
            scenePhoto=pho_dic["scenePhoto"],  # 必填
            sceneFeature=pho_dic["sceneFeature"],  # 必填
            cardPhoto=pho_dic["cardPhoto"],  # 必填
            cardFeature=pho_dic["cardFeature"],  # 必填
            largePhoto=pho_dic["largePhoto"]  # 必填
        )
        logging.info(res.text)
        logging.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)

# @pytest.mark.skip(reason="旅客带婴儿,人工刷票-> 人工复核-> 登机口走人工放行-> 回查")
# @pytest.mark.parametrize("insert_data_into_mysql", [{"bdno": "10","flight_no": "3U8747"}],indirect=True)
@pytest.mark.parametrize("creat_zhiji_random", [{"lk_bdno": "10","lk_flight": "3U8747","lk_inf":"INF"}],indirect=True)
def test_01(creat_zhiji_random,struct_pho):
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
    time.sleep(5)
    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF002",
        scenePhoto=pho_dic["scenePhoto"],
        cardNo=zhiji_dic["idNo"],
        passengerName="大西瓜",
        passengerEnglishName="XIGUA",
        securityStatus=1,  # 安检的状态(0人证1:1,  1 人工放行,  2闸机B门通过,3-未知)
        securityPassTime=zhiji_dic["lk_chkt"],
        securityGateNo="",
        securityDeviceNo="",
        flightNo=zhiji_dic["lk_flight"],
        boardingNumber=zhiji_dic["lk_bdno"],
        sourceType=0,
        flightDay=zhiji_dic["lk_date"])
    logging.info(res.text)

    """2.3.13登机口人工放行、报警接口（二期）"""
    res = AirportProcess().api_face_boarding_manual_check(
        flightNo=zhiji_dic["lk_flight"],
        date=zhiji_dic["lk_date"],
        boardingGate=zhiji_dic["lk_bdno"],
        deviceCode="DJK",
        cardId=zhiji_dic["idNo"],
        scenePhoto=zhiji_dic["scenePhoto"],
        passengerName="大西瓜",
        boardingNumber=zhiji_dic["lk_bdno"]
    )
    logging.info(res.text)

    """2.3.17 人员回查-安检、登机口接口（二期）"""
    res = AirportProcess().api_face_data_flowback_query(
        cardId=zhiji_dic["idNo"],
        flightNo=zhiji_dic["lk_flight"],
        flightDay=zhiji_dic["lk_date"],
        boardingNumber=zhiji_dic["lk_bdno"],
        seatId=zhiji_dic["lk_inf"]
    )
    logging.info(res.text)

    logging.info("**************%s 测试完成**************" % sys._getframe().f_code.co_name)

