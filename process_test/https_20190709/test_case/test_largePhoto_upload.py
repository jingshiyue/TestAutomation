#!/usr/bin/python3
# Time : 2019/8/13 9:15 
# Author : zcl
import pytest,random,os,sys,pymysql
from https_20190709.common.common_method import *
from BaiTaAirport2_month.common import Idcardnumber
from https_20190709.API_https.AirportProcess import *
from BaiTaAirport2_month.msgQueue import Autosendlk
from BaiTaAirport2_month.common.mysql_class import *

def log(res):
    """
    打印结果
    :param res:
    :return:
    """
    logging.info("---------------------------------------------------")
    logging.info(res.text)
    logging.info("---------------------------------------------------")
    sleep(1)


# @pytest.mark.skip(reason="A-> B-> 复核")
@pytest.mark.parametrize("insert_data_into_mysql", [{"bdno": "16", "date": "20191024", "flight_no": "FU6630"}],indirect=True)
@pytest.mark.parametrize("creat_zhiji_random", [{"lk_bdno": "16", "lk_date": "20191024", "lk_flight": "FU6630"}],indirect=True)
def test_02(insert_data_into_mysql,creat_zhiji_random,struct_pho): #02表示第二行
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logging.info("测试的身份证号码:%s" %zhiji_dic["idNo"])
    """2.3.20自助验证闸机A门接口（二期）"""
    res = AirportProcess().api_security_ticket_check(
        reqId=get_uuid(),  # 必填
        gateNo="T1AJ1",  # 必填,A B门T1AJ1，复核对应T1AF1
        deviceId="T1AJ001",  # 必填
        cardType="0",  # 必填
        idCard=zhiji_dic["idNo"],  # 必填
        nameZh="西瓜",
        nameEn="xigua",
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
    log(res)


    """2.3.21自助验证闸机B门接口（二期）"""
    res = AirportProcess().api_face_security_face_check(
        reqId=get_uuid(),  # 必填
        gateNo="T1AJ1",  # 必填
        deviceId="T1AJ001",  # 必填
        cardType=0,  # 必填
        idCard=zhiji_dic["idNo"],  # 必填
        nameZh="西瓜",
        nameEn="xigua",
        age=get_age(zhiji_dic["idNo"]),
        sex="1",
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
    log(res)

    """2.3.22	自助闸机复核接口（二期）  [1:N]"""
    res = AirportProcess().api_face_review_self_check(
        reqid=get_uuid(),  # 必填
        gateno = "T1AF1",  # 必填 对应T1AJ1
        deviceid = "T1AJ002",  # 必填
        scenephoto = pho_dic["scenePhoto"],  # 必填,可以不用2K
        scenefeature = pho_dic["sceneFeature_2k"])  # 必填,需要2K文件夹里
    log(res)

    """2.3.24	人员回查-安检、登机口接口（二期）"""
    res = AirportProcess().api_face_data_flowback_query(
        reqId=get_uuid(),
        cardId=zhiji_dic["idNo"],
        flightNo=zhiji_dic["lk_flight"],
        flightDay=zhiji_dic["lk_date"],  # 航班dd
        boardingNumber=zhiji_dic["lk_bdno"],
        isFuzzyQuery=0)  # 不传是默认模糊查询，传值1-为模糊查询，非1为精确查询
    log(res)

    logging.info("test_02测试完成")

# @pytest.mark.skip(reason="debug skip")
def test_03(creat_zhiji_random,struct_pho): #03表示第三行
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logging.info("测试的身份证号码:%s" %zhiji_dic["idNo"])
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
    log(res)

    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
                        reqId=get_uuid(),
                        gateNo="T1AF1",
                        deviceId="T1AF002",
                        scenePhoto=pho_dic["scenePhoto"],
                        cardNo=zhiji_dic["idNo"],
                        passengerName="西瓜",
                        passengerEnglishName="xigua",
                        securityStatus=1,#安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
                        securityPassTime=zhiji_dic["lk_chkt"],
                        securityGateNo="",
                        securityDeviceNo="",
                        flightNo=zhiji_dic["lk_flight"],
                        boardingNumber=zhiji_dic["lk_bdno"],
                        sourceType=0,
                        flightDay=zhiji_dic["lk_date"])
    log(res)
    logging.info("test_03测试完成")


# @pytest.mark.skip(reason="debug skip")
def test_04(creat_zhiji_random,struct_pho): #04表示第四行
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logging.info("测试的身份证号码:%s" %zhiji_dic["idNo"])
    """2.3.20自助验证闸机A门接口（二期）"""
    res = AirportProcess().api_security_ticket_check(
                                  reqId=get_uuid(),     #必填
                                  gateNo="T1AJ1",      #必填,A B门T1AJ1，复核对应T1AF1
                                  deviceId="T1AJ001",  #必填
                                  cardType="0",         #必填
                                  idCard=zhiji_dic["idNo"],         #必填
                                  nameZh="西瓜",
                                  nameEn="xigua",
                                  age=get_age(zhiji_dic["idNo"]),
                                  sex=1,
                                  birthDate=get_birthday(zhiji_dic["idNo"]),      #必填
                                  address="重庆市",
                                  certificateValidity="20120101-20230202",   #必填
                                  nationality="CHina",
                                  ethnic="汉族",
                                  contactWay="13512134390",
                                  cardPhoto=pho_dic["cardPhoto"],     #必填
                                  fId=get_uuid()       #必填
                                  )
    log(res)


    """2.3.21自助验证闸机B门接口（二期）"""
    res = AirportProcess().api_face_security_face_check(
                                     reqId=get_uuid(),  #必填
                                     gateNo="T1AJ1",#必填
                                     deviceId="T1AJ001",#必填
                                     cardType=0,#必填
                                     idCard=zhiji_dic["idNo"],#必填
                                     nameZh="西瓜",
                                     nameEn="xigua",
                                     age=get_age(zhiji_dic["idNo"]),
                                     sex="1",
                                     birthDate=get_birthday(zhiji_dic["idNo"]),#必填
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",#必填
                                     nationality="China",#必填
                                     ethnic="汉族",#必填
                                     contactWay="13512134390",
                                     scenePhoto=pho_dic["scenePhoto"],#必填
                                     sceneFeature=pho_dic["sceneFeature"],#必填
                                     cardPhoto=pho_dic["cardPhoto"],#必填
                                     cardFeature=pho_dic["cardFeature"],#必填
                                     largePhoto=pho_dic["largePhoto"]#必填
                                    )
    log(res)

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
                                largePhoto="")
    log(res)

    """2.3.22	自助闸机复核接口（二期）  [1:N]"""
    res = AirportProcess().api_face_review_self_check(
        reqid=get_uuid(),  # 必填
        gateno = "T1AF1",  # 必填 对应T1AJ1
        deviceid = "T1AJ002",  # 必填
        scenephoto = pho_dic["scenePhoto"],  # 必填,可以不用2K
        scenefeature = pho_dic["sceneFeature_2k"])  # 必填,需要2K文件夹里
    log(res)
    logging.info("test_04测试完成")

