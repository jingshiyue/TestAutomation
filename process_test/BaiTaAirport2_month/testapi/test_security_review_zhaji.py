# coding:utf-8
# @author : chenkeyun
# @date : 20190301
import pytest
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture


def test_01_01():
    """验证有安检闸机B门通过记录传入安检闸机B门通过的旅客信息，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
                                   gateno="T1AF1",
                                   deviceid="T1AF001",
                                   scenephoto=Base64Picture,
                                   scenefeature=get_txt(shiwanli2k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    assert json_data['userInfo']["cardNo"] == "500238199312134391" and json_data["status"] == 0
    print("验证有安检闸机B门通过记录传入安检闸机B门通过的旅客信息，服务器能正常响应")


def test_01_02():
    """验证没有通过B门传入没有安检闸机B门通过记录的旅客信息的参数，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
                                   gateno="T1AF1",
                                   deviceid="T1AF001",
                                   scenephoto=Base64Picture,
                                   scenefeature=get_txt(shiwanli2k_features+"/"+str(5004)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["msg"] == 'not find the match face' and json_data["status"] == 0
    print("验证有安检闸机B门通过记录传入安检闸机B门通过的旅客信息，服务器能正常响应")


def test_01_03():
    """验证传入的reqId为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=None,
                                   gateno="T1AF1",
                                   deviceid="T1AF001",
                                   scenephoto=Base64Picture,
                                   scenefeature=get_txt(shiwanli2k_features+"/"+str(5004)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["msg"] == 'bad params' and json_data["status"] == 400
    print("验证传入的reqId为空时服务器能正确响应")


def test_01_04():
    """验证传入的gateNo为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
                                   gateno=None,
                                   deviceid="T1AF001",
                                   scenephoto=Base64Picture,
                                   scenefeature=get_txt(shiwanli2k_features+"/"+str(5004)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["msg"] == 'bad params<gateNo is empty> ' and json_data["status"] == 400
    print("验证传入的gateNo为空时服务器能正确响应")


def test_01_05():
    """验证传入的deviceId为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
                                   gateno="T1AF1",
                                   deviceid=None,
                                   scenephoto=Base64Picture,
                                   scenefeature=get_txt(shiwanli2k_features+"/"+str(5004)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["msg"] == 'bad params<device id is empty> ' and json_data["status"] == 400
    print("验证传入的deviceId为空时服务器能正确响应")


def test_01_06():
    """验证传入的scenePhoto为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
                                   gateno="T1AF1",
                                   deviceid="T1AF001",
                                   scenephoto=None,
                                   scenefeature=get_txt(shiwanli2k_features+"/"+str(5004)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["msg"] == 'badparams<faceImage is empty> ' and json_data["status"] == 400
    print("验证传入的scenePhoto为空时服务器能正确响应")


def test_01_07():
    """验证传入的sceneFeature为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
                                   gateno="T1AF1",
                                   deviceid="T1AF001",
                                   scenephoto=Base64Picture,
                                   scenefeature=None)
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["msg"] == 'bad params<feature data is error> ' and json_data["status"] == 400
    print("验证传入的sceneFeature为空时服务器能正确响应")


if __name__ == '__main__':
    pytest.main(["-q", "test_security_review_zhaji"])


