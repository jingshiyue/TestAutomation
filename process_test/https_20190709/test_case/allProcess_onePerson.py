#!/usr/bin/python3
# Time : 2020/4/22 14:49
# Author : zcl
"""
备降流程，不值机
安检:人工通道 -> 复核:人工通道(face/review/check 现场不用了,换成face/review/manual-check) ->登机:人工通道

"""
import os
import threading
import xlwt
from BaiTaAirport2_month.msgQueue.Autosendlk import *
from https_20190709.API_https.AirportProcess import AirportProcess
from https_20190709.common.common_method import *
import logging
#log surpport
logging.basicConfig(level=logging.DEBUG,
                    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    filename=r"D:\workfile\zhongkeyuan_workspace\https_20190709\test_case/test.log",
                    filemode = 'a'
                    )
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
# console.setFormatter(formatter)
logging.getLogger().addHandler(console)
# logging.info("Here should not have addr!")


def boarding_pre():
    """登机准备:1、登机口拉取航班；2、发登记指令"""
    res = AirportProcess().api_face_boarding_strange(flightNo=flightNo,
                                                     boardingGate=boardingGate,
                                                     deviceCode="T1ZZ002",
                                                     gateNo="01",
                                                     flightDay=flightDate               #YYYY-MM-DD
                                                     )
    logging.info("变更登机口响应：" + res.text)
    time.sleep(0.2)
    #http开始登机
    res = AirportProcess().api_face_boarding_start(flightNo=flightNo,
                                                     boardingGate=boardingGate,
                                                     deviceCode="T1ZZ002",
                                                     gateNo="01",
                                                     flightDay=flightDate
                                                     )
    logging.info("开始登机响应：%s"   % res.text)

def process_01():
    """安检，分为系统和人工

    """
    offset = 0
    for i in range(boarding_start, boarding_start + anjianNum):
        offset += 1
        cardPhoto = to_base64(main_path + "picture(现场照片)/%s" % dir_list[i])  # 身份证照片
        feature_8k = read_feature(main_path + "picture8k/%s.txt" % dir_list[i].split(".")[0])  # 读取8k特征
        # feature_8k = read_feature(main_path + "picture8k/%s.txt" %i)  # 读取8k特征
        logging.debug("picture(现场照片)/%s" % dir_list[i])
        logging.debug("picture8k/%s.txt" % dir_list[i].split(".")[0])
        lk_cname = "测试%s" % i  # 中文姓名
        # logging.info("航班号:" + flight_no + ",登机序号:" + bdno)
        """安检人工通道刷票"""
        res = AirportProcess().api_face_security_manual_check(
            flightNo=flightNo,
            faceImage=cardPhoto,
            gateNo="T1AJ1",
            deviceCode="T1AJ001",
            boardingNumber=str(int(boardingNumber) + offset),  # 登机序列号
            # seatId="04" + "A",
            seatId=str(int(boardingNumber) + offset) + "A",
            startPort="HET",  #出发港  HET 表示呼和浩特
            flightDay=date[-2:],
            faceFeature=feature_8k,
            kindType=0,  # 类型：0：刷票 1：刷票放行
            largePhoto=largePhoto
        )
        print("安检人工通道刷票响应: " + res.text)
    time.sleep(3)

def process_02():
    """旅客通道复核,分为系统和人工
        face/review/manual-check 人工
        /face/review/self-check  系统
    """
    tmp_num = 1
    for h in range(boarding_start,boarding_start+fuheNum):
        cardPhoto = to_base64(main_path + "picture(现场照片)/%s"%dir_list[h])  # 身份证照片
        feature_2k = read_feature(main_path + "picture2k/%s.txt" % dir_list[h].split(".")[0])  # 读取2k特征
        logging.debug("picture(现场照片)/%s"%dir_list[h])
        logging.debug("picture2k/%s.txt" % dir_list[h].split(".")[0])
        res = AirportProcess().api_face_review_check(gateNo="T1AF1",   # 旅客通道复核
                                      deviceId="T1AF001",
                                      scenePhoto=cardPhoto,
                                      sceneFeature=feature_2k)

        # res = AirportProcess().api_face_review_manual_check()
        print("通道复核响应" + res.text)
        print("第%s个旅客复核完成..." %tmp_num)
        tmp_num += 1
    time.sleep(10)

