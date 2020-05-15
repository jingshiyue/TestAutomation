# coding:utf-8
# @author : chenkeyun
# @date : 20190331
import pytest
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture


def test_01(zhiji):
    """1 验证传入已值机旅客信息，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="500238199312134391",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("500238199312134391"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("500238199312134391"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-20230202",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["result"] == 0


def test_01_01():
    """验证响应时间小于500ms"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="500238199312134391",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("500238199312134391"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("500238199312134391"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-20230202",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(str(json_data)+"\n"+"响应时间为：%ss" % (str(res.elapsed.total_seconds())))
    assert json_data["result"] == 0 and res.elapsed.total_seconds() < 0.5


def test_02():
    """2 验证传入重复的旅客信息，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="500238199312134391",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("500238199312134391"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("500238199312134391"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-20230202",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["result"] == 0


def test_03():
    """3 验证传入未值机旅客信息，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="500238199312134392",
                                                                                      age=get_age("500238199312134391"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("500238199312134391"),
                                                                                      cardPhoto=Base64Picture,)
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["result"] == 1


def test_04():
    """4 验证已值机，身份证过期的旅客信息，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="500238199312134391",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("500238199312134391"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("500238199312134391"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-20180202",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["result"] == 2


def test_05():
    """5 验证已值机，长期身份证的旅客信息，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="500238199312134391",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("500238199312134391"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("500238199312134391"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-长期",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["result"] == 0


def test_06():
    """验证值机信息不是当天的旅客，刷身份证后，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="600238199312134390",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("600238199312134390"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("500238199312134391"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-长期",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["result"] == 1


def test_07(zhiji_two):
    """7 验证当天的值机信息有多条的旅客，刷身份证后，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="100238199312134390",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("100238199312134390"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("100238199312134390"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-长期",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["result"] == 1


def test_08():
    """8 验证传入的reqId为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=None,
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="100238199312134390",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("100238199312134390"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("100238199312134390"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-长期",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 500 and json_data["result"] == 0


def test_09():
    """9 验证传入的gateNo为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo=None,
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="100238199312134390",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("100238199312134390"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("100238199312134390"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-长期",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'bad params<gateno is empty> '


def test_09_01():
    """验证传入的deviceId为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId=None,
                                                                                      cardType=0,
                                                                                      idCard="100238199312134390",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("100238199312134390"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("100238199312134390"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-长期",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'bad params<deviceID is empty> '


def test_09_02():
    """验证传入的cardType为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ001",
                                                                                      cardType=None,
                                                                                      idCard="100238199312134390",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("100238199312134390"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("100238199312134390"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-长期",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'bad params<cardType is empty> '


def test_09_03():
    """验证传入的idCard为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ001",
                                                                                      cardType=0,
                                                                                      idCard=None,
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("100238199312134390"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("100238199312134390"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-长期",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'bad params<idCard is empty> '


def test_09_04():
    """验证传入的birthDate为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ001",
                                                                                      cardType=0,
                                                                                      idCard="100238199312134390",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("100238199312134390"),
                                                                                      sex=0,
                                                                                      birthDate=None,
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-长期",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'bad params<birthDate is empty> '


def test_09_05():
    """验证传入的certificateValidity为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="500238199312134391",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("500238199312134391"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("500238199312134391"),
                                                                                      address="重庆市",
                                                                                      certificateValidity=None,
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["result"] == 0 and json_data['msg'] == 'bad params<certificateValidity is empty> '


def test_09_06():
    """验证传入的cardPhoto为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="500238199312134391",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("500238199312134391"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("500238199312134391"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20180201-长期",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=None,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data['msg'] == 'bad params<cardphoto is empty> '


def test_09_07():
    """验证传入的fId为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="500238199312134391",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age=get_age("500238199312134391"),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("500238199312134391"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20180201-长期",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=None)
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data['msg'] == 'bad params<fid is empty> '


def test_09_08():
    """验证传入的age不为int型时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="500238199312134391",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age="你的",
                                                                                      sex=0,
                                                                                      birthDate=get_birthday("500238199312134391"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20180201-长期",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 204 and json_data['msg'] == 'No Content'


def test_09_09():
    """
    验证传入的sex不为int型时服务器能正确响应
    :return:
    """
    res = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard="500238199312134391",
                                                                                      nameZh="ckytest",
                                                                                      nameEn="ckytest",
                                                                                      age="24",
                                                                                      sex="nide",
                                                                                      birthDate=get_birthday("500238199312134391"),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20180201-长期",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 204 and json_data['msg'] == 'No Content'
if __name__ == '__main__':
    pytest.main(["-q", "test_security_ticket_check_test.py"])