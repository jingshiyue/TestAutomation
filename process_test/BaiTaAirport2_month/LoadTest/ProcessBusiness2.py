# coding:utf-8
from locust import HttpLocust,TaskSequence,task
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData import FlightNo,IdCard,PictureBase64One
from BaiTaAirport2_month.common.Log import MyLog
from BaiTaAirport2_month.msgQueue.Autosendlk import *
name = os.path.realpath(__file__).split("\\")[-1].split(".")[0]
log = MyLog(name=name)
""" 2.通道安检1：1 --------->通道复核。对流程进行并发30测试，
检查各个接口状态返回的正确性，以及在压测期间，服务器的资源占用情况，并以数据汇总。
"""

"""操作步骤
1.值机1w个样本数据进行值机
2.对这个1w个样本数据从通道安检1：1-通道复核进行校验
3.全流程并发30，查验应用服务器资源使用情况以及mysql数据库服务器在Linux中使用情况
"""


class ProcessBusiness2(TaskSequence):

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
        e1 = None
        index = random.randint(0, 9999)
        body1 = {"reqId": get_uuid(),
                 "gateNo": "Process2",
                 "deviceId": "Process002",
                 "cardType": 0,  # 证件类型 int
                 "idCard": IdCard.IdCard_list_1w[index],
                 "nameZh": "nameZh",
                 "nameEn": "nameEn",
                 "age": get_age(IdCard.IdCard_list_1w[index]),  # int
                 "sex": "0",  # int
                 "birthDate": get_birthday(IdCard.IdCard_list_1w[index]),
                 "address": "隋唐",
                 "certificateValidity": "20081010-20191206",  # 时间yyyymmdd或者长期(起-止)
                 "nationality": "China",
                 "ethnic": "汉族",
                 "contactWay": "18680946659",
                 "scenePhoto": PictureBase64One.Base64Picture,
                 "sceneFeature": get_txt(shiwanid8k_features+"/"+str(index)+".txt"),
                 "cardPhoto": PictureBase64One.Base64Picture,
                 "cardFeature": get_txt(shiwanid8k_features+"/"+str(index)+".txt"),
                 }
        with self.client.post(url="/security-server/api/v1/face/security/check",
                              json=body1,
                              headers=AirportProcess().get_headers("/api/v1/face/security/check"),
                              verify=False,
                              catch_response=True) as response:
            json_data = None
            try:
                json_data = json.loads(str(response.text))
                if json_data["result"] == 0:
                    a_statue = True
                    response.success()
                elif json_data["result"] == 1:
                    a_statue = False
                    response.failure("人证1：1比对失败")
            except Exception as e:
                a_statue = False
                response.failure("解析错误"+str(json_data)+str(e))
        # 开始进行复核
        time.sleep(2)
        body2 = {"reqId": get_uuid(),
                 "gateNo": "Process2",
                 "deviceId": "Process002",
                 "scenePhoto": PictureBase64One.Base64Picture,
                 "sceneFeature": get_txt(shiwanli2k_features+"/"+str(index)+".txt")}
        with self.client.post(url="/review-server/api/v1/face/review/check",
                              json=body2,
                              headers=AirportProcess().get_headers("/api/v1/face/review/check"),
                              verify=False,
                              catch_response=True) as response1:
            response1.success()
            json_data1 = None
            try:
                json_data1 = json.loads(str(response1.text))
                if json_data1["status"] == 0:
                    if json_data1[["result"]] == 0 and json_data1["userInfo"]["cardNo"] == IdCard.IdCard_list_1w[index]:
                        b_statue = True

                    else:
                        b_statue = False
                else:
                    b_statue = False
                    log.logger.warn("服务器内部错误")
            except Exception as e1:
                b_statue = False
        if a_statue and b_statue:
            log.logger.info("通道安检1：1 --------->通道复核成功,此时索引为%d" % index)
        else:
            log.logger.info("通道安检1：1 --------->通道复核失败,此时索引为%d" % index+str(e1))


class BehaviorP1(HttpLocust):
    task_set = ProcessBusiness2
    min_wait = 50
    max_wait = 100000
    host = "http://192.168.1.106:9091"


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    command1 = "c:"
    command2 = r"cd %s" % current_path
    command3 = r"locust -f ProcessBusiness2.py -P 8201 --web-host=127.0.0.1"
    os.system(command1)
    os.system(command2)
    os.system(command3)

