# coding:utf-8
# @author : chenkeyun
# @date : 20190305
import pytest
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture


def test_1_00():
    """验证无航班信息时reqiID返回正确"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="reqIdflight",
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate="01",
                                        deviceCode="T1DJ001",
                                        gateNo="T1DJ1")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 0 and json_data["reqId"] != None


def test_1_01(method_8):
    """500建库人数,500本地出发人员,0个中转的人数,0个经停的人数,验证传入正确的参数，服务器能正常响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="bendiflight",
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate="01",
                                        deviceCode="T1DJ001",
                                        gateNo="T1DJ1")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 0 and json_data["result"]["totalPassengerNum"] == 500 and json_data["result"]['localDepartNum'] == 500


def test_1_02(method_9):
    """500建库人数0本地出发人员,500个中转的人数,0个经停的人数,验证传入正确的参数，服务器能正常响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="zhongzhuanflight",
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate="02",
                                        deviceCode="T1DJ001",
                                        gateNo="T1DJ1")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 0 and json_data["result"]["totalPassengerNum"] == 500 and json_data["result"]['transferNum'] == 500


def test_1_03(method_10):
    """500建库人数0本地出发人员,0个中转的人数,500个经停的人数,验证传入正确的参数，服务器能正常响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="jingtingflight",
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate="03",
                                        deviceCode="T1DJ001",
                                        gateNo="T1DJ1")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 0 and json_data["result"]["totalPassengerNum"] == 500 and json_data["result"]['stopNum'] == 500 and json_data["reqId"] !=None


def test_1_04(method_11):
    """500建库人数498本地出发,人员1个中转的人数,1个经停的人数,验证传入正确的参数，服务器能正常响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="hunheflight",
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate="04",
                                        deviceCode="T1DJ004",
                                        gateNo="T1DJ4")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 0 and json_data["result"]["totalPassengerNum"] == 500 and json_data["result"]['stopNum'] == 1 and json_data["reqId"] !=None and json_data["result"]['transferNum'] == 1


def test_2_01():
    """验证传入的reqId为空时服务器能正确响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=None,
                                        flightNo="test1flight",
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate="01",
                                        deviceCode="T1DJ001",
                                        gateNo="T1DJ1")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 400 and json_data["reqId"] != None and json_data["msg"] == 'reqId is empty'


def test_2_02():
    """验证传入的flightNo为空时服务器能正确响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo=None,
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate="01",
                                        deviceCode="T1DJ001",
                                        gateNo="T1DJ1")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 400 and json_data["reqId"] != None and json_data["msg"] == 'flightNo is empty'


def test_2_03():
    """验证传入的date为空时服务器能正确响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="test1flight",
                                        date=None,                 # 日期yyyyMMdd
                                        boardingGate="01",
                                        deviceCode="T1DJ001",
                                        gateNo="T1DJ1")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 400 and json_data["reqId"] != None and json_data["msg"] == 'date is empty'


def test_2_04():
    """验证传入的boardingGate为空时服务器能正确响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="test1flight",
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate=None,
                                        deviceCode="T1DJ001",
                                        gateNo="T1DJ1")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 400 and json_data["reqId"] != None and json_data["msg"] ==  'boardingGate is empty'


def test_2_05():
    """验证传入的deviceCode为空时服务器能正确响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="test1flight",
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate="01",
                                        deviceCode=None,
                                        gateNo="T1DJ1")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 400 and json_data["reqId"] != None and json_data["msg"] == 'deviceCode is empty'


def test_2_06():
    """验证传入的gateNo为空时服务器能正确响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="test1flight",
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate="01",
                                        deviceCode="1",
                                        gateNo=None)
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 400 and json_data["reqId"] != None and json_data["msg"] == 'gateNo is empty'


def test_3_01():
    """验证传入的flightNo为空值时服务器能正确响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="",
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate="01",
                                        deviceCode="T1DJ001",
                                        gateNo="T1DJ1")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 400 and json_data["reqId"] != None and json_data["msg"] == 'flightNo is empty'


def test_3_02():
    """验证传入的date为空值时服务器能正确响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="test1flight",
                                        date="",                 # 日期yyyyMMdd
                                        boardingGate="01",
                                        deviceCode="T1DJ001",
                                        gateNo="T1DJ1")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 400 and json_data["reqId"] != None and json_data["msg"] == 'date is empty'


def test_3_03():
    """验证传入的boardingGate为空值时服务器能正确响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="test1flight",
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate="",
                                        deviceCode="T1DJ001",
                                        gateNo="T1DJ1")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 400 and json_data["reqId"] != None and json_data["msg"] ==  'boardingGate is empty'


def test_3_04():
    """验证传入的deviceCode为空值时服务器能正确响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="test1flight",
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate="01",
                                        deviceCode="",
                                        gateNo="T1DJ1")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 400 and json_data["reqId"] != None and json_data["msg"] == 'deviceCode is empty'


def test_3_05():
    """验证传入的gateNo为空值时服务器能正确响应"""
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="test1flight",
                                        date=produce_flight_date(),                 # 日期yyyyMMdd
                                        boardingGate="01",
                                        deviceCode="1",
                                        gateNo="")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 400 and json_data["reqId"] != None and json_data["msg"] == 'gateNo is empty'


def test_3_06():
    """验证传入的date格式不为yyyymmdd时服务器能正确响应"""
    # 不做校验
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_library_check(reqId=get_uuid(),
                                        flightNo="test1flight",
                                        date="农历二月初一",                 # 日期yyyyMMdd
                                        boardingGate="01",
                                        deviceCode="1",
                                        gateNo="mmm")
    json_data = json.loads(res1)
    print(json_data)
    assert json_data["status"] == 0 and json_data["msg"] == 'Success'
if __name__ == '__main__':
    pytest.main(["-q", "test_boarding_library_check.py"])