# @pytest.mark.skip(reason="debug skip")
def test_05(creat_zhiji_random,struct_pho): #05表示第五行
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logging.info("测试的身份证号码:%s" %zhiji_dic["idNo"])

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
    log(res)

    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
                        reqId=get_uuid(),
                        gateNo="T1AF1",
                        deviceId="T1AF002",
                        scenePhoto=pho_dic["scenePhoto"],
                        cardNo=zhiji_dic["idNo"],
                        passengerName="西瓜",
                        passengerEnglishName="xigua",
                        securityStatus=1,#安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
                        securityPassTime=zhiji_dic["lk_chkt"],
                        securityGateNo="",
                        securityDeviceNo="",
                        flightNo=zhiji_dic["lk_flight"],
                        boardingNumber=zhiji_dic["lk_bdno"],
                        sourceType=0,
                        flightDay=zhiji_dic["lk_date"])
    log(res)
    logging.info("test_05测试完成")

# @pytest.mark.skip(reason="debug skip")
def test_06(creat_zhiji_random,struct_pho):
    another_pho = to_base64(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\1.jpg")
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logging.info("测试的身份证号码:%s" %zhiji_dic["idNo"])

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

    """2.3.20自助验证闸机A门接口（二期）"""
    res = AirportProcess().api_security_ticket_check(
                                  reqId=get_uuid(),     #必填
                                  gateNo="T1AJ1",      #必填,A B门T1AJ1，复核对应T1AF1
                                  deviceId="T1AJ001",  #必填
                                  cardType="0",         #必填
                                  idCard=zhiji_dic["idNo"],         #必填
                                  nameZh="西瓜",
                                  nameEn="xigua",
                                  age=get_age(zhiji_dic["idNo"]),
                                  sex=1,
                                  birthDate=get_birthday(zhiji_dic["idNo"]),      #必填
                                  address="重庆市",
                                  certificateValidity="20120101-20230202",   #必填
                                  nationality="CHina",
                                  ethnic="汉族",
                                  contactWay="13512134390",
                                  cardPhoto=pho_dic["cardPhoto"],     #必填
                                  fId=get_uuid()       #必填
                                  )
    log(res)


    """2.3.21自助验证闸机B门接口（二期）"""
    res = AirportProcess().api_face_security_face_check(
                                     reqId=get_uuid(),  #必填
                                     gateNo="T1AJ1",#必填
                                     deviceId="T1AJ001",#必填
                                     cardType=0,#必填
                                     idCard=zhiji_dic["idNo"],#必填
                                     nameZh="西瓜",
                                     nameEn="xigua",
                                     age=get_age(zhiji_dic["idNo"]),
                                     sex="1",
                                     birthDate=get_birthday(zhiji_dic["idNo"]),#必填
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",#必填
                                     nationality="China",#必填
                                     ethnic="汉族",#必填
                                     contactWay="13512134390",
                                     scenePhoto=pho_dic["scenePhoto"],#必填
                                     sceneFeature=pho_dic["sceneFeature"],#必填
                                     cardPhoto=pho_dic["cardPhoto"],#必填
                                     cardFeature=pho_dic["cardFeature"],#必填
                                     largePhoto=another_pho  #必填
                                    )
    log(res)

    """2.3.17安检口人工放行接口（二期）"""

    res = AirportProcess().api_face_security_manual_optcheck(
                                          reqId=get_uuid(),
                                          gateNo="T1AF1",
                                          deviceId="T1AJ001",
                                          cardType=0,
                                          idCard=zhiji_dic["idNo"],
                                          nameZh="西瓜",
                                          nameEn="xigua",
                                          age=get_age(zhiji_dic["idNo"]),
                                          sex="",
                                          birthDate=get_birthday(zhiji_dic["idNo"]),
                                          address="",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=pho_dic["scenePhoto"],
                                          sceneFeature=pho_dic["sceneFeature"],
                                          cardPhoto=pho_dic["cardPhoto"],
                                          cardFeature=pho_dic["cardFeature"],
                                          largePhoto=pho_dic["largePhoto"])

    log(res)

    """2.3.22	自助闸机复核接口（二期）  [1:N]"""
    res = AirportProcess().api_face_review_self_check(
        reqid=get_uuid(),  # 必填
        gateno = "T1AF1",  # 必填 对应T1AJ1
        deviceid = "T1AJ002",  # 必填
        scenephoto = pho_dic["scenePhoto"],  # 必填,可以不用2K
        scenefeature = pho_dic["sceneFeature_2k"])  # 必填,需要2K文件夹里
    log(res)
    logging.info("test_06测试完成")

# @pytest.mark.skip(reason="debug skip")
def test_07(creat_zhiji_random,struct_pho):
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logging.info("测试的身份证号码:%s" %zhiji_dic["idNo"])

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
                                kindType=1,  # 类型：0：刷票 1：刷票放行
                                largePhoto=pho_dic["largePhoto"])
    log(res)

    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF002",
        scenePhoto=pho_dic["scenePhoto"],
        cardNo=zhiji_dic["idNo"],
        passengerName="西瓜",
        passengerEnglishName="xigua",
        securityStatus=1,  # 安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
        securityPassTime=zhiji_dic["lk_chkt"],
        securityGateNo="",
        securityDeviceNo="",
        flightNo=zhiji_dic["lk_flight"],
        boardingNumber=zhiji_dic["lk_bdno"],
        sourceType=0,
        flightDay=zhiji_dic["lk_date"])
    log(res)
    logging.debug("test_07测试完成")

