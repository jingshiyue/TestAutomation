# coding:utf-8
# @author : chenkeyun
# @date : 20190302
import pytest
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture


def test_01_01(method_1):
    """验证安检人工通道人证1：1,传入人工通道人证1：1安检的旅客信息，服务器能正常响应"""
    time.sleep(2)
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(5200)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 0 and json_data["userInfo"]["cardNo"] == "700238199312134390"


def test_01_02():
    """验证传入已通过通道复核的旅客信息，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(5200)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 0 and json_data["userInfo"]["cardNo"] == "700238199312134390" and json_data[ 'isWrite'] == 1


def test_01_03(method_2):
    """验证传入安检刷机票通过的旅客信息，服务器能正常响应"""
    time.sleep(2)
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(5201)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    print("通道复核验证传入安检刷机票通过的旅客信息，服务器能正常响应")
    assert json_data["status"] == 0 and json_data["userInfo"]['flightNumber'] == "hangban001"


def test_01_04(method_3):
    """验证传入人工通道人工放行的旅客信息，服务器能正常响"""
    time.sleep(1)
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(5202)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    print("通道复核验证传入人工通道人工放行的旅客信息，服务器能正常响")
    assert json_data["status"] == 0 and json_data["userInfo"]['flightNumber'] == "hangban002"


def test_02_01():
    """验证传入的reqId为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(reqId=None,
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(5203)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'bad params' and json_data['isWrite'] == 0


def test_02_02():
    """验证传入的gateNo为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(reqId=get_uuid(),
                              gateNo=None,
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(5203)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'bad params<gateNo is empty> ' and json_data['isWrite'] == 0


def test_02_03():
    """验证传入的deviceId为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(reqId=get_uuid(),
                              gateNo="T1AJ1",
                              deviceId=None,
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(5203)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'bad params<device id is empty> ' and json_data['isWrite'] == 0
    print("验证传入的deviceId为空时服务器能正确响应")


def test_02_04():
    """验证传入的scenePhoto为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(reqId=get_uuid(),
                              gateNo="T1AJ1",
                              deviceId="T1AJ001",
                              scenePhoto=None,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(5203)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'badparams<faceImage is empty> ' and json_data['isWrite'] == 0
    print("验证传入的scenePhoto为空时服务器能正确响应")


def test_02_05():
    """验证传入的sceneFeature为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(reqId=get_uuid(),
                              gateNo="T1AJ1",
                              deviceId="T1AJ001",
                              scenePhoto=Base64Picture,
                              sceneFeature=None)
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'bad params<feature data is error> ' and json_data['isWrite'] == 0
    print("验证传入的scenePhoto为空时服务器能正确响应")


if __name__ == '__main__':
    pytest.main(["-q", "test_face_review_check"])
