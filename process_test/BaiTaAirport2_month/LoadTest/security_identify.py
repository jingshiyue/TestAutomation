# coding:utf-8
from locust import HttpLocust,TaskSequence,task
from BaiTaAirport2_month.API.AirportProcess import *
import json
"""（1）、对人证1：1接口进行30高并发测试，服务器响应时间小于1s，同时，返回状态正确
"""


class TaskSecIdentify(TaskSequence):
    @task
    def post_sec_identify(self):
        # self.host+self.anjian_server+"/api/v1/face/security/check"  # 安检1：1人脸验证
        body = {"reqId": get_uuid(),
                 "gateNo": "T6test",
                 "deviceId": "T6test001",
                 "cardType": 0,  # 证件类型 int
                 "idCard": "500228195802035223",
                 "nameZh": "test01",
                 "nameEn": "english",
                 "age": "50",  # int
                 "sex": "1",  # int
                 "birthDate": "19580203",
                 "address": "隋唐",
                 "certificateValidity": "20081010-20191206",  # 时间yyyymmdd或者长期(起-止)
                 "nationality": "China",
                 "ethnic": "汉族",
                 "contactWay": "18680946659",
                "scenePhoto": to_base64(shiwanli+"/"+"10000.jpg"),
                 "sceneFeature": get_txt(shiwanli8k_features+"/"+"10000.txt"),
                 "cardPhoto": to_base64(shiwanid+"/"+"10000.jpg"),
                 "cardFeature": get_txt(shiwanid8k_features+"/"+"10000.txt"),
                 }
        with self.client.post(url="/security-server/api/v1/face/security/check",
                              json=body,
                              headers=AirportProcess().get_headers("/api/v1/face/security/check"),
                              verify=False,
                              catch_response=True) as response:
            json_data = None
            try:
                json_data = json.loads(str(response.text))
                if json_data["result"] == 0:
                    response.success()
                    print("比对成功")
                else:
                    response.failure("比对失败"+"\n"+str(json_data))
                    logger.info("比对失败")
            except Exception as e:
                response.failure("比对失败"+"\n"+str(json_data))
                logger.error("解析出错"+str(e)+"\n"+str(json_data))


class BehaviorIdentify(HttpLocust):
    task_set = TaskSecIdentify
    max_wait = 6000
    min_wait = 1000
    host = "http://192.168.1.106:9091"

if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    command1 = "c:"
    command2 = r"cd %s" % current_path
    command3 = r"locust -f security_identify.py -P 8101 --web-host=127.0.0.1"
    os.system(command1)
    os.system(command2)
    os.system(command3)