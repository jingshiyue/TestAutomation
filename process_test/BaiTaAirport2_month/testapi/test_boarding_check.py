# coding:utf-8
# @author : chenkeyun
# @date : 20190305
import pytest
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture


def test_1_01(method_12):
    """传入已通过登机口复核的旅客信息,验证传入已通过登机口复核的旅客信息，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(reqId=get_uuid(),
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanid2k_features+"/25000.txt"),
                                deviceCode="T1DJ001",
                                boardingGate="06",
                                flightNo="zhengchangflight",
                                flightDay=produce_flight_date())
    json_data = json.loads(res.text)
    print(json_data)
    print("传入已通过登机口复核的旅客信息,验证传入已通过登机口复核的旅客信息，服务器能正常响应")


def test_1_02(method_13):
    """1:1安检，通道复核,验证传入正确的参数，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(reqId=get_uuid(),
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanid2k_features+"/25003.txt"),
                                deviceCode="T1DJ001",
                                boardingGate="07",
                                flightNo="zhengchang1",
                                flightDay=produce_flight_date())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 0 and json_data['userInfo']['cardNo'] == '222238199312134392'
    print("1:1安检，通道复核,验证传入正确的参数，服务器能正常响应")


def test_1_03(method_14):
    """1:1安检，人工复核fangxing,验证传入正确的参数，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(reqId=get_uuid(),
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanid2k_features+"/25004.txt"),
                                deviceCode="T1DJ001",
                                boardingGate="08",
                                flightNo="zhengchang2",
                                flightDay=produce_flight_date())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 0 and json_data['userInfo']['cardNo'] == '222238199312134393'
    print("1:1安检，人工复核fangxing,验证传入正确的参数，服务器能正常响应")


def test_1_04(method_15):
    """1:1安检，人工复核报警,验证传入正确的参数，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(reqId=get_uuid(),
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanid2k_features+"/25005.txt"),
                                deviceCode="T1DJ001",
                                boardingGate="09",
                                flightNo="zhengchang3",
                                flightDay=produce_flight_date())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 0 and json_data['userInfo']['cardNo'] == '222238199312134394'
    print("1:1安检，人工复核报警,验证传入正确的参数，服务器能正常响应")


def test_2_01():
    """不是该登机口航班的旅客,验证传入正确的参数，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(reqId=get_uuid(),
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanid2k_features+"/25005.txt"),
                                deviceCode="T1DJ001",
                                boardingGate="09",
                                flightNo="test004",
                                flightDay=produce_flight_date())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 0 and json_data['msg'] == 'not find the flightNumber'
    print("不是该登机口航班的旅客,验证传入正确的参数，服务器能正常响应")


def test_2_02():
    """验证传入的reqId为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(reqId=None,
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanid2k_features+"/25005.txt"),
                                deviceCode="T1DJ001",
                                boardingGate="09",
                                flightNo="test004",
                                flightDay=produce_flight_date())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data['msg'] == 'bad params<reqId is empty> '
    print("验证传入的reqId为空时服务器能正确响应")


def test_2_03():
    """验证传入的faceImage为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(reqId=get_uuid(),
                                faceImage=None,
                                faceFeature=get_txt(shiwanid2k_features+"/25005.txt"),
                                deviceCode="T1DJ001",
                                boardingGate="09",
                                flightNo="test004",
                                flightDay=produce_flight_date())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data['msg'] == 'bad params<faceImage is empty> '
    print("验证传入的faceImage为空时服务器能正确响应")


def test_2_04():
    """验证传入的faceFeature为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(reqId=get_uuid(),
                                faceImage=Base64Picture,
                                faceFeature=None,
                                deviceCode="T1DJ001",
                                boardingGate="09",
                                flightNo="test004",
                                flightDay=produce_flight_date())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data['msg'] == 'bad params<faceFeature is empty> '
    print("验证传入的faceFeature为空时服务器能正确响应")


def test_2_05():
    """验证传入的deviceCode为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(reqId=get_uuid(),
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanid2k_features+"/25005.txt"),
                                deviceCode=None,
                                boardingGate="09",
                                flightNo="test004",
                                flightDay=produce_flight_date())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data['msg'] == 'bad params<deviceCode is empty> '
    print("验证传入的deviceCode为空时服务器能正确响应")


def test_2_06():
    """验证传入的boardingGate为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(reqId=get_uuid(),
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanid2k_features+"/25005.txt"),
                                deviceCode="T1DJ001",
                                boardingGate=None,
                                flightNo="test004",
                                flightDay=produce_flight_date())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data['msg'] == 'bad params<boardingGate is empty> '
    print("验证传入的boardingGate为空时服务器能正确响应")


def test_2_07():
    """验证传入的flightNo为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(reqId=get_uuid(),
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanid2k_features+"/25005.txt"),
                                deviceCode="T1DJ001",
                                boardingGate="01",
                                flightNo=None,
                                flightDay=produce_flight_date())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data['msg'] == 'bad params<flightNo is empty> '
    print("验证传入的flightNo为空时服务器能正确响应")


if __name__ == '__main__':
    pytest.main(["-q", "test_boarding_check.py"])
