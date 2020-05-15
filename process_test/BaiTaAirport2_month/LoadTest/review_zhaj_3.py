# coding:utf-8
from locust import HttpLocust,seq_task,task,TaskSequence
from BaiTaAirport2_month.API.AirportProcess import *
import json

"""3.在底库10000人时，对同一个进行并发30压力测试，
并且传入的特征为最后一次注册后人员的特征，服务器响应时间小于？，持续时间1小时
测试步骤，
1.先建立底库为10000人，图片索引0-9999
2.对9999人索引底库进行请求发送
3.查看服务器响应时间，以及识别率情况
"""


class ReviewAutoZHAji3(TaskSequence):
    """2.3.16 自助闸机复核接口（二期）"""

    @staticmethod
    def build_lib():
        """通过人工通道验票接口建立10000人的底库,直接造成航班号为图片名称
        """
        # 先生成3000个不同的身份证号码
        list_id = get_random_idcard_to_only_list(10000)
        for i in range(0, 10000):
            # 进行人员注册
            a = AirportProcess().api_face_security_face_check(reqId=get_uuid(), gateNo="T3AJ1", deviceId="T3AJ001",
                                                              cardType=0,
                                                              idCard=list_id[i],
                                                              nameZh="name"+str(i),
                                                              nameEn="englishName",
                                                              age=get_age(list_id[i]),
                                                              sex=random.randint(0,1),
                                                              birthDate=get_birthday(list_id[i]),
                                                              address="重庆",
                                                              certificateValidity="2008-2022",
                                                              nationality="China",
                                                              ethnic="汉族",
                                                              contactWay="0123456789",
                                                              scenePhoto=to_base64(shiwanid+"/"+str(i)+".jpg"),
                                                              sceneFeature=get_txt(shiwanid8k_features+"/"+str(i)+".txt"),
                                                              cardPhoto=to_base64(shiwanid+"/"+str(i)+".jpg"),
                                                              cardFeature=get_txt(shiwanid8k_features+"/"+str(i)+".txt"))
            print(a+"\n"+"第%d次注册底库成功"% i )

    @task
    def post_review_anto_zhaji_3(self):
        # self.host+self.review_server+"/api/v1/face/review/self-check"  # 自助闸机复核接口
        index = 10000
        body = {"reqId": get_uuid(),
                "gateNo": "T3AJ2",
                "deviceId": "T3AJ002",
                "scenePhoto": to_base64(shiwanli+"/"+str(index)+".jpg"),
                "sceneFeature": get_txt(shiwanli2k_features+"/"+str(index)+".txt")}
        with self.client.post(url="/review-server/api/v1/face/review/self-check",
                              json=body,
                              headers=AirportProcess().get_headers("/api/v1/face/review/self-check"),
                              verify=False,
                              catch_response=True) as response:
            json_data = json.loads(str(response.text))
            if json_data["status"] == 0 and json_data["result"] == 0 and json_data["userInfo"]["nameZh"] == "name"+str(index):
                response.success()
            else:
                response.failure('Failed!,没有识别出来')


class BehaviorReview2(HttpLocust):
    task_set = ReviewAutoZHAji3
    max_wait = 1000
    min_wait = 1000
    host = "http://192.168.1.106:9091"


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    command1 = "c:"
    command2 = r"cd %s" % current_path
    command3 = r"locust -f review_zhaj_3.py -P 8097 --web-host=127.0.0.1"
    os.system(command1)
    os.system(command2)
    os.system(command3)