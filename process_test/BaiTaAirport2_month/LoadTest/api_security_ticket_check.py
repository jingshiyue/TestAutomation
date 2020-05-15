# coding:utf-8
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture
from locust import HttpLocust,seq_task,TaskSequence,task
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.common.Log import MyLog
name = os.path.realpath(__file__).split("\\")[-1].split(".")[0]
log = MyLog(name=name)
"""1.自助验证闸机A门接口在并发30时，服务器响应时间小于1s，
并且压力不断向上提高，直到服务器能够处理的最大极限，输出此时服务器资源情况以及请求数量情况。
"""


class TaskAutoAzhaji(TaskSequence):
    """发送自助验证闸机A门接口"""
    @task
    def post_auto_zhaji(self):
        status = None
        e = None
        data = {"reqId": get_uuid(),
                "gateNo": "T1AJ1",
                "deviceId": "T1AD001",
                "cardType": 1,
                "idCard": "500238199312134390",
                "nameZh": "nameZh",  # 非必填
                "nameEn": "nameEn",  # 非必填
                "age": get_age("500238199312134390"),  # 非必填
                "sex": "1",  # 非必填
                "birthDate": get_birthday("500238199312134390"),
                "address": "重庆市",  # 非必填
                "certificateValidity": "20150212-20201212",
                "nationality": "China",  # 非必填
                "ethnic": "汉族",  # 非必填
                "contactWay": "123456789",  # 非必填
                "cardPhoto": Base64Picture,
                "fId": get_uuid()}
        with self.client.post(url="/security-server/api/v1/face/security/ticket-check",
                              json=data,
                              headers=AirportProcess().get_headers("/api/v1/face/security/ticket-check"),
                              verify=False,
                              catch_response=True) as response:
            response.success()
        json_data = None
        try:
            json_data = json.loads(str(response.text))
            if json_data["status"] == 0:
                if json_data["result"] == 0:
                    status = True
                elif json_data["result"] == 1:
                    status = False
                else:
                    status = False
            else:
                status = False
                log.logger.warn("服务器返回错误")
        except Exception as e:
            status = False
            log.logger.error("解析错误"+str(json_data)+str(e))
        if status:
            log.logger.info("人票验证通过"+str(json_data))


class Beav(HttpLocust):
    task_set = TaskAutoAzhaji
    max_wait = 10000
    min_wait = 10
    host = "http://192.168.1.106:9091"

if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    command1 = "c:"
    command2 = r"cd %s" % current_path
    command3 = r"locust -f api_security_ticket_check.py -P 8093 --web-host=127.0.0.1"
    os.system(command1)
    os.system(command2)
    os.system(command3)