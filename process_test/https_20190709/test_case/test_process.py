#!/usr/bin/python3
# Time : 2020/4/28 09:49
# Author : zcl
"""
用于测试 安检->复核->登机口复核  多种流程
"""
import pytest
import os
import sys
print({"cwd":os.getcwd()})
sys.path.append(r"D:\workfile\zhongkeyuan_workspace\TestAutomation\process_test")

import threading
import xlwt
from BaiTaAirport2_month.msgQueue.Autosendlk import *
from https_20190709.API_https.AirportProcess import AirportProcess
from https_20190709.common.common_method import *
import json

import logging
# logging.basicConfig(level=logging.INFO,   #log文件写入等级
#                     format='[%(asctime)s %(filename)s line:%(lineno)d]%(levelname)s:  %(message)s',
#                     filename=r"D:\workfile\zhongkeyuan_workspace/test.log",
#                     filemode='a'
#                     )
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)     #设置控制台输出等级
# formatter = logging.Formatter('[%(asctime)s %(filename)s line:%(lineno)d]%(levelname)s:  %(message)s')
# console.setFormatter(formatter)
# logging.getLogger().addHandler(console)

# logging.basicConfig(level=logging.INFO,  # log文件写入等级
#                     format='[%(asctime)s %(filename)s line:%(lineno)d]%(levelname)s:  %(message)s',
#                     )

dataInfo = {}

def get_useful_flight():
    """
    return 从172.18.2.199 redis中获取可用测试的航班
    parm:gateNoList 登机口列表 如["02","02A","03","03A",]
    """
    import redis
    try:
        sr=redis.StrictRedis(host='172.18.2.199', port=6379, db=2,password='cigit')
    except Exception as e:
        print(e)

    import time
    flightTemp = "plan-" + time.strftime("%Y-%m-%d",time.localtime()) #plan-2020-05-08
    for gate in ["02","14"]:
        flightNum = flightTemp + "-" + gate  #plan-2020-05-08-02
        zsetRes = sr.zrange(flightNum,0,-1,withscores=True)   #当天每个登机口里的航班
        for flight in zsetRes:
            try:
                detailFlight = "status-" + time.strftime("%Y-%m-%d",time.localtime()) + "-" + str(flight[0][:6])[2:-1]  #status-2020-05-08-3U8747
                hRes = sr.hmget(detailFlight, "flightDate","depTimeJ","twoFlightNo","gateNo","status")  #航班详细信息
                depTimeJ = str(hRes[0])[2:-1] + " " + str(hRes[1])[2:-1]   #redis中预计起飞时间， 日期 + 时间:2020-05-09 0725
                timeArray = time.strptime(depTimeJ, "%Y-%m-%d %H%M")
                timeStamp = int(time.mktime(timeArray))
                offsetTime = int((timeStamp-time.time())/60)  #redis中的起飞时间与现在时间的时间差(min)
                if offsetTime > 60*1:    #时间差大于1小时
                    
                    return hRes   #byte类型 [b'2020-05-09', b'1150', b'CA1118', b'14', b'0']
            except Exception as e:
                print(e)
                print("该次格式化航班出错，将跳过筛选...")
        flightNum = flightTemp

# dataInfo["flight_no"] = "CA1649"
# dataInfo["bdno"] = "10"
# dataInfo["date"] = "20200428"

# @pytest.mark.parametrize("get_useful_flight", ["11","12","13",],indirect=True)
# def setup_function():
#     logging.info("setup_function：每个用例开始前都会执行")
#     flight = get_useful_flight()
#     dataInfo["flight_no"] = str(flight[2])[2:-1]
#     dataInfo["bdno"] = str(flight[3])[2:-1]
#     dataInfo["date"] = str(flight[0])[2:-1]
#     logging.info({"dataInfo_setup_function":dataInfo})
    
    """登机准备:1、登机口拉取航班；2、发登记指令"""
    # res = AirportProcess().api_face_boarding_strange(flightNo=dataInfo["flight_no"],
    #                                                  boardingGate=dataInfo["bdno"],
    #                                                  deviceCode="T1ZZ002",
    #                                                  gateNo="01",
    #                                                  flightDay=dataInfo["date"]               #YYYY-MM-DD
    #                                                  )
    # logging.info("变更登机口响应：" + res.text)
    # time.sleep(0.2)
    #http开始登机
    res = AirportProcess().api_face_boarding_start(flightNo=dataInfo["flight_no"],
                                                     boardingGate=dataInfo["bdno"],
                                                     deviceCode="T1ZZ002",
                                                     gateNo="01",
                                                     flightDay=dataInfo["date"]
                                                     )
    logging.info("开始登机响应：%s"   % res.text)

def teardown_function():
    logging.info("teardown_function：每个用例结束后都会执行")
    dataInfo = {}

