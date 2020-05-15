# coding:utf-8
# @author : chenkeyun
# @date : 20190301
import pytest
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture


def test_01_01(zhiji_to_manopcheck):
    """验证现场照和身份证照匹配（分数较低），人工查验通过传入安检口多次人脸识别失败，
    现场照和身份证照匹配旅客信息，服务器能正常响应"""
    # 安检人工放行接口
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard="500238199312154390",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 0 and json_data["msg"] == 'Success'


def test_01_02():
    """验证传入的reqId为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=None,
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard="500238199312154390",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'reqId is empty'
    print("验证传入的reqId为空时服务器能正确响应")


def test_01_03():
    """验证传入的gateNo为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo=None,
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard="500238199312154390",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'badparams<gateNo is empty> '
    print("验证传入的gateNo为空时服务器能正确响应")


def test_01_04():
    """验证传入的deviceId为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId=None,
                                          cardType="0",
                                          idCard="500238199312154390",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'badparams<deviceId is empty> '
    print("验证传入的deviceId为空时服务器能正确响应")


def test_01_05():
    """验证传入的cardType为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType=None,
                                          idCard="500238199312154399",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'bad params'
    print("验证传入的cardType为空时服务器能正确响应")


def test_01_06():
    """验证传入的birthDate为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard="500238199312154390",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=None,
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'badparams<birthDate is empty> '
    print("验证传入的birthDate为空时服务器能正确响应")


def test_01_08():
    """验证传入的idCard为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard=None,
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'badparams<idcard is empty> '
    print("验证传入的idCard为空时服务器能正确响应")


def test_02_01():
    """验证传入的certificateValidity为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard="500238199312154390",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity=None,
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'badparams<certificateValidity is empty> '
    print("验证传入的certificateValidity为空时服务器能正确响应")


def test_02_02():
    """验证传入的nationality为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard="500238199312154399",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality=None,
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'badparams<Nationality is empty> '
    print("验证传入的nationality为空时服务器能正确响应")


def test_02_03():
    """验证传入的ethnic为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard="500238199312154390",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic=None,
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'badparams<ethnic is empty> '
    print("验证传入的ethnic为空时服务器能正确响应")


def test_02_04():
    """验证传入的scenePhoto为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard="500238199312154390",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=None,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'badparams<scenePhoto is empty> '
    print("验证传入的scenePhoto为空时服务器能正确响应")


def test_02_05():
    """验证传入的sceneFeature为空时服务器能正确响应,没有检测到人脸也能放行通过"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard="500238199312154390",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=None,
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 0 and json_data["msg"] == 'Success'
    print("验证传入的sceneFeature为空时服务器能正确响应,没有检测到人脸也能放行通过")


def test_02_06():
    """验证传入的cardPhoto为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard="500238199312154399",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=None,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'badparams<cardPhoto is empty> '
    print("验证传入的cardPhoto为空时服务器能正确响应")


def test_02_07():
    """验证传入的cardFeature为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard="500238199312154390",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=None)
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'badparams<cardFeature is empty> '
    print("验证传入的cardFeature为空时服务器能正确响应")

if __name__ == '__main__':
    pytest.main(["-q", "test_security_manual_optcheck.py"])

"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard="500238199312154390",
                                          nameZh="nameZh",
                                          nameEn="nameEn",
                                          age=get_age("500238199312154390"),
                                          sex="1",
                                          birthDate=get_birthday("500238199312154390"),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'Success'

"""