# coding:utf-8
from locust import HttpLocust, task, TaskSequence
from BaiTaAirport2_month.API.AirportProcess import *
import json
"""
（1）、底库为3000，对同一个进行并发30压力测试，并且传入的特征为最后一次注册后人员的特征，服务器响应时间小于1s，同时，返回状态正确
"""

"""操作步骤
1.通过刷票接口进行注册3000人作为底库
2.对注册的最后一人进行压测，
3.查看服务器响应时间和资源使用情况，以及服务器负载情况
"""


class TaskReview1N1(TaskSequence):
    @staticmethod
    def build_lib1():
        for i in range(0, 3000):
            res = AirportProcess().api_face_security_manual_check(reqId=get_uuid(),
                                                                  flightNo="flightno%d" % i,
                                                                  faceImage=to_base64(r"C:\chenkeyun\OtherFile\IDcard\0.jpg"),
                                                                  gateNo="T9AJ1",
                                                                  deviceCode="T9AJ001",
                                                                  boardingNumber="001",
                                                                  seatId="001",
                                                                  flightDay=produce_flight_day(),
                                                                  faceFeature=get_txt(shiwanid8k_features+"/"+str(i)+".txt"))
            print("第%d个完毕" % (i+1)+"\n"+res)
        print("数据底库造完")

    @task
    def first_task(self):
        # elf.host + self.review_server + "/api/v1/face/review/check"
        """进行通道复核"""
        body = {"reqId": get_uuid(),
                "gateNo": "T9AJ1",
                "deviceId": "T9AF001",
                "scenePhoto": to_base64(r"C:\chenkeyun\OtherFile\IDcard\0.jpg"),
                "sceneFeature": get_txt(shiwanid2k_features+"/"+str(2999)+".txt")}
        with self.client.post(url="/review-server/api/v1/face/review/check",
                              json=body,
                              headers=AirportProcess().get_headers("/api/v1/face/review/check"),
                              verify=False,
                              catch_response=True) as response:
            json_data = None
            try:
                json_data = json.loads(str(response.text))
                if json_data["result"] == 0 and json_data["userInfo"]["flightNumber"] == "flightno2999":
                    response.success()
                elif json_data["result"] == 0 and json_data["userInfo"]["flightNumber"] != "flightno2999":
                    response.failure("复核失败"+"\n"+str(json_data))
                elif json_data["result"] == 1:
                    response.failure("复核失败"+"\n"+str(json_data))
            except Exception as e:
                response.failure("解析失败"+str(json_data)+str(e))


class BehaviorReview1N1(HttpLocust):
    task_set = TaskReview1N1
    min_wait = 1000
    max_wait = 6000
    host = "http://192.168.1.106:9091"

if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    command1 = "c:"
    command2 = r"cd %s" % current_path
    command3 = r"locust -f review_1N1.py -P 8102 --web-host=127.0.0.1"
    os.system(command1)
    os.system(command2)
    os.system(command3)