@pytest.mark.skip(reason="插入安检表 + 产生值机信息")
@pytest.mark.parametrize("insert_data_into_mysql", [{"bdno":"10","date":"20200428","flight_no":"CA1645"}], indirect=True)
@pytest.mark.parametrize("creat_zhiji_random", [{"lk_bdno": "10","lk_date":"20200428","lk_flight": "CA1645"}],indirect=True)
def test_anjian_and_zhiji(insert_data_into_mysql,creat_zhiji_random):
    logging.info("安检+值机完成")

@pytest.mark.skip(reason="产生值机信息")
@pytest.mark.parametrize("creat_zhiji_random", [{"lk_bdno": "10","lk_date":"20200428","lk_flight": "CA1645"}],indirect=True)
def test_zhiji(creat_zhiji_random):
    logging.info("安检+值机完成")


"""
"lk_gateno":"10" ,    登机口
"lk_flight": "CA1645",  航班号
"lk_bdno":"001",  登机序号
"""
@pytest.mark.skip(reason="根据登机口自动查找到航班(起飞时间间隔>1)A-> B-> 复核(分为自助和人工两种)-> 发送开始登机-> 登机复核")
@pytest.mark.parametrize("creat_zhiji_byFlight", [{"lk_cname":"大西瓜003"}],indirect=True)
def test_01(creat_zhiji_byFlight,struct_pho):    #{'flight_no': 'CA8295', 'bdno': '02', 'date': '2020-05-09'}
    zhiji_dic = creat_zhiji_byFlight
    pho_dic = struct_pho
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
    logging.info({"第一次安检时间:":time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())})
    time.sleep(3)
    ############################################################################
    """2.3.22	自助闸机复核接口（二期）  [1:N]"""
    res = AirportProcess().api_face_review_self_check(
        reqid=get_uuid(),  # 必填
        gateno = "T1AF1",  # 必填 对应T1AJ1
        deviceid = "T1AJ002",  # 必填
        scenephoto = pho_dic["scenePhoto_fuhe"],  # 必填,可以不用2K
        scenefeature = pho_dic["sceneFeature_2k"])  # 必填,需要2K文件夹里
    result = json.loads(res.text)
    del result['userInfo']['basePhoto']
    logging.info({"系统复核: ":result})

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
    # logging.info({"人工复核: ",res.text})
    ############################################################################

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
    logging.info({"登机口系统复核: ":res.text})
    ############################################################################
    logging.info("test_01测试完成")


@pytest.mark.skip(reason="中转采集")
@pytest.mark.parametrize("creat_zhiji_random", [{"lk_flight":"CA8128","lk_cname":"大西瓜001","lk_bdno": "001","lk_gateno":"10"}],indirect=True)
def test_02(creat_zhiji_random,struct_pho):    #{'flight_no': 'CA8295', 'bdno': '02', 'date': '2020-05-09'}
    zhiji_dic = creat_zhiji_random
    pho_dic = struct_pho
    logging.info({"值机信息: ":zhiji_dic})

    res = AirportProcess().api_face_transfergate_face_collect(
        reqId=get_uuid(),
        flightNo=zhiji_dic["lk_flight"],
        faceImage=pho_dic["scenePhoto"],
        faceFeature=pho_dic["sceneFeature"],
        deviceCode="T1ZZ002",
        gateNo=zhiji_dic["lk_gateno"],
        seatId=zhiji_dic["lk_seat"],
        startPort="HET",
        boardingNumber=zhiji_dic["lk_bdno"],
        flightDay="11",   # 传Dd
        sourceType=0,    #0,中转；1，经停；2、备降采集；3、中转人工放行；4、经停人工放行；5、备降人工放行 6、经停证件采集（废弃）
        endPort="",
        cardId="",       #非必须  sourceType为6-经停证采集必给
        nameZh="",       #非必须  sourceType 为6-经停证采集必给
        mainFlightNo="", #非必须  主航班
        cardPhoto="",    #非必须  身份证件照base64编码
        cardFeature="",  #非必须  证件照特征base64
        largePhoto="",   #非必须  大图（口罩检测用）
        facePst=""       #非必须  人脸坐标（口罩检测用）
    )
    ############################################################################
    logging.info("test_02测试完成")


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
    """
    --capture=sys : 捕获print，将print写入到html里;
    logging和--capture=no实现运行测试用例的实时输出所有的log信息;
    """
    # pytest.main(["test_process.py","--html=./report/report_%s.html"])
    # pytest.main(["-v", "-s", "test_process.py", "--color=yes", "--reruns=2", "--self-contained-html","--html=./report/report_%s.html"])
    # import time
    # timestamp = time.strftime("%Y%m%d%H%M%S",time.localtime())
    pytest.main([
                 r"process_test\https_20190709\test_case\test_process.py",
                 "-v","-s",
                 "--log-cli-level=INFO",
                #  "--log-cli-date-format=%Y-%m-%d %H:%M:%S",
                #  "--log-cli-format=[%(asctime)s %(filename)s line:%(lineno)d]%(levelname)s:  %(message)s",
                 # "--setup-show=OFF"
                 ])

    # flight = get_useful_flight(["14"])
    # print(flight)
