# coding:utf-8
# @author : chenkeyun
# @date : 20190301
import pytest
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture


def test_01_01():
    """验证传入现场照和身份证照匹配，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 0 and json_data["result"] == 0


def test_01_02():
    """验证传入同一人的另外的现场照和身份证照匹配，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 0 and json_data["result"] == 0


def test_01_03():
    """验证未值机时传入现场照和身份证照匹配，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134395",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 105 and json_data["result"] == 1


def test_01_04():
    """验证值机信息不是当天的旅客传入现场照和身份证照匹配，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134396",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 105 and json_data["result"] == 1


def test_01_05():
    """验证通过A门后传入现场照和身份证照不匹配，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5002)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 0 and json_data["result"] == 1


def test_01_06():
    """验证传入的gateNo为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo=None,
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 400 and json_data["msg"] == "bad params<gateno is empty> "


def test_02_01():
    """验证传入的deviceId为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId=None,
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 400 and json_data["msg"] == "bad params<deviceID is empty> "


def test_02_02():
    """验证传入的cardType为空时服务器能正确响应"""  # 不做校验
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType=None,
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 0 and json_data["msg"] == "Success"


def test_02_03():
    """验证传入的idCard为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType=0,
                                     idCard=None,
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 400 and json_data["msg"] == "bad params<idCard is empty> "


def test_02_04():
    """验证传入的birthDate为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=None,
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 400 and json_data["msg"] == "bad params<birthDate is empty> "


def test_02_05():
    """验证传入的certificateValidity为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity=None,
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 0 and json_data["result"] == 0


def test_02_06():
    """验证传入的nationality为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality=None,
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 00 and json_data["result"] == 0


def test_02_07():
    """验证传入的ethnic为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic=None,
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 0 and json_data["result"] == 0


def test_02_08():
    """验证传入的scenePhoto为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=None,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 400 and json_data["msg"] == "bad params<scenephoto is empty> "


def test_02_09():
    """验证传入的sceneFeature为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=None,
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 400 and json_data["msg"] == "bad params<scenefeature is empty> "


def test_03_01():
    """验证传入的cardPhoto为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=None,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 400 and json_data["msg"] == "bad params<cardphoto is empty> "


def test_03_02():
    """验证传入的cardFeature为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=None)
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 400 and json_data["msg"] == "bad params<cardfeature is empty> "


if __name__ == '__main__':
    pytest.main(["-q", "test_face_security_face_check.py"])
"""    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard="500238199312134391",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age=get_age("500238199312134391"),
                                     sex="1",
                                     birthDate=get_birthday("500238199312134391"),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5000)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5000)+".txt"))
    json_data = json.loads(res.text)
    print(res.text)
    assert json_data["status"] == 0 and json_data["result"] == 0

 """