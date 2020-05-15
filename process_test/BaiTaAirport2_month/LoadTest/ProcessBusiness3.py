# coding:utf-8
from locust import HttpLocust,TaskSequence,task
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData import FlightNo,IdCard,PictureBase64One
from BaiTaAirport2_month.common.Log import MyLog
from BaiTaAirport2_month.msgQueue.Autosendlk import *
name = os.path.realpath(__file__).split("\\")[-1].split(".")[0]
log = MyLog(name=name)
""" 3.通道人工验票 --------->通道复核。对流程进行并发30测试，
检查各个接口状态返回的正确性，以及在压测期间，服务器的资源占用情况，并以数据汇总。
"""

"""操作步骤
1.值机1w个样本数据进行值机
2.对这个1w个样本数据从通道人工验票 --------->通道复核进行校验
3.全流程并发30，查验应用服务器资源使用情况以及mysql数据库服务器在Linux中使用情况
"""


class ProcessBusiness3(TaskSequence):

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
        e = None
        e1 = None
        index = random.randint(0, 9999)
        body = {"reqId": get_uuid(),
                "flightNo": FlightNo.Flight_no_list_1w[index],
                "faceImage": PictureBase64One.Base64Picture,
                "gateNo": "Process3",
                "deviceCode": "Process003",
                "boardingNumber": "001",
                "seatId": "001",
                "startPort": "HET",
                "flightDay": produce_flight_day(),
                "faceFeature": get_txt(shiwanli8k_features+"/"+str(index)+".txt")
                }
        # self.host + self.anjian_server + "/api/v1/face/security/manual-check"
        with self.client.post(url="/security-server/api/v1/face/security/manual-check",
                              json=body,
                              headers=AirportProcess().get_headers("/api/v1/face/security/manual-check"),
                              verify=False,
                              catch_response=True) as response:
            response.success()
            json_data = None
            try:
                json_data = json.loads(str(response.text))
                if json_data["status"] == 0:
                    a_statue = True
                else:
                    a_statue = False
            except Exception as e:
                a_statue = False
                log.logger.error("解析错误"+str(json_data)+str(e))
        if a_statue and b_statue:
            log.logger.info("通道人工验票 --------->通道复核成功,此时的索引为%d"%index)
        else:
            log.logger.info("通道人工验票 --------->通道复核失败,此时的索引为%d"%index)


class BehaviorP1(HttpLocust):
    task_set = ProcessBusiness3
    min_wait = 50
    max_wait = 100000
    host = "http://192.168.1.106:9091"


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    command1 = "c:"
    command2 = r"cd %s" % current_path
    command3 = r"locust -f ProcessBusiness3.py -P 8202 --web-host=127.0.0.1"
    os.system(command1)
    os.system(command2)
    os.system(command3)

