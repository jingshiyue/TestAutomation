# coding:utf-8
from https_20190709.API_https.BlackList import *
# from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture
import threading


class AirportProcess(BlackListApi):
    def __init__(self, host="http://172.18.2.199:9091/"):
        BlackListApi.__init__(self, host)
        self.A_security_ticket_check = self.host + self.anjian_server + "/api/v1/face/security/ticket-check"
        self.B_security_face_check = self.host + self.anjian_server + "/api/v1/face/security/face-check"
        self.api_v1_face_review_check = self.host + self.review_server + "/api/v1/face/review/check"
        self.api_v1_face_review_manual_check = self.host + self.review_server + "/api/v1/face/review/manual-check"  # 复核人工通道
        self.api_v1_face_security_manual_check = self.host + self.anjian_server + "/api/v1/face/security/manual-check"  # 安检人工通道
        self.api_v1_face_transfergate_ticket_collect = self.host + self.boardinggate_server + "/api/v1/face/transfergate/ticket-collect"
        self.api_v1_face_transfergate_face_collect = self.host + self.boardinggate_server + "/api/v1/face/transfergate/face-collect"
        self.api_v1_face_notice_crateLib = self.host + self.boardinggate_server + "/api/v1/face/notice/crateLib"  # 登机口通知建库
        self.api_v1_face_boarding_check = self.host + self.boardinggate_server + "/api/v1/face/boarding/check"  # 登机口复核
        self.api_v1_face_boarding_library_check = self.host + self.boardinggate_server + "/api/v1/face/boarding/library-check"  # 登机口建库人数查询
        self.api_v1_face_boarding_manual_check = self.host + self.boardinggate_server + "/api/v1/face/boarding/manual-check"  # 登机口人工放行报警
        self.api_v1_face_data_flowback_query = self.host + self.data_platform_server+"/api/v1/face/data/flowback-query" # 用于登机口，安检口人员回查功能
        self.api_v1_data_flight_query = self.host + self.data_platform_server + "/api/v1/data/flight/query"     #数据平台航班查询
        self.api_v1_data_flight_activate = self.host + self.data_platform_server + "/api/v1/data/flight/activate"   #数据平台航班激活
        self.api_v1_face_security_manual_optcheck = self.host + self.anjian_server + "/api/v1/face/security/manual-optcheck"  # 安检口人工放行
        self.api_anjian1_1 = self.host+self.anjian_server+"/api/v1/face/security/check"  # 安检1：1人脸验证
        self.api_v1_face_review_self_check = self.host+self.review_server+"/api/v1/face/review/self-check"  # 自助闸机复核接口

    def api_security_ticket_check(self,
                                  reqId=get_uuid(),
                                  gateNo="",
                                  deviceId="",
                                  cardType="0",
                                  idCard="",
                                  nameZh="nameZh",
                                  nameEn="nameEn",
                                  age=None,
                                  sex=None,
                                  birthDate="",
                                  address="重庆市",
                                  certificateValidity="20120101-20230202",
                                  nationality="CHina",
                                  ethnic="汉族",
                                  contactWay="0123456789",
                                  cardPhoto="",
                                  fId=get_uuid()
                                  ):
        """2.3.14自助验证闸机A门接口（二期)"""
        body = {"reqId": reqId,
                "gateNo": gateNo,
                "deviceId": deviceId,
                "cardType": cardType,
                "idCard": idCard,
                "nameZh": nameZh,  # 非必填
                "nameEn": nameEn,  # 非必填
                "age": age,  # 非必填
                "sex": sex,  # 非必填
                "birthDate": birthDate,
                "address": address,  # 非必填
                "certificateValidity": certificateValidity,
                "nationality": nationality,  # 非必填
                "ethnic": ethnic,  # 非必填
                "contactWay": contactWay,  # 非必填
                "cardPhoto": cardPhoto,
                "fId": fId
                }
        # print(body)
        # print(self.get_headers("/api/v1/face/security/ticket-check"))
        res = requests.post(url=self.A_security_ticket_check,
                            json=body,
                            headers=self.get_headers("/api/v1/face/security/ticket-check"),
                            verify=self.certificate)
        res.close()
        return res

    def api_face_security_face_check(self,
                                     reqId=get_uuid(),
                                     gateNo="",
                                     deviceId="",
                                     cardType="",
                                     idCard="",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age="",
                                     sex="",
                                     birthDate="",
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto="",
                                     sceneFeature="",
                                     cardPhoto="",
                                     cardFeature="",
                                     largePhoto="",
                                     facePst="",        #非必须，left,top,right,bottom  facePst和properyFeature必须至少传一个
                                     properyFeature=""  #非必填,属性特征(前端不提取属性特征，由服务器根据largePhoto+facePst自行提取)会检测口罩
                                     ):
        """2.3.15自助验证闸机B门接口（二期）"""
        body = {"reqId": reqId,
                "gateNo": gateNo,
                "deviceId": deviceId,
                "cardType": cardType,
                "idCard": idCard,
                "nameZh": nameZh,  # 非必填
                "nameEn": nameEn,  # 非必填
                "age": age,  # 非必填
                "sex": sex,  # 非必填
                "birthDate": birthDate,
                "address": address,  # 非必填
                "certificateValidity": certificateValidity,
                "nationality": nationality,  # 非必填
                "ethnic": ethnic,  # 非必填
                "contactWay": contactWay,  # 非必填
                "scenePhoto": scenePhoto,
                "sceneFeature": sceneFeature,
                "cardPhoto": cardPhoto,
                "cardFeature": cardFeature,
                "largePhoto":largePhoto, # 非必填
                "facePst":facePst,  # 非必填left,top,right,bottom
                "properyFeature":properyFeature #非必填,属性特征
                }
        # print(body)
        # print(self.get_headers("/api/v1/face/security/face-check"))
        res = requests.post(url=self.B_security_face_check,
                            json=body,
                            headers=self.get_headers("/api/v1/face/security/face-check"),
                            verify=self.certificate)
        res.close()
        return res

    def api_anjian(self,
                   anjiangateNo="T1AJ1",
                   anjiandeviceId="T1AJ001",
                   cardType=0,
                   idCard="300238199312134390",
                   nameZh="铁塔",
                   nameEn="CHENKEYUN",
                   age=25,
                   sex=1,
                   birthDate=get_birthday("300238199312134390"),
                   address="重庆市大竹林街道",
                   certificateValidity="20081010-长期",# 时间yyyymmdd或者长期(起-止)
                   nationality="中国",
                   ethnic="汉族",
                   scenePhoto="204.jpg",
                   sceneFeature="",
                   cardPhoto="204.jpg",
                   cardFeature="",
                   largePhoto="",
                   facePst="",  #非必填,left,top,right,bottom    1.largePhoto+facePst  2.properyFeature二选一传
                   properyFeature=""  #非必填,属性特征(前端不提取属性特征，由服务器根据largePhoto+facePst自行提取)不检测口罩，只用于判断年龄和性别
                   ):
        """安检1：1人脸验证"""
        body = {"reqId": get_uuid(),
                "gateNo": anjiangateNo,
                "deviceId": anjiandeviceId,
                "cardType": cardType,  # 证件类型 int
                "idCard": idCard,
                "nameZh": nameZh,
                "nameEn": nameEn,
                "age": age,  # int
                "sex": sex,  # int
                "birthDate": birthDate,
                "address": address,
                 "certificateValidity": certificateValidity,  # 时间yyyymmdd或者长期(起-止)
                 "nationality": nationality,
                 "ethnic": ethnic,
                 "contactWay": "18680946659",
                 "scenePhoto": scenePhoto,
                 "sceneFeature": sceneFeature,
                 "cardPhoto": cardPhoto,
                 "cardFeature": cardFeature,
                 "largePhoto":largePhoto,
                 "facePst": facePst,  # left,top,right,bottom
                 "properyFeature": properyFeature  # 属性特征
                }
        # print(self.get_headers("/api/v1/face/security/check"))
        # print(get_uuid())
        res = requests.post(url=self.api_anjian1_1,
                            json=body,
                            headers=self.get_headers("/api/v1/face/security/check"),
                            verify=self.certificate)
        res.close()
        return res

    def api_face_review_self_check(self,
                                   reqid=get_uuid(),
                                   gateno="",
                                   deviceid="",
                                   scenephoto="",
                                   scenefeature=""):
        """2.3.16 自助闸机复核接口（二期）"""
        # print(self.get_headers("/api/v1/face/review/self-check"))
        # print(self.api_v1_face_review_self_check)
        body = {"reqId": reqid,
                "gateNo": gateno,
                "deviceId": deviceid,
                "scenePhoto": scenephoto,
                "sceneFeature": scenefeature}
        res = requests.post(url=self.api_v1_face_review_self_check,
                            json=body,
                            headers=self.get_headers("/api/v1/face/review/self-check"),
                            verify=self.certificate)
        res.close()
        return res

    def api_face_review_check(self,
                              reqId=get_uuid(),
                              gateNo="",
                              deviceId="",
                              scenePhoto="",
                              sceneFeature=""):
        """2.3.6复核口服务器接口（二期优化）"""
        body = {"reqId": reqId,
                "gateNo": gateNo,
                "deviceId": deviceId,
                "scenePhoto": scenePhoto,
                "sceneFeature": sceneFeature}
        res = requests.post(url=self.api_v1_face_review_check,
                            headers=self.get_headers("/api/v1/face/review/check"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_face_review_manual_check(self,
                                     reqId=get_uuid(), gateNo="", deviceId="", scenePhoto="", cardNo="",
                                     passengerName="", passengerEnglishName="", securityStatus="",
                                     securityPassTime="", securityGateNo="", securityDeviceNo="",
                                     flightNo="", boardingNumber="",
                                     sourceType="",flightDay="",seatId=""):
        """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
        body = {"reqId": reqId,
                "gateNo": gateNo,
                "deviceId": deviceId,
                "scenePhoto": scenePhoto,  # 否 现场照base64编码，有现场照就上传现场照
                "cardNo": cardNo,
                "passengerName": passengerName,
                "passengerEnglishName": passengerEnglishName,
                "securityStatus": securityStatus,
                "securityPassTime": securityPassTime,
                "securityGateNo": securityGateNo,  # 否
                "securityDeviceNo": securityDeviceNo,  # 否
                "flightNo": flightNo,
                "boardingNumber": boardingNumber,
                "sourceType": sourceType,
                "flightDay":flightDay,
                "seatId":seatId
                }
        res = requests.post(url=self.api_v1_face_review_manual_check,
                            headers=self.get_headers("/api/v1/face/review/manual-check"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_face_security_manual_check(self,
                                       reqId=get_uuid(),
                                       flightNo="HU002",
                                       faceImage="",
                                       gateNo="T1AJ1",
                                       deviceCode="T1AJMM007",
                                       boardingNumber="010",
                                       seatId="",
                                       startPort="HET",
                                       flightDay="1",
                                       faceFeature="",
                                       kindType=0,                  # 类型：0：刷票 1：刷票放行
                                       largePhoto="",
                                       isFocus=0     #是否标记为布控人员  1-标记
                                       ):
        """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "faceImage": faceImage,
                "gateNo": gateNo,
                "deviceCode": deviceCode,
                "boardingNumber": boardingNumber,
                "seatId": seatId,
                "startPort": startPort,
                "flightDay": flightDay,
                "faceFeature": faceFeature,
                "kindType": kindType,
                "largePhoto":largePhoto,
                "isFocus":isFocus
                }
        # print(self.get_headers("/api/v1/face/security/manual-check"))
        res = requests.post(url=self.api_v1_face_security_manual_check,
                            headers=self.get_headers("/api/v1/face/security/manual-check"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_face_transfergate_ticket_collect(self,
                                             reqId=get_uuid(),
                                             flightNo="test006",
                                             faceImage="",
                                             deviceCode="T1ZZ002",
                                             gateNo="",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay="20181225",   # 传Dd
                                             faceFeature="",
                                             sourceType=0): #0-中转；1-经停；3-中转放行；4-经停放行
        """2.3.9中转通道接口（一期二阶段）2019.12.23废弃"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "faceImage": faceImage,
                "gateNo": gateNo,
                "deviceCode": deviceCode,
                "boardingNumber": boardingNumber,
                "seatId": seatId,
                "startPort": startPort,
                "flightDay": flightDay,    # DD
                "faceFeature": faceFeature,
                "sourceType": sourceType
                }
        res = requests.post(url=self.api_v1_face_transfergate_ticket_collect,
                            headers=self.get_headers("/api/v1/face/transfergate/ticket-collect"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_face_transfergate_face_collect(self,
                                             reqId=get_uuid(),
                                             flightNo="test006",
                                             faceImage="",
                                             faceFeature="",
                                             deviceCode="T1ZZ002",
                                             gateNo="",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay="20181225",   # 传Dd
                                             sourceType=0,    #0,中转；1，经停；2、备降采集；3、中转人工放行；4、经停人工放行；5、备降人工放行 6、经停证件采集（废弃）
                                             endPort="",
                                             cardId="",       #非必须  sourceType为6-经停证采集必给
                                             nameZh="",       #非必须  sourceType 为6-经停证采集必给
                                             mainFlightNo="", #非必须  主航班
                                             cardPhoto="",    #非必须  身份证件照base64编码
                                             cardFeature="",  #非必须  证件照特征base64
                                             largePhoto="",   #非必须  大图（口罩检测用）
                                             facePst=""       #非必须  人脸坐标（口罩检测用）
                                           ):
        """2.3.9中转通道接口（无特征传入）（二期）"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "faceImage": faceImage,
                "faceFeature":faceFeature,
                "gateNo": gateNo,
                "deviceCode": deviceCode,
                "boardingNumber": boardingNumber,
                "seatId": seatId,
                "startPort": startPort,
                "flightDay": flightDay,    # DD
                "sourceType": sourceType,
                "endPort":endPort,
                "cardId":cardId,  # 非必须  sourceType为6-经停证采集必给
                "nameZh":nameZh,  # 非必须  sourceType 为6-经停证采集必给
                "mainFlightNo":mainFlightNo,  # 非必须  主航班
                "cardPhoto":cardPhoto,  # 非必须  身份证件照base64编码
                "cardFeature":cardFeature,  # 非必须  证件照特征base64
                "largePhoto":largePhoto,  # 非必须  大图（口罩检测用）
                "facePst":facePst
        }
        # print(body)
        res = requests.post(url=self.api_v1_face_transfergate_face_collect,
                            headers=self.get_headers("/api/v1/face/transfergate/face-collect"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res


    def api_face_notice_cratelib(self,
                                 reqId=get_uuid(),
                                 flightNo="DL04462",
                                 date="20190121",
                                 boardingGate="14",
                                 deviceCode="T1DJ001",
                                 number=200,
                                 outTime=get_flight_out_time(1)
                                 ):
        """登机口复核建库通知接口"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "date": date,
                "boardingGate": boardingGate,
                "deviceCode": deviceCode,
                "number": number,
                "outTime": outTime
                }

        res = requests.post(url=self.api_v1_face_notice_crateLib,
                            headers=self.get_headers("/api/v1/face/notice/crateLib"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_face_boarding_review_check(self, reqId=get_uuid(),
                                faceImage="",
                                faceFeature="",
                                deviceCode="T1DJ001",
                                boardingGate="14",
                                gateNo="07",
                                flightNo="DL04462",
                                flightDay="20190417"   # （yyyyMMdd）
                                # faceInfo={"bottom": 11,
                                #           "top": 33,
                                #           "right": 55,
                                #           "left": 66 }
                                ):
        """2.3.12登机口复核接口（二期优化）"""
        body = {"reqId": reqId,
                "faceImage": faceImage,
                "faceFeature": faceFeature,
                "deviceCode": deviceCode,
                "boardingGate": boardingGate,
                "flightNo": flightNo,
                "flightDay": flightDay,
                "gateNo":gateNo,
                "isVipChannel":0,
                # "faceInfo":faceInfo
                }
        res = requests.post(url=self.api_v1_face_boarding_check,
                            #url="http://172.18.2.28:11015/api/v1/face/boarding/check",
                            headers=self.get_headers("/api/v1/face/boarding/check"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_face_boarding_library_check(self,
                                        reqId=get_uuid(),
                                        flightNo="",
                                        date="",
                                        boardingGate="",
                                        deviceCode="",
                                        gateNo=""):
        """2.3.12登机口建库人数查询接口（二期）"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "date": date,
                "boardingGate": boardingGate,
                "deviceCode": deviceCode,
                "gateNo": gateNo}
        res = requests.post(url=self.api_v1_face_boarding_library_check,
                            headers=self.get_headers("/api/v1/face/boarding/library-check"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res.text

    def api_face_boarding_manual_check(self,
                                       reqId=get_uuid(),
                                       flightNo="",
                                       date="",
                                       boardingGate="",
                                       deviceCode="",
                                       gateNo="",
                                       cardId="",
                                       scenePhoto="",
                                       sourceType="",
                                       passengerName="",
                                       boardingNumber="",
                                       seatId=""        #座位号
                                       ):
        """2.3.13登机口人工放行、报警接口（二期）"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "date": date,
                "boardingGate": boardingGate,
                "deviceCode": deviceCode,
                "gateNo": gateNo,
                "cardId": cardId,
                "scenePhoto": scenePhoto,
                "sourceType": sourceType,  # 0-放行，1-报警
                "passengerName": passengerName,
                "boardingNumber": boardingNumber,
                "seatId":seatId}
        res = requests.post(url=self.api_v1_face_boarding_manual_check,
                            headers=self.get_headers("/api/v1/face/boarding/manual-check"),
                            json=body,
                            verify=self.certificate)
        res.close()
        # print(body)
        return res

    def api_face_data_flowback_query(self,
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo="",
                                     flightDay="",   # 航班dd
                                     boardingNumber="",
                                     isFuzzyQuery=0,
                                     seatId=""
                                     # **kwargs
                                     ):
        """2.3.17 人员回查-安检、登机口接口（二期）"""
        # if "seatId" in kwargs.keys():
        #     body = {"reqId": reqId,
        #             "cardId": cardId,  # 否
        #             "flightNo": flightNo,  # 否
        #             "flightDay": flightDay,  # 否
        #             "boardingNumber": boardingNumber,
        #             "isFuzzyQuery" : isFuzzyQuery,
        #             "seatId":kwargs["seatId"]     #值为INF表示婴儿票
        #             }
        # else:
        #     body = {"reqId": reqId,
        #             "cardId": cardId,  # 否
        #             "flightNo": flightNo,  # 否
        #             "flightDay": flightDay,  # 否
        #             "boardingNumber": boardingNumber,  # 否
        #             "isFuzzyQuery": isFuzzyQuery
        #
        # print(body)

        body = {"reqId": reqId,
                "cardId": cardId,  # 否
                "flightNo": flightNo,  # 否
                "flightDay": flightDay,  # 否
                "boardingNumber": boardingNumber,
                "isFuzzyQuery" : isFuzzyQuery,
                "seatId":seatId     #值为INF表示婴儿票
                }
        print(body)
        print(self.api_v1_face_data_flowback_query)
        
        res = requests.post(url=self.api_v1_face_data_flowback_query,
                            headers=self.get_headers("/api/v1/face/data/flowback-query"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_face_security_manual_optcheck(self,
                                          reqId=get_uuid(),
                                          gateNo="",
                                          deviceId="",
                                          cardType="",
                                          idCard="",
                                          nameZh="",
                                          nameEn="",
                                          age="",
                                          sex="",
                                          birthDate="",
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto="",
                                          sceneFeature="",
                                          cardPhoto="",
                                          cardFeature="",
                                          largePhoto=""):
        """2.3.17安检口人工放行接口（二期）"""
        body = {"reqId": reqId,
                "gateNo": gateNo,
                "deviceId": deviceId,
                "cardType": cardType,
                "idCard": idCard,
                "nameZh": nameZh,
                "nameEn": nameEn,
                "age": age,
                "sex": sex,
                "birthDate": birthDate,
                "address": address,
                "certificateValidity": certificateValidity,
                "nationality": nationality,
                "ethnic": ethnic,
                "contactWay": contactWay,
                "scenePhoto": scenePhoto,
                "sceneFeature": sceneFeature,
                "cardPhoto": cardPhoto,
                "cardFeature": cardFeature,
                "largePhoto":largePhoto}
        res = requests.post(url=self.api_v1_face_security_manual_optcheck,
                            headers=self.get_headers("/api/v1/face/security/manual-optcheck"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res


    def api_face_boarding_start(self,
                                 reqId=get_uuid(),
                                 flightNo="test006",
                                 boardingGate="",
                                 deviceCode="T1ZZ002",
                                 gateNo="",
                                 flightDay=""
                                 ):
        """2.3.14调度系统开始登机（人工开始登机）（二期）"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "gateNo": gateNo,
                "deviceCode": deviceCode,
                "boardingGate":boardingGate,
                "flightDay": flightDay
                }
        res = requests.post(url=self.host + self.jms_server + "/api/v1/face/boarding/start",
                            headers=self.get_headers("/api/v1/face/boarding/start"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_face_notice_boarding_start(self,
                                 reqId=get_uuid(),
                                 flightNo="test006",
                                 threeFlightNo="test006",
                                 gateNo="T1DJ1",
                                 flightDay=""     #YYYY-MM-DD
                                 ):
        """2.3.14开始登机（内部使用，不对外）"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "threeFlightNo":threeFlightNo,
                "gateNo": gateNo,
                "flightDay": flightDay
                }
        res = requests.post(url=self.host + "boardinggate-server/api/v1/face/notice/boarding/start",
                            headers=self.get_headers("/api/v1/face/notice/boarding/start"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res



    def api_face_boarding_finish(self,
                                 reqId=get_uuid(),
                                 flightNo="test006",
                                 boardingGate="",
                                 deviceCode="T1ZZ002",
                                 gateNo="",
                                 flightDay=""         #YYYY-MM-DD
                                 ):
        """2.3.14调度系统结束登机（人工结束登机）（二期）"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "gateNo": gateNo,
                "deviceCode": deviceCode,
                "boardingGate":boardingGate,
                "flightDay": flightDay
                }
        res = requests.post(url=self.host + self.jms_server + "/api/v1/face/boarding/finish",
                            headers=self.get_headers("/api/v1/face/boarding/finish"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_face_boarding_strange(self,
                                 reqId=get_uuid(),
                                 flightNo="test006",
                                 boardingGate="",
                                 deviceCode="T1ZZ002",
                                 gateNo="",
                                 flightDay=""               #YYYY-MM-DD
                                 ):
        """2.3.16调度系统其余航班登机（人工改变登机口）（二期）"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "gateNo": gateNo,
                "deviceCode": deviceCode,
                "boardingGate":boardingGate,
                "flightDay":flightDay
                }
        res = requests.post(url=self.host + self.jms_server + "/api/v1/face/boarding/strange",
                            headers=self.get_headers("/api/v1/face/boarding/strange"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_face_boarding_flightplan(self,
                                  reqId=get_uuid(),
                                  boardingGate=""
                                  ):
        """2.3.17调度系统拉取航班计划（二期）"""
        body = {"reqId": reqId,
                "boardingGate": boardingGate
                }
        res = requests.post(url=self.host + self.jms_server + "/api/v1/face/boarding/flightplan",
                            headers=self.get_headers("/api/v1/face/boarding/flightplan"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_data_flight_query(self,
                              reqId=get_uuid(),
                              flightDate="",
                              flightNo=""
                              ):
        """数据平台航班查询"""
        body = {"reqId": reqId,
                "flightDate": flightDate,
                "flightNo":flightNo
                }
        res = requests.post(url=self.api_v1_data_flight_query,
                            headers=self.get_headers("/api/v1/data/flight/query"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_data_flight_activate(self,
                                 reqId=get_uuid(),
                                 flightDate="",      #yyyyMMdd
                                 flightNo=""
                                 ):
        """数据平台航班激活"""
        body = {"reqId": reqId,
                "flightDate": flightDate,
                "flightNo":flightNo
                }
        res = requests.post(url=self.api_v1_data_flight_activate,
                            headers=self.get_headers("/api/v1/data/flight/activate"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_v1_face_boarding_queryFlights(self,
                                          reqId=get_uuid(),
                                          flightNo=""
                                          ):
        """2.3.26	调度系统航班查询"""
        body = {"reqId": reqId,
                "flightNo": flightNo
                }
        res = requests.post(url=self.host + self.jms_server + "/api/v1/face/boarding/queryFlights",
                            headers=self.get_headers("/api/v1/face/boarding/queryFlights"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_v1_face_recognition_info(self,
                                     reqId=get_uuid(),
                                     channelCode="T1PX1",
                                     deviceId="T1PX001",
                                     fid="",
                                     faceImg="",
                                     faceFeature="",
                                     **kwargs
                                     ):
        '''2.3.25 旅客航班信息屏幕引导'''
        if "faceInfos" in kwargs.keys():
            body = {"reqId": reqId,
                    "channelCode": channelCode,
                    "deviceId": deviceId,
                    "faceInfos":kwargs["faceInfos"]
                    }
        else:
            body = {"reqId":reqId,
                    "channelCode":channelCode,
                    "deviceId":deviceId,
                    "faceInfos":[{"fid":fid,
                                  "faceImg":faceImg,
                                  "faceFeature":faceFeature
                                }]
                    }
        # print(self.get_headers("/api/v1/face/recognition/info"))
        res = requests.post(url=self.host + self.screen_guider + "/api/v1/face/recognition/info",
                            headers=self.get_headers("/api/v1/face/recognition/info"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_face_abnormal_passenger_query(self,
                                          reqId=get_uuid(),
                                          pageNum=1,               #必须，分页页码
                                          pageSize=20,          #必须，分页长度
                                          isCount=1,            #必须，为1时查询总记录数
                                          searchTime=""         #非必须，第一次的搜索时间，yyyyMMddHHmmss
                                          ):
        """2.4.20.1数据平台异常记录查询"""
        body = {"reqId": reqId,
                "pageNum":pageNum,
                "pageSize":pageSize,
                "isCount":isCount,
                "searchTime":searchTime
                }
        res = requests.post(url=self.host + self.data_platform_server + "/api/v1/face/abnormal-passenger/query",
                            headers=self.get_headers("/api/v1/face/abnormal-passenger/query"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_face_lib_recognize_n_query(self,
                                      reqId=get_uuid(),  #必须
                                      img=""             #必须,base64图片编码
                                      ):
        """2.4.21.1 底库TOPN查询"""
        body = {"reqId": reqId,
                "img":img
                }
        res = requests.post(url=self.host + self.data_platform_server + "/api/v1/face/lib-recognize/n-query",
                            headers=self.get_headers("/api/v1/face/lib-recognize/n-query"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_v1_face_boarding_passenger_query(self,
                                          reqId=get_uuid(),
                                          flightNo="",               #必须，航班号
                                          date="",          #必须，日期yyyy-MM-dd
                                          queryType=1,            #必须，查询类型：0-建库旅客查询；1-已登机旅客查询；2-未登机旅客查询; 3-全查询
                                          pageNum=1,         #必须，页码
                                          pageSize=20,      #必须，分页长度
                                          isCount=1,         #必须，为1时查询总记录数
                                          gateNo="",
                                          boardingGate=""
                                          ):
        """2.3.13登机口建库、已登机、未登机旅客查询接口（20191105）"""
        body = {"reqId": reqId,
                "flightNo":flightNo,
                "date":date,
                "queryType":queryType,
                "pageNum":pageNum,
                "pageSize":pageSize,
                "isCount":isCount,
                "gateNo":gateNo,
                "boardingGate":boardingGate
                }
        # print(self.get_headers("/api/v1/face/boarding/passenger-query"))
        # print(body)
        res = requests.post(url=self.host + self.boardinggate_server + "/api/v1/face/boarding/passenger-query",
                            #url="http://172.18.2.28:11015/api/v1/face/boarding/passenger-query",
                            headers=self.get_headers("/api/v1/face/boarding/passenger-query"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_v1_face_boarding_active(self,
                                  reqId=get_uuid(),
                                  flightNo="",               #必须，航班号
                                  gateNo="",          #必须，登机口编码
                                  boardingGate="",            #必须，登机口
                                  deviceCode="",         #必须，设备编码
                                  flightDay=""          #必须,日期yyyy-MM-dd
                                  ):
        """2.3.27 调度系统异常航班激活"""
        body = {"reqId": reqId,
                "flightNo":flightNo,
                "gateNo":gateNo,
                "boardingGate":boardingGate,
                "deviceCode":deviceCode,
                "flightDay":flightDay
                }
        res = requests.post(url=self.host + self.jms_server + "/api/v1/face/boarding/active",
                            headers=self.get_headers("/api/v1/face/boarding/active"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_v1_face_boarding_lib_delete(self,
                                  reqId=get_uuid(),
                                  flightNo="",               #必须，航班号
                                  gateNo="",          #必须，登机口编码
                                  boardingGate="",            #必须，登机口
                                  deviceCode="",         #必须，设备编码
                                  id=""          #必须,日期yyyy-MM-dd
                                  ):
        """2.3.28 底库删除接口（新增）"""
        body = {"reqId": reqId,
                "flightNo":flightNo,
                "gateNo":gateNo,
                "boardingGate":boardingGate,
                "deviceCode":deviceCode,
                "id":id
                }
        res = requests.post(url=self.host + self.boardinggate_server + "/api/v1/face/boarding/lib-delete",
                            headers=self.get_headers("/api/v1/face/boarding/lib-delete"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_v1_face_boarding_cancel(self,
                                  reqId=get_uuid(),
                                  flightNo="",               #必须，航班号
                                  gateNo="",          #必须，登机口编码
                                  boardingGate="",            #必须，登机口
                                  deviceCode="",         #必须，设备编码
                                  flightDay=""          #必须,日期yyyy-MM-dd
                                  ):
        """2.3.29 调度系统人工取消航班"""
        body = {"reqId": reqId,
                "flightNo":flightNo,
                "gateNo":gateNo,
                "boardingGate":boardingGate,
                "deviceCode":deviceCode,
                "flightDay":flightDay
                }
        res = requests.post(url=self.host + self.jms_server + "/api/v1/face/boarding/cancel",
                            headers=self.get_headers("/api/v1/face/boarding/cancel"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_v1_face_boarding_ticket_check(self,
                                          reqId=get_uuid(),      # 必须  string 32位UUID
                                          deviceCode="",         # 必须  string 设备编号
                                          boardingGate="",       # 必须  string 登机口编号
                                          gateNo="",             # 必须  string 登机口区域编号
                                          flightNo="",           # 必须  string 航班号
                                          flightDay="",          # 必须  string 航班日（yyyyMMdd）
                                          IsVipChannel=0,        # 非必须integer 是否贵宾通道（新增）1-是 0-不是
                                          boardingNumber="",     # 非必须string 登机序列号
                                          seatId="",             # 非必须string 座位号
                                          mainFlightNo="",       # 非必须string 主航班号
                                          cardId="",             # 非必须string 身份证号
                                          cardType="",           # 非必须string 证件类型
                                          nameZh="",             # 非必须string 旅客姓名
                                          sex=""                 # 非必须string 旅客性别
                                          ):
        """2.3.30 登机口刷票登机接口（新增）"""
        body = {"reqId":reqId,
                "deviceCode":deviceCode,
                "boardingGate":boardingGate,
                "gateNo":gateNo,
                "flightNo":flightNo,
                "flightDay":flightDay,
                "IsVipChannel":IsVipChannel,
                "boardingNumber":boardingNumber,
                "seatId":seatId,
                "mainFlightNo":mainFlightNo,
                "cardId":cardId,
                "cardType":cardType,
                "nameZh":nameZh,
                "sex":sex
                }
        # print(body)
        api_url = "/api/v1/face/boarding/ticket-check"
        res = requests.post(url=self.host + self.boardinggate_server + api_url,
                            headers=self.get_headers(api_url),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_v1_face_boarding_weight_upload(self,
                                           reqId=get_uuid(),   # 必须string 32位UUID
                                           deviceCode="",      # 非必须string 设备编号
                                           boardingGate="",    # 必须string 登机口编号
                                           gateNo="",          # 非必须string 登机口区域编号
                                           flightNo="",        # 必须string 航班号
                                           flightDay="",       # 必须string 航班日（yyyyMMdd）
                                           boardingNumber="",  # 非必须string 登机序列号（证件信息和票信息二选一）
                                           seatId="",          # 非必须string 座位号
                                           cardId="",          # 非必须string 证件信息和票信息二选一
                                           cardType=0,         # 非必须integer 证件类型
                                           nameZh="",          # 非必须string 中文姓名
                                           weight=0,           # 必须number 旅客及行李重量
                                          ):
        """2.3.31 登机口重量采集接口（新增）"""
        body = {"reqId":reqId,
                "deviceCode":deviceCode,
                "boardingGate":boardingGate,
                "gateNo":gateNo,
                "flightNo":flightNo,
                "flightDay":flightDay,
                "boardingNumber":boardingNumber,
                "seatId":seatId,
                "cardId":cardId,
                "cardType":cardType,
                "nameZh":nameZh,
                "weight":weight
                }
        api_url = "/api/v1/face/boarding/weight/upload"
        res = requests.post(url=self.host + self.boardinggate_server + api_url,
                            headers=self.get_headers(api_url),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res

    def api_v1_face_boarding_weight_query(self,
                                          reqId=get_uuid(),   # 必须string 32位UUID
                                          flightNo="",        # 非必须string 航班号
                                          flightDay="",       # 必须string 航班日（yyyyMMdd）
                                          pageNum=1,          # 必须integer 页码
                                          pageSize=20,        # 必须integer 查询条数
                                          isCount=1           # 非必须integer 为1查询总数
                                         ):
        """2.3.31 登机口重量采集查询接口（新增）"""
        body = {"reqId":reqId,
                "flightNo":flightNo,
                "flightDay":flightDay,
                "pageNum":pageNum,
                "pageSize":pageSize,
                "isCount":isCount
                }
        # print(body)
        api_url = "/api/v1/face/boarding/weight/query"
        res = requests.post(url=self.host + self.data_platform_server + api_url,
                            headers=self.get_headers(api_url),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res




if __name__ == '__main__':
    # 数据准备
    # bdno = str(random.randint(1, 999))  # 登机序号
    bdno = "169"  # 登机序号
    # flight_no = produce_flight_number()  # 航班号
    flight_no = "AB0002"  # 航班号
    feature_num = int(bdno)  # 照片特征文件名，每次+2
    idcard = get_random_id_number()  # 随机身份证号码
    # idcard = "511401199010211111"
    date = produce_flight_date()  # 当天日期YYYYMMDD
    main_path = "D:/pre_data/new_feature"
    main_path_old = "D:/pre_data/old_feature"
    cardPhoto = to_base64(main_path + "/picture/%s.jpg" % feature_num)  # 身份证照片
    facePst = read_feature(main_path + "/picture_facePst/%s.txt" % feature_num)  # 读取属性特征坐标
    cardPhoto_mouth_muffle = to_base64(main_path + "/mouth_muffle/image/1.jpg")  # 带口罩图片
    feature_8k = read_feature(main_path_old + "/picture8k/%s.txt" % feature_num)  # 读取8k特征
    feature_8k_other = read_feature(main_path_old + "/picture8k/%s.txt" %(feature_num+1))  # 读取8k特征
    feature_2k = read_feature(main_path_old + "/picture2k/%s.txt" % feature_num)  # 读取2k特征
    lk_cname = "周志喜%s" % bdno  # 中文姓名
    print("身份证号码:" + idcard + ",航班号:" + flight_no + ",登机序号:" + bdno)
    # res = AirportProcess().api_face_boarding_manual_check(flightNo="JD5572",
    #                                                        date=date,
    #                                                        boardingGate="04",
    #                                                        deviceCode="T1AF003",
    #                                                        gateNo="T1AF3",
    #                                                        cardId="330602198201104310",
    #                                                        scenePhoto=cardPhoto,
    #                                                        sourceType=0,
    #                                                        passengerName="",
    #                                                        boardingNumber="",
    #                                                        seatId="INF"  # 座位号
    #                                                        )
    # print(res.json())
    # for i in range(400):
    #     # 中转通道接口（无特征传入）
    #     res = AirportProcess().api_face_transfergate_face_collect(flightNo=flight_no,
    #                                                               faceImage=cardPhoto,
    #                                                               faceFeature=feature_8k,
    #                                                               deviceCode="T1ZZ002",
    #                                                               gateNo="T1AF1",
    #                                                               seatId="",
    #                                                               startPort="HET",
    #                                                               boardingNumber="",
    #                                                               flightDay=date[-2:],  # 传Dd
    #                                                               sourceType=0,  # 0,中转；1，经停；2、备降采集；3、中转人工放行；4、经停人工放行；5、备降人工放行 6、经停证件采集（废弃）
    #                                                               endPort="",
    #                                                               cardId=str(i),  # 非必须  sourceType为6-经停证采集必给
    #                                                               nameZh="3",  # 非必须  sourceType 为6-经停证采集必给
    #                                                               mainFlightNo=flight_no,  # 非必须  主航班
    #                                                               cardPhoto=cardPhoto,  # 非必须  身份证件照base64编码
    #                                                               cardFeature=feature_8k,  # 非必须  证件照特征base64
    #                                                               largePhoto=cardPhoto,  # 非必须  大图（口罩检测用）
    #                                                               facePst=facePst  # 非必须  人脸坐标（口罩检测用）
    #                                                               )
    #     print(res.json())
    #登机口重量采集接口
    # res = AirportProcess().api_v1_face_boarding_weight_upload(deviceCode="123",  # 非必须string 设备编号
    #                                                            boardingGate="02",  # 必须string 登机口编号
    #                                                            gateNo="123",  # 非必须string 登机口区域编号
    #                                                            flightNo=flight_no,  # 必须string 航班号
    #                                                            flightDay=date,  # 必须string 航班日（yyyyMMdd）
    #                                                            boardingNumber="123",  # 非必须string 登机序列号（证件信息和票信息二选一）
    #                                                            seatId="123",  # 非必须string 座位号
    #                                                            cardId="",  # 非必须string 证件信息和票信息二选一
    #                                                            cardType=0,  # 非必须integer 证件类型
    #                                                            nameZh="123",  # 非必须string 中文姓名
    #                                                            weight=10,  # 必须number 旅客及行李重量
    #                                                            )
    # print(res.json())
    # print(type(res.json()))
    # 登机口重量采集查询接口
    res = AirportProcess().api_v1_face_boarding_weight_query(flightNo="CA8295",  # 非必须string 航班号
                                                              flightDay="20200420",  # 必须string 航班日（yyyyMMdd）
                                                              pageNum=1,  # 必须integer 页码
                                                              pageSize=20,  # 必须integer 查询条数
                                                              isCount=1  # 非必须integer 为1查询总数
                                                              )
    print("重量查询" + res.text)
    # # 登机口刷票登机
    # res = AirportProcess().api_v1_face_boarding_ticket_check(deviceCode="T3AF003",  # 必须  string 设备编号
    #                                                           boardingGate="04",  # 必须  string 登机口编号
    #                                                           gateNo="T3AF3",  # 必须  string 登机口区域编号
    #                                                           flightNo="AB0003",  # 必须  string 航班号
    #                                                           flightDay=date,  # 必须  string 航班日（yyyyMMdd）
    #                                                           IsVipChannel=0,  # 非必须integer 是否贵宾通道（新增）1-是 0-不是
    #                                                           boardingNumber="",  # 非必须string 登机序列号
    #                                                           seatId="",  # 非必须string 座位号
    #                                                           mainFlightNo="",  # 非必须string 主航班号
    #                                                           cardId="",  # 非必须string 身份证号
    #                                                           cardType="",  # 非必须string 证件类型
    #                                                           nameZh="",  # 非必须string 旅客姓名
    #                                                           sex=""  # 非必须string 旅客性别
    #                                                           )
    # print(res.json())
    # 人工结束登机
    # res = AirportProcess().api_face_boarding_finish(flightNo="MU5459",
    #                                                  boardingGate="04",
    #                                                  deviceCode="T1ZZ002",
    #                                                  gateNo="1",
    #                                                  flightDay="2020-04-20"  # YYYY-MM-DD
    #                                                  )
    # print(res.json())
    '''
    # 0-建库旅客查询；1-已登机旅客查询；2-未登机旅客查询
    res = AirportProcess().api_v1_face_boarding_passenger_query(flightNo="GT1004",  # 必须,航班号
                                                                date="2020-04-20",  # 必须,日期yyyy-MM-dd
                                                                queryType=1,  # 必须,查询类型：0-建库旅客查询；1-已登机旅客查询；2-未登机旅客查询
                                                                pageNum=1,  # 必须，分页页码
                                                                pageSize=20,  # 必须，分页长度b
                                                                isCount=1,  # 必须，为1返回总数
                                                                gateNo="",
                                                                boardingGate="04"
                                                                )
    print(res.json())
'''
    # 回查旅客信息
    res = AirportProcess().api_face_data_flowback_query(cardId="",
                                                        flightNo="CA8295",
                                                        flightDay="-1",  # 航班dd
                                                        boardingNumber="001",
                                                        isFuzzyQuery=1,  # 1-为模糊查询，非1为精确查询
                                                        seatId=""
                                                        )
    print("传入座位号回查" + res.text)

    # # 登机口复核
    # res = AirportProcess().api_face_boarding_review_check(faceImage=cardPhoto,
    #                                                        faceFeature=feature_2k,
    #                                                        deviceCode="T1DJ001",
    #                                                        boardingGate="04",
    #                                                        gateNo="07",
    #                                                        flightNo="DL04462",
    #                                                        flightDay="20190417"  # （yyyyMMdd）
    #                                                        )
    # print("登机口复核" + res.text)
    # 小闸机复核
    # res = AirportProcess().api_face_review_self_check(gateno="T1AF3",
    #                                                    deviceid="T1AF003",
    #                                                    scenephoto=to_base64(r"C:\Users\admin\Desktop\TIM图片20200420113404.jpg"),
    #                                                    scenefeature=read_feature(r"C:\Users\admin\Desktop\0.txt")
    #                                                   )
    # print(res.json())



