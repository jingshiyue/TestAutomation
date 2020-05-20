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

# @pytest.mark.skip(reason="中转采集")
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


if __name__ == '__main__':
    pytest.main([
                 r"process_test\https_20190709\test_case\test_process.py",
                 "-v","-s",
                 "--log-cli-level=INFO",
                 ])