def process_03():
    """
    登机口复核，分为系统和人工
    """
    tmp_num = 1
    offset = 0
    for n in range(boarding_start,boarding_start+dengjiNum):
        offset += 1
        cardPhoto = to_base64(main_path + "picture(现场照片)/%s"%dir_list[n])  # 身份证照片
        feature_2k = read_feature(main_path + "picture2k/%s.txt" % dir_list[n].split(".")[0])  # 读取2k特征
        # 登机口复核
        # res = AirportProcess().api_face_boarding_review_check(faceImage=cardPhoto,
        #                                                       faceFeature=feature_2k,
        #                                                       deviceCode="T1DJ001",
        #                                                       boardingGate=boardingGate,
        #                                                       flightNo=flightNo,
        #                                                       flightDay=produce_flight_date(),  # （yyyyMMdd）
        #                                                       gateNo="01"
        #                                                       )
        # print("第%s个旅客登机口复核响应"%tmp_num + res.text)

        # 登机口人工通道
        res = AirportProcess().api_face_boarding_manual_check(
            reqId=get_uuid(),
            flightNo=flightNo,
            date=str(time.strftime("%Y%m%d", time.localtime())),  #YYYYMMDD
            boardingGate=boardingGate,
            deviceCode="T1DJ001",
            gateNo="01", 
            # cardId="50038219990909707%d" %n,
            scenePhoto="",
            sourceType=0,  #0-放行，1-报警
            passengerName="旅客姓名", #旅客姓名
            boardingNumber=str(int(boardingNumber) + offset),
            seatId=str(int(boardingNumber) + offset) + "A",  # 座位号
        )
        print("登机口人工通道: " + res.text)

# def flowback_query():
#     res = AirportProcess().api_face_data_flowback_query(
#                                      reqId=get_uuid(),
#                                      # cardId="",
#                                      flightNo=flightNo,
#                                      flightDay="20200423",  # 航班dd
#                                      boardingNumber="1",
#                                      isFuzzyQuery=0,
#                                      )
#     print(res.text)

if __name__ == '__main__':
    largePhoto = to_base64(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture_640_480/1.jpg")  # 现场大图
    # 添加40个航班，每个航班350个人
    main_path = r"D:\workfile\zhongkeyuan_workspace\test_photoes\\"
    dir_list = os.listdir(main_path + "picture(现场照片)")
    anjianNum = 1  #安检人数
    fuheNum = 1    #复核人数
    dengjiNum = 1  #登机口复核人数
    boarding_start = 684  # 特征值有关
    boardingNumber = "001"  # 登机序号
    boardingGate = "02"  # 登机口
    flightNo = "HU7449"
    date = produce_flight_date()
    flightDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:10]  # 航班时间，格式为"2019-04-23"
    # 开始登机:  安检、复核、登机口复核
    # process_01()
    # boarding_pre()   #执行一次
    # process_02()
    # process_03()

    res = AirportProcess().api_face_data_flowback_query(
        reqId=get_uuid(),
        # cardId="142724198605103941",
        flightNo=flightNo,
        boardingNumber=boardingNumber,
        flightDay="11",  # 航班dd
        isFuzzyQuery=0,
        # seatId="0INF"
    )
    print(res.text)

    # res = AirportProcess().api_v1_face_boarding_passenger_query(
    #     reqId=get_uuid(),
    #     flightNo=flightNo,  # 必须，航班号
    #     date="2020-05-11",  # 必须，日期yyyy-MM-dd
    #     queryType=0,  # 必须，查询类型：0-建库旅客查询；1-已登机旅客查询；2-未登机旅客查询; 3-全查询
    #     pageNum=1,  # 必须，页码
    #     pageSize=40,  # 必须，分页长度
    #     isCount=1,  # 必须，为1时查询总记录数
    #     gateNo="",
    #     boardingGate="02"
    # )
    # print(res.text)


