# coding:utf-8
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture
from locust import HttpLocust,TaskSequence,task
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.common.Log import MyLog
name = os.path.realpath(__file__).split("\\")[-1].split(".")[0]
log = MyLog(name=name)
"""
自助验证闸机B门接口在并发30时，服务器响应时间小于1s，并且压力不断向上提高，
直到服务器能够处理的最大负荷极限，输出此时服务器资源情况以及请求数量情况。
"""


class TaskBAutozhaji(TaskSequence):

    """发送自助闸机B门接口
    """
    @task
    def post_auto_zhaji_b(self):
        status = False
        body = {"reqId": get_uuid(),
                "gateNo": "T3AJ1",
                "deviceId": "T3AJ001",
                "cardType": 1,
                "idCard": "500238199312134390",
                "nameZh": "nameZh",  # 非必填
                "nameEn": "nameEh",  # 非必填
                "age": get_age("500238199312134390"),  # 非必填
                "sex": 1,  # 非必填
                "birthDate": get_birthday("500238199312134390"),
                "address": "重庆市",  # 非必填
                "certificateValidity": "20150212-20201212",
                "nationality": "China",  # 非必填
                "ethnic": "汉族",  # 非必填
                "contactWay": "0123456789",  # 非必填
                "scenePhoto": Base64Picture,
                "sceneFeature": get_txt(shiwanli8k_features+"/"+"0.txt"),
                "cardPhoto": Base64Picture,
                "cardFeature": get_txt(shiwanid8k_features+"/"+"0.txt")
                }
        # self.host + self.anjian_server + "/api/v1/face/security/face-check"
        with self.client.post(url="/security-server/api/v1/face/security/face-check",
                              json=body,
                              headers=AirportProcess().get_headers("/api/v1/face/security/face-check"),
                              verify=False,
                              catch_response=True) as response:
            response.success()
            jsondata = None
            try:
                jsondata = json.loads(response.text)
                if jsondata["result"] == 0:
                    status = True
                elif jsondata["result"] == 1:
                    status = False
                elif jsondata["result"] == 2:
                    status = False
            except Exception as e:
                log.logger.error("失败"+str(jsondata)+str(e))
        if status:
            pass


class Behavior(HttpLocust):
    task_set = TaskBAutozhaji
    max_wait = 10000
    min_wait = 10
    host = "http://192.168.1.106:9091"

if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    command1 = "c:"
    command2 = r"cd %s" % current_path
    command3 = r"locust -f api_security_ticket_check_B.py -P 8094 --web-host=127.0.0.1"
    os.system(command1)
    os.system(command2)
    os.system(command3)