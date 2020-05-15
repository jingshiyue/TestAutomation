# coding:utf-8
# @author : chenkeyun
# @date : 20190305
import pytest
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture


def test_1_01(method_16):
    """先刷票，然后放行,验证传入放行的参数，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo="method16",
                                       date=produce_flight_date(),
                                       boardingGate="10",
                                       deviceCode="T1DJ001",
                                       gateNo="T1DJ001",
                                       cardId="",
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="passengerName",
                                       boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("先刷票，然后放行,验证传入放行的参数，服务器能正常响应")
    assert json_data["status"] == 0


def test_1_02(method_17):
    """报警,验证传入报警的参数，服务器能正常响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo="method17",
                                       date=produce_flight_date(),
                                       boardingGate="11",
                                       deviceCode="T1DJ001",
                                       gateNo="T1DJ001",
                                       cardId="",
                                       scenePhoto=Base64Picture,
                                       sourceType="1",
                                       passengerName="passengerName",
                                       boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("报警,验证传入报警的参数，服务器能正常响应")
    assert json_data["status"] == 0


def test_2_01():
    """验证传入的flightNo，cardId，boardingNumber都为空值时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo=None,
                                       date=produce_flight_date(),
                                       boardingGate="11",
                                       deviceCode="T1DJ001",
                                       gateNo="T1DJ001",
                                       cardId=None,
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="passengerName",
                                       boardingNumber=None
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("验证传入的flightNo，cardId，boardingNumber都为空值时服务器能正确响应")


def test_2_02():
    """验证传入的reqId为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=None,
                                       flightNo="method18",
                                       date=produce_flight_date(),
                                       boardingGate="10",
                                       deviceCode="T1DJ001",
                                       gateNo="T1DJ001",
                                       cardId="",
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="passengerName",
                                       boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("验证传入的reqId为空时服务器能正确响应")
    assert json_data[ 'status'] == 400 and json_data['msg'] == 'reqId is empty'


def test_2_03():
    """验证传入的date为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo="method18",
                                       date=None,
                                       boardingGate="10",
                                       deviceCode="T1DJ001",
                                       gateNo="T1DJ001",
                                       cardId="",
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="passengerName",
                                       boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("验证传入的date为空时服务器能正确响应")
    assert json_data[ 'status'] == 400 and json_data['msg'] == 'date is empty'


def test_2_04():
    """验证传入的boardingGate为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo="method18",
                                       date=produce_flight_date(),
                                       boardingGate=None,
                                       deviceCode="T1DJ001",
                                       gateNo="T1DJ001",
                                       cardId="",
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="passengerName",
                                       boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("验证传入的boardingGate为空时服务器能正确响应")
    assert json_data['status'] == 400 and json_data['msg'] == 'boardingGate is empty'


def test_2_05():
    """验证传入的deviceCode为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo="method18",
                                       date=produce_flight_date(),
                                       boardingGate="11",
                                       deviceCode=None,
                                       gateNo="T1DJ001",
                                       cardId="",
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="passengerName",
                                       boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("验证传入的deviceCode为空时服务器能正确响应")
    assert json_data['status'] == 400 and json_data['msg'] == 'deviceCode is empty'


def test_2_06():
    """验证传入的gateNo为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo="method18",
                                       date=produce_flight_date(),
                                       boardingGate="11",
                                       deviceCode="T1DJ1",
                                       gateNo=None,
                                       cardId="",
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="passengerName",
                                       boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("验证传入的gateNo为空时服务器能正确响应")
    assert json_data['status'] == 400 and json_data['msg'] == 'gateNo is empty'


def test_2_07():
    """验证传入的scenePhoto为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo="method18",
                                       date=produce_flight_date(),
                                       boardingGate="11",
                                       deviceCode="T1DJ0011",
                                       gateNo="T1DJ1",
                                       cardId="",
                                       scenePhoto=None,
                                       sourceType="0",
                                       passengerName="passengerName",
                                       boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("验证传入的scenePhoto为空时服务器能正确响应")
    assert json_data['status'] == 0 and json_data['msg'] == 'Success'


def test_2_08():
    """验证传入的sourceType为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo="method18",
                                       date=produce_flight_date(),
                                       boardingGate="11",
                                       deviceCode="T1DJ0011",
                                       gateNo="T1DJ1",
                                       cardId="",
                                       scenePhoto=Base64Picture,
                                       sourceType=None,
                                       passengerName="passengerName",
                                       boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("验证传入的sourceType为空时服务器能正确响应")
    assert json_data['status'] == 400 and json_data['msg'] == 'sourceType is error'


if __name__ == '__main__':
    pytest.main(["-q", "test_w_boarding_fangxing.py"])




