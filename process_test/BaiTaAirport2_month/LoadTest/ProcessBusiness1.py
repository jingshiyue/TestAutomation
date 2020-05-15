# coding:utf-8
from locust import HttpLocust,TaskSequence,task
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData import FlightNo,IdCard,PictureBase64One
from BaiTaAirport2_month.msgQueue.Autosendlk import *
import threading
"""（1）、值机（由于值机收MQ影响，先值机结束10W样本数据测试）----->A门闸机接口----->B门闸机接口------->复核小闸机接口  ，
对流程进行并发30，测试，检查各个接口状态返回的正确性，以及在压测期间，服务器的资源占用情况，并以数据汇总。
"""

"""操作步骤
1.值机1w个样本数据进行值机
2.对这个1w个样本数据从闸机A-闸机B-复核闸机进行校验
3.全流程并发30，查验应用服务器资源使用情况以及mysql数据库服务器在Linux中使用情况
"""


class ProcessBusiness1(TaskSequence):

    @staticmethod
    def build_zhiji():
        """进行1w个值机人员注册"""
        for i in range(0, 10000):
            send_lkxx(lk_IsInternation="0",
                      lk_bdno="001",
                      lk_cardid=IdCard.IdCard_list_1w[i],
                      lk_chkt="",
                      lk_cname="nametest",
                      lk_date=produce_flight_date(),
                      lk_desk=get_lk_desk(),
                      lk_ename="englishName",
                      lk_flight=FlightNo.Flight_no_list_1w[i],
                      lk_gateno="10",
                      lk_id=get_uuid(),
                      lk_inf=" ",
                      lk_insur="0",
                      lk_outtime=get_flight_out_time(),
                      lk_sex="1",
                      lk_vip="0")
            print("第%d个旅客注册完毕" % i)
        print("所有旅客全部值机完毕")

    @task
    def task_first(self):
        a_statue = None
        b_statue = None
        c_statue = None
        index = random.randint(0, 9999)
        body_zhaji_a = {"reqId": get_uuid(),
                        "gateNo": "T6AJ1",
                        "deviceId": "T6AJ001",
                        "cardType": 1,
                        "idCard": IdCard.IdCard_list_1w[index],
                        "nameZh": "nameZh",  # 非必填
                        "nameEn": "nameEn",  # 非必填
                        "age": get_age(IdCard.IdCard_list_1w[index]),  # 非必填
                        "sex": "0",  # 非必填
                        "birthDate": get_birthday(IdCard.IdCard_list_1w[index]),
                        "address": "重庆市",  # 非必填
                        "certificateValidity": "20160222-20220215",
                        "nationality": "China",  # 非必填
                        "ethnic": "汉族",  # 非必填
                        "contactWay": "123456789",  # 非必填
                        "cardPhoto": PictureBase64One.Base64Picture,  # 用同一人的照片的base64编码String
                        "fId": get_uuid()}
        with self.client.post(url="/security-server/api/v1/face/security/ticket-check",
                              json=body_zhaji_a,
                              headers=AirportProcess().get_headers("/api/v1/face/security/ticket-check"),
                              verify=False,
                              catch_response=True) as response:
            json_data_a = None
            try:
                json_data_a = json.loads(str(response.text))
                if json_data_a["result"] == 0:
                    response.success()
                    print(json_data_a)
                    a_statue = True
                elif json_data_a["result"] == 1:
                    response.failure("人票比对不成功")
                elif json_data_a["result"] == 2:
                    response.failure("身份证过期")
            except Exception as e:
                response.failure("解析错误"+str(json_data_a)+str(e))
        # time.sleep(1)

        # 开始进行 B门1：1验证
        body_zhaji_b = {"reqId": get_uuid(),
                        "gateNo": "T6AJ2",
                        "deviceId": "T6AJ002",
                        "cardType": 1,
                        "idCard": IdCard.IdCard_list_1w[index],
                        "nameZh": "nameZh",  # 非必填
                        "nameEn": "nameEn",  # 非必填
                        "age": get_age(IdCard.IdCard_list_1w[index]),  # 非必填
                        "sex": "0",  # 非必填
                        "birthDate": get_birthday(IdCard.IdCard_list_1w[index]),
                        "address": "重庆市",  # 非必填
                        "certificateValidity": "2015-2022",
                        "nationality": "Chin",  # 非必填
                        "ethnic": "汉族",  # 非必填
                        "contactWay": "0123456789",  # 非必填
                        "scenePhoto": PictureBase64One.Base64Picture,
                        "sceneFeature": get_txt(shiwanid8k_features+"/"+str(index)+".txt"),
                        "cardPhoto": PictureBase64One.Base64Picture,
                        "cardFeature": get_txt(shiwanid8k_features+"/"+str(index)+".txt")}
        with self.client.post(url="/security-server/api/v1/face/security/face-check",
                              json=body_zhaji_b,
                              headers=AirportProcess().get_headers("/api/v1/face/security/face-check"),
                              verify=False,
                              catch_response=True) as response1:
            json_data_b = None
            try:
                json_data_b = json.loads(str(response1.text))
                if json_data_b["result"] == 0:
                    b_statue = True
                    response1.success()
                elif json_data_b["result"] == 1:
                    b_statue = False
                    response1.failure("人证1比1比对失败")
            except Exception as e1:
                b_statue = False
                response1.failure("解析错误"+str(json_data_b)+str(e1))

        # time.sleep(3)
        # 开始进行闸机复核测试
        body_zhaji_c = {"reqId": get_uuid(),
                        "gateNo": "T6AJ3",
                        "deviceId": "T3AJ003",
                        "scenePhoto": PictureBase64One.Base64Picture,
                        "sceneFeature": get_txt(shiwanli2k_features+"/"+str(index)+".txt")}
        with self.client.post(url="/review-server/api/v1/face/review/self-check",
                              json=body_zhaji_c,
                              headers=AirportProcess().get_headers("/api/v1/face/review/self-check"),
                              verify=False,
                              catch_response=True) as response2:
            json_data_c = None
            try:
                json_data_c = json.loads(str(response2.text))
                if json_data_c["userInfo"] == None:
                    c_statue = False
                    response2.failure("复核失败，没有找到匹配的人脸")
                else:
                    if json_data_c["userInfo"]["cardNo"] == IdCard.IdCard_list_1w[index]:
                        response2.success()
                    else:
                        response2.failure("复核识别错误")
            except Exception as e2:
                c_statue = False
                response2.failure("解析错误"+str(json_data_c)+str(e2))

        if a_statue and b_statue and c_statue:
            print("index序号为的%d" % index+"自助闸机全流程成功")
        else:
            print("index序号为的%d" % index+"自助闸机全流程失败")


class BehaviorP1(HttpLocust):
    task_set = ProcessBusiness1
    min_wait = 50
    max_wait = 100000
    host = "http://192.168.1.106:9091"


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    command1 = "c:"
    command2 = r"cd %s" % current_path
    command3 = r"locust -f ProcessBusiness1.py -P 8200 --web-host=127.0.0.1"
    os.system(command1)
    os.system(command2)
    os.system(command3)

