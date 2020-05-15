# coding:utf-8
# @author : chenkeyun
# @date : 20190304
import pytest
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture


def test_1_01(method_6):
    """验证传入中转旅客的参数，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(reqId=get_uuid(),
                                             flightNo="test006",
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1zz1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+"7000.txt"),
                                             sourceType="0")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 0
    print("验证传入中转旅客的参数，服务器能正常响应")


def test_1_02(method_7):
    """验证传入经停的参数，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(reqId=get_uuid(),
                                             flightNo="test007",
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1zz1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+"7001.txt"),
                                             sourceType="1")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 0
    print("验证传入中转旅客的参数，服务器能正常响应")


def test_2_01():
    """验证gateNo为空"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(reqId=get_uuid(),
                                             flightNo="test008",
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo=None,
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+"7002.txt"),
                                             sourceType="1")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'bad params<gateNo is empty> '
    print("验证中转通道接口gateNo为空")


def test_2_02():
    """验证gateNo为空值"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(reqId=get_uuid(),
                                             flightNo="test008",
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+"7002.txt"),
                                             sourceType="1")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'bad params<gateNo is empty> '
    print("验证中转通道接口gateNo为空")

if __name__ == '__main__':
    pytest.main(["-q", "test_transfergate_ticket_collect.py"])