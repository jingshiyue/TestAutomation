# coding:utf-8
# @author : chenkeyun
# @date : 20190302
import pytest
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture


def test_01_01(method_4):
    """有值机信息时，验证传入放行的参数，服务器能正常响应，以及数据库流水表数据的写入"""
    # 复核口  人工放行  报警接口
    # 安检的状态(
    # 0 人证1:1
    # 1 人工放行
    # 2闸机B门通过
    # 3-未知)
    time.sleep(1)
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo="511228199312134390",
                                      passengerName="passengerName",
                                      passengerEnglishName="passengerEnglishName",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo="flightnofang1",
                                      boardingNumber="001",
                                      sourceType="0")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data['status'] == 0 and json_data['msg'] == 'Success'
    print("有值机信息时，验证传入放行的参数，服务器能正常响应")


def test_01_02(method_5):
    """有值机信息时，验证传入报警的参数，服务器能正常响应"""
    # 复核口  人工放行  报警接口
    # 安检的状态(
    # 0 人证1:1
    # 1 人工放行
    # 2闸机B门通过
    # 3-未知)
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo="511228199312134391",
                                      passengerName="passengerName",
                                      passengerEnglishName="passengerEnglishName",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo="flightnofang2",
                                      boardingNumber="001",
                                      sourceType="1")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data['status'] == 0 and json_data['msg'] == 'Success'
    print("有值机信息时，验证传入报警的参数，服务器能正常响应")


def test_02_01():
    """验证传入证件号码为空值，航班号和登记序列号不为空值的参数，服务器能正常响应"""
    # 复核口  人工放行  报警接口
    # 安检的状态(
    # 0 人证1:1
    # 1 人工放行
    # 2闸机B门通过
    # 3-未知)
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo="",
                                      passengerName="passengerName",
                                      passengerEnglishName="passengerEnglishName",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo="flightnofang2",
                                      boardingNumber="001",
                                      sourceType="0")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 0 and json_data["msg"] == 'Success'
    print("验证传入证件号码为空值，航班号和登记序列号不为空值的参数，服务器能正常响应")


def test_02_02():
    """验证传入证件号码为不空值，航班号和登记序列号为空值的参数，服务器能正常响应,"""
    # 复核口  人工放行  报警接口
    # 安检的状态(
    # 0 人证1:1
    # 1 人工放行
    # 2闸机B门通过
    # 3-未知)
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo="511228199312134391",
                                      passengerName="passengerName",
                                      passengerEnglishName="passengerEnglishName",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo="",
                                      boardingNumber="",
                                      sourceType="0")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 0 and json_data["msg"] == 'Success'
    print("验证传入证件号码为不空值，航班号和登记序列号为空值的参数，服务器能正常响应")


def test_02_03():
    """验证传入的cardNo，flightNo，boardingNumber都为空值时服务器能正确响应"""
    # 复核口  人工放行  报警接口
    # 安检的状态(
    # 0 人证1:1
    # 1 人工放行
    # 2闸机B门通过
    # 3-未知)
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo="",
                                      passengerName="passengerName",
                                      passengerEnglishName="passengerEnglishName",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo="",
                                      boardingNumber="",
                                      sourceType="0")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data["status"] == 400 and json_data["msg"] == 'flightInfo and cardNo  is empty'
    print("验证传入的cardNo，flightNo，boardingNumber都为空值时服务器能正确响应")


def test_02_04():
    """验证传入的gateNo为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo=None,
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo="511228199312134390",
                                      passengerName="passengerName",
                                      passengerEnglishName="passengerEnglishName",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo="flightnofang1",
                                      boardingNumber="001",
                                      sourceType="0")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data['status'] == 400 and json_data['msg'] == 'badparams<gateNo is empty> '
    print("验证传入的gateNo为空时服务器能正确响应")


def test_02_05():
    """验证传入的deviceId为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo='T1AJ1',
                                      deviceId=None,
                                      scenePhoto=Base64Picture,
                                      cardNo="511228199312134390",
                                      passengerName="passengerName",
                                      passengerEnglishName="passengerEnglishName",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo="flightnofang1",
                                      boardingNumber="001",
                                      sourceType="0")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data['status'] == 400 and json_data['msg'] == 'badparams<deviceId is empty> '
    print("验证传入的deviceId为空时服务器能正确响应")


def test_02_06():
    """验证传入的passengerName为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo='T1AJ1',
                                      deviceId='T1AJ001',
                                      scenePhoto=Base64Picture,
                                      cardNo="511228199312134390",
                                      passengerName=None,
                                      passengerEnglishName="passengerEnglishName",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo="flightnofang1",
                                      boardingNumber="001",
                                      sourceType="0")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data['status'] == 0 and json_data['msg'] == 'Success'
    print("验证传入的passengerName为空时服务器能正确响应")


def test_02_07():
    """验证传入的passengerEnglishName为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo='T1AJ1',
                                      deviceId='T1AJ001',
                                      scenePhoto=Base64Picture,
                                      cardNo="511228199312134390",
                                      passengerName="45",
                                      passengerEnglishName=None,
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo="flightnofang1",
                                      boardingNumber="001",
                                      sourceType="0")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data['status'] == 0 and json_data['msg'] == 'Success'
    print("验证传入的passengerEnglishName为空时服务器能正确响应")


def test_02_08():
    """验证传入的securityStatus为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo='T1AJ1',
                                      deviceId='T1AJ001',
                                      scenePhoto=Base64Picture,
                                      cardNo="511228199312134390",
                                      passengerName="45",
                                      passengerEnglishName="name",
                                      securityStatus=None,
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo="flightnofang1",
                                      boardingNumber="001",
                                      sourceType="0")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data['status'] == 400 and json_data['msg'] == 'badparams<security status is empty> '
    print("验证传入的securityStatus为空时服务器能正确响应")


def test_02_09():
    """验证传入的securityPassTime为空时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo='T1AJ1',
                                      deviceId='T1AJ001',
                                      scenePhoto=Base64Picture,
                                      cardNo="511228199312134390",
                                      passengerName="45",
                                      passengerEnglishName="name",
                                      securityStatus=0,
                                      securityPassTime=None,
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo="flightnofang1",
                                      boardingNumber="001",
                                      sourceType="0")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data['status'] == 400 and json_data['msg'] == 'badparams<security passtime is empty> '
    print("验证传入的securityPassTime为空时服务器能正确响应")


def test_03_01():
    """验证传入的securityStatus不为0或1或2或3时服务器能正确响应"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo='T1AJ1',
                                      deviceId='T1AJ001',
                                      scenePhoto=Base64Picture,
                                      cardNo="511228199312134390",
                                      passengerName="45",
                                      passengerEnglishName="name",
                                      securityStatus="a",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo="flightnofang1",
                                      boardingNumber="001",
                                      sourceType="0")
    json_data = json.loads(res.text)
    print(json_data)
    assert json_data['status'] == 0 and json_data['msg'] == 'Success'
    print("验证传入的securityStatus不为0或1或2或3时服务器能正确响应")


if __name__ == '__main__':
    pytest.main(["-q", "test_review_man_fangxing_baojing.py"])