# @pytest.mark.skip(reason="debug skip")
def test_08(creat_zhiji_random,struct_pho):
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logging.info("测试的身份证号码:%s" %zhiji_dic["idNo"])

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
                                kindType=1,  # 类型：0：刷票 1：刷票放行
                                largePhoto=pho_dic["largePhoto"])
    log(res)

    """安检1：1刷证  包括A B 门"""
    """2.3.20自助验证闸机A门接口（二期）"""
    res = AirportProcess().api_security_ticket_check(
        reqId=get_uuid(),  # 必填
        gateNo="T1AJ1",  # 必填,A B门T1AJ1，复核对应T1AF1
        deviceId="T1AJ001",  # 必填
        cardType="0",  # 必填
        idCard=zhiji_dic["idNo"],  # 必填
        nameZh="西瓜",
        nameEn="xigua",
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
    log(res)

    """2.3.21自助验证闸机B门接口（二期）"""
    res = AirportProcess().api_face_security_face_check(
        reqId=get_uuid(),  # 必填
        gateNo="T1AJ1",  # 必填
        deviceId="T1AJ001",  # 必填
        cardType=0,  # 必填
        idCard=zhiji_dic["idNo"],  # 必填
        nameZh="西瓜",
        nameEn="xigua",
        age=get_age(zhiji_dic["idNo"]),
        sex="1",
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
        largePhoto=""  # 必填
    )

    """2.3.22	自助闸机复核接口（二期）  [1:N]"""
    res = AirportProcess().api_face_review_self_check(
        reqid=get_uuid(),  # 必填
        gateno = "T1AF1",  # 必填 对应T1AJ1
        deviceid = "T1AJ002",  # 必填
        scenephoto = pho_dic["scenePhoto"],  # 必填,可以不用2K
        scenefeature = pho_dic["sceneFeature_2k"])  # 必填,需要2K文件夹里
    log(res)
    logging.info("test_08测试完成")


# @pytest.mark.skip(reason="debug skip")
def test_09(creat_zhiji_random,struct_pho):
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
                                flightDay=zhiji_dic["lk_date"][-2:],
                                faceFeature=pho_dic["sceneFeature"],
                                kindType=1,  # 类型：0：刷票 1：刷票放行
                                largePhoto=pho_dic["largePhoto"])
    log(res)

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
                                kindType=1,  # 类型：0：刷票 1：刷票放行
                                largePhoto=another_pho)
    log(res)

    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF002",
        scenePhoto=pho_dic["scenePhoto"],
        cardNo=zhiji_dic["idNo"],
        passengerName="西瓜",
        passengerEnglishName="xigua",
        securityStatus=1,  # 安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
        securityPassTime=zhiji_dic["lk_chkt"],
        securityGateNo="",
        securityDeviceNo="",
        flightNo=zhiji_dic["lk_flight"],
        boardingNumber=zhiji_dic["lk_bdno"],
        sourceType=0,
        flightDay=zhiji_dic["lk_date"])
    log(res)
    logging.debug("test_09测试完成")

# @pytest.mark.skip(reason="debug skip")
def test_10(creat_zhiji_random,struct_pho):
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logging.info("测试的身份证号码:%s" %zhiji_dic["idNo"])

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
        kindType=1,  # 类型：0：刷票 1：刷票放行
        largePhoto=pho_dic["largePhoto"])
    log(res)

    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF002",
        scenePhoto=pho_dic["scenePhoto"],
        cardNo=zhiji_dic["idNo"],
        passengerName="西瓜",
        passengerEnglishName="xigua",
        securityStatus=1,  # 安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
        securityPassTime=zhiji_dic["lk_chkt"],
        securityGateNo="",
        securityDeviceNo="",
        flightNo=zhiji_dic["lk_flight"],
        boardingNumber=zhiji_dic["lk_bdno"],
        sourceType=0,
        flightDay=zhiji_dic["lk_date"])
    log(res)

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
        kindType=1,  # 类型：0：刷票 1：刷票放行
        largePhoto="")
    log(res)

    """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
    res = AirportProcess().api_face_review_manual_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF002",
        scenePhoto=pho_dic["scenePhoto"],
        cardNo=zhiji_dic["idNo"],
        passengerName="西瓜",
        passengerEnglishName="xigua",
        securityStatus=1,  # 安检的状态(0人证1:1,1 人工放行,2闸机B门通过,3-未知)
        securityPassTime=zhiji_dic["lk_chkt"],
        securityGateNo="",
        securityDeviceNo="",
        flightNo=zhiji_dic["lk_flight"],
        boardingNumber=zhiji_dic["lk_bdno"],
        sourceType=0,
        flightDay=zhiji_dic["lk_date"])
    log(res)

###   核对图片是否存入相应的表里
    connection = connect_db()
    data_list = query_data(connection,"sec_passenger_entity","flight",zhiji_dic["lk_flight"],"bdno",zhiji_dic["lk_bdno"])
    raw_largePhoto_data = ""
    with open(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\0.jpg","rb") as f:
        raw_largePhoto_data = f.read()
    for item in data_list:
        temp_d = query_data(connection,"security_check_info_entity", "ajid", item["ajid"])
        for tmp in temp_d:
            assert tmp["photo"][:100] == raw_largePhoto_data[:100]  #断言 安检信息系统中旅客图片为刷票上传的大图

    connection_t = connect_db(host = "192.168.5.15",db = "htbusyinfo",)
    man_sec_check = query_data(connection_t,"aib_manual_security_check_7_9", "certificate_number", zhiji_dic["idNo"])
    large_photo_path = ""
    for i in man_sec_check:
        if i["large_photo_path"] != "":
            large_photo_path = i["large_photo_path"]
    large_photo_path = "https://192.168.5.15:9090/data-platform-server/api/v1/resource/" + large_photo_path
    res_pho = requests.get(url=large_photo_path, verify=BlackListApi().certificate)
    assert res_pho.content == raw_largePhoto_data  #断言 安检流水表，redis中有上传的大图

    logging.info("%s 测试完成" % sys._getframe().f_code.co_name)



if __name__ == '__main__':
    # pytest.main(["-s", "test_largePhoto_upload.py"])
    pytest.main(["-s","test_largePhoto_upload.py::test_10"])
