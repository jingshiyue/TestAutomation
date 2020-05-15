# coding:utf-8
# @author : chenkeyun
# @date : 20190306
import pytest
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture


def test_1_01(qianzhi_1):
    """1:1安检通过，通道复核通过，登机口正常复核通过"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="001238198312134390",
                                     flightNo="qianzhi1",
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("1:1安检通过，通道复核通过，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 0 and \
           json_data["result"][0]['userInfo']['certificateNumber'] == "001238198312134390" and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']["passType"] == 0 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_02(qianzhi_2):
    """1:1安检通过，人工复核放行，登机口正常复核通过"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="002238198312134390",
                                     flightNo="qianzhi2",
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("1:1安检通过，通道复核通过，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 1 and \
           json_data["result"][0]['userInfo']['certificateNumber'] == "002238198312134390" and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']["passType"] == 0 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_03(qianzhi_3):
    """安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口正常复核通过"""
    card = "003238198312134390"
    flight = "qianzhi3"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId=card,
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 0 and \
           json_data["result"][0]['userInfo']['certificateNumber'] == card and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']["passType"] == 1 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_04(qianzhi_4):
    """安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口正常复核通过"""
    card = "004238198312134390"
    flight = "qianzhi4"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId=card,
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 1 and \
           json_data["result"][0]['userInfo']['certificateNumber'] == card and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']["passType"] == 1 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_05(qianzhi_5):
    """闸机B门通过安检，人工复核放行，登机口正常复核通过"""
    card = "005238198312134390"
    flight = "qianzhi5"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId=card,
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("闸机B门通过安检，人工复核放行，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 1 and \
           json_data["result"][0]['userInfo']['certificateNumber'] == card and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']["passType"] == 2 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_06(qianzhi_6):
    """闸机B门通过安检，自助闸机复核通过，登机口正常复核通过"""
    card = "006238198312134390"
    flight = "qianzhi6"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId=card,
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("闸机B门通过安检，人工复核放行，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 2 and \
           json_data["result"][0]['userInfo']['certificateNumber'] == card and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']["passType"] == 2 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_07(qianzhi_7):
    """验票通过，通道复核通过，登机口正常复核通过"""
    card = "007238198312134390"
    flight = "qianzhi7"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("验票通过，通道复核通过，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 0 and \
           json_data["result"][0]['userInfo']['certificateNumber'] == card and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']["passType"] == 3 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_08(qianzhi_8):
    """验票通过，人工复核放行，登机口正常复核通过"""
    card = "008238198312134390"
    flight = "qianzhi8"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("验票通过，人工复核放行，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 1 and \
           json_data["result"][0]['userInfo']['certificateNumber'] == card and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']["passType"] == 3 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_09(qianzhi_9):
    """中转，登机口正常复核通过"""
    card = "009238198312134390"
    flight = "qianzhi9"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("中转，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo'] == None and \
           json_data["result"][0]['transferInfo']['sourceType'] == 0


def test_1_10(qianzhi_10):
    """经停，登机口正常复核通过"""
    card = "010238198312134390"
    flight = "qianzhi10"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("中转，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo'] == None and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo'] == None and \
           json_data["result"][0]['transferInfo']['sourceType'] == 1


def test_1_11(qianzhi_11):
    """中转后退出去，1:1安检通过，通道复核通过，登机口正常复核通过"""
    card = "011238198312134390"
    flight = "qianzhi11"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="011238198312134390",
                                     flightNo="",
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("中转后退出去，1:1安检通过，通道复核通过，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']['passType'] == 0 and \
           json_data["result"][0]['userInfo']['certificateNumber'] == card and \
           json_data["result"][0]['boardingInfo'] == None and \
           json_data["result"][0]['securityInfo']["passType"] == 0 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_12(qianzhi_12):
    """中转后退出去，1:1安检通过，人工复核放行，登机口正常复核通过"""
    card = "012238198312134390"
    flight = "qianzhi12"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("中转后退出去，1:1安检通过，人工复核放行，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo'] == None and \
           json_data["result"][0]['boardingInfo']['passType'] == 0 and \
           json_data["result"][0]['securityInfo']["passType"] == 0 and \
           json_data["result"][0]['transferInfo']['sourceType'] == 0


def test_1_13(qianzhi_13):
    """中转后退出去，安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口正常复核通过"""
    card = "013238198312134390"
    flight = "qianzhi13"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("中转后退出去，安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo'] == None and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo'] == None and \
           json_data["result"][0]['transferInfo'] != None


def test_1_14(qianzhi_14):
    """中转后退出去，安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口正常复核通过"""
    card = "014238198312134390"
    flight = "qianzhi14"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("中转后退出去，安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo'] == None and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo'] == None and \
           json_data["result"][0]['transferInfo'] != None


def test_1_15(qianzhi_15):
    """中转后退出去，验票通过，通道复核通过，登机口正常复核通过"""
    card = "015238198312134390"
    flight = "qianzhi15"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("中转后退出去，安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']['passType'] == 0 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']['passType'] == 3 and \
           json_data["result"][0]['transferInfo'] != None


def test_1_16(qianzhi_16):
    """中转后退出去，验票通过，人工复核放行，登机口正常复核通过"""
    card = "016238198312134390"
    flight = "qianzhi16"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("中转后退出去，验票通过，人工复核放行，登机口正常复核通过")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']['passType'] == 1 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']['passType'] == 3 and \
           json_data["result"][0]['transferInfo']['sourceType'] == 0


def test_1_17(qianzhi_17):
    """1:1安检通过，通道复核通过，登机口人工放行"""
    card = "017238198312134390"
    flight = "qianzhi17"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("1:1安检通过，通道复核通过，登机口人工放行")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']['passType'] == 0 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 0 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_18(qianzhi_18):
    """1:1安检通过，人工复核放行，登机口人工放行"""
    card = "018238198312134390"
    flight = "qianzhi18"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("1:1安检通过，人工复核放行，登机口人工放行")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']['passType'] == 1 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 0 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_19(qianzhi_19):
    """安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口人工放行"""
    card = "019238198312134390"
    flight = "qianzhi19"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口人工放行")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']['passType'] == 0 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 1 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_20(qianzhi_20):
    """安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口人工放行"""
    card = "020238198312134390"
    flight = "qianzhi20"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口人工放行")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']['passType'] == 1 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 1 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_21(qianzhi_21):
    """安检人工放行（没有检测到人脸）通过，人工复核放行，登机口人工放行"""
    card = "021238198312134390"
    flight = "qianzhi21"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("安检人工放行（没有检测到人脸）通过，人工复核放行，登机口人工放行")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']['passType'] == 1 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 1 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_22(qianzhi_22):
    """闸机B门通过安检，人工复核放行，登机口人工放行"""
    card = "022238198312134390"
    flight = "qianzhi22"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("闸机B门通过安检，人工复核放行，登机口人工放行")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']['passType'] == 1 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 2 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_23(qianzhi_23):
    """闸机B门通过安检，自助闸机复核通过，登机口人工放行"""
    card = "023238198312134390"
    flight = "qianzhi23"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("闸机B门通过安检，自助闸机复核通过，登机口人工放行")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']['passType'] == 2 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 2 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_24(qianzhi_24):
    """验票通过，通道复核通过，登机口人工放行"""
    card = "024238198312134390"
    flight = "qianzhi24"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验票通过，通道复核通过，登机口人工放行""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']['passType'] == 0 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 3 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_25(qianzhi_25):
    """验票通过，人工复核放行，登机口人工放行"""
    card = "025238198312134390"
    flight = "qianzhi25"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验票通过，人工复核放行，登机口人工放行""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']['passType'] == 1 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 3 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_26(qianzhi_26):
    """中转，登机口人工放行"""
    card = "026238198312134390"
    flight = "qianzhi26"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""中转，登机口人工放行""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo'] == None and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo'] == None and \
           json_data["result"][0]['transferInfo']["sourceType"] == 0


def test_1_27(qianzhi_27):
    """经停，登机口人工放行"""
    card = "027238198312134390"
    flight = "qianzhi27"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""经停，登机口人工放行""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo'] == None and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo'] == None and \
           json_data["result"][0]['transferInfo']["sourceType"] == 1


def test_1_28(qianzhi_28):
    """中转后退出去，1:1安检通过，通道复核通过，登机口人工放行"""
    card = "028238198312134390"
    flight = "qianzhi28"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""中转后退出去，1:1安检通过，通道复核通过，登机口人工放行""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo'] == None and\
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 0 and \
           json_data["result"][0]['transferInfo']["sourceType"] == 0


def test_1_29(qianzhi_29):
    """中转后退出去，1:1安检通过，人工复核放行，登机口人工放行"""
    card = "029238198312134390"
    flight = "qianzhi29"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""中转后退出去，1:1安检通过，人工复核放行，登机口人工放行""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 0 and \
           json_data["result"][0]['transferInfo']["sourceType"] == 0


def test_1_30(qianzhi_30):
    """中转后退出去，验票通过，通道复核通过，登机口人工放行"""
    card = "030238198312134390"
    flight = "qianzhi30"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""中转后退出去，验票通过，通道复核通过，登机口人工放行""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 0 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 3 and \
           json_data["result"][0]['transferInfo']["sourceType"] == 0


def test_1_31(qianzhi_31):
    """中转后退出去，验票通过，人工复核放行，登机口人工放行"""
    card = "031238198312134390"
    flight = "qianzhi31"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""中转后退出去，验票通过，人工复核放行，登机口人工放行""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 1 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 3 and \
           json_data["result"][0]['transferInfo']["sourceType"] == 0


def test_1_32(qianzhi_32):
    """经停后退出去，验票通过，通道复核通过，登机口人工放行"""
    card = "032238198312134390"
    flight = "qianzhi32"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""经停后退出去，验票通过，通道复核通过，登机口人工放行""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 0 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 3 and \
           json_data["result"][0]['transferInfo']["sourceType"] == 1


@pytest.mark.skip(msg="需要确认是1-1通过后不能成功 还是由于人脸质量本身不好导致的")
def test_1_33(qianzhi_33):
    """1:1安检通过，通道复核通过，登机口人工报警"""
    card = "033338198312134390"
    flight = "qianzhi33"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""1:1安检通过，通道复核通过，登机口人工报警""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 0 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 0 and \
           json_data["result"][0]['transferInfo']["sourceType"] == 2


def test_1_34(qianzhi_34):
    """1:1安检通过，人工复核放行，登机口人工报警"""
    card = "034338198312134390"
    flight = "qianzhi34"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""1:1安检通过，人工复核放行，登机口人工报警""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 1 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']['passType'] == 0 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_35(qianzhi_35):
    """安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口人工报警"""
    card = "035338198312134390"
    flight = "qianzhi35"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口人工报警""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 0 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 2 and \
           json_data["result"][0]['securityInfo']['passType'] == 1 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_36(qianzhi_36):
    """安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口人工报警"""
    card = "036338198312134390"
    flight = "qianzhi36"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口人工报警""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 1 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 2 and \
           json_data["result"][0]['securityInfo']['passType'] == 1 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_37(qianzhi_37):
    """闸机B门通过安检，人工复核放行，登机口人工报警"""
    card = "037338198312134390"
    flight = "qianzhi37"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""闸机B门通过安检，人工复核放行，登机口人工报警""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 1 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 2 and \
           json_data["result"][0]['securityInfo']['passType'] == 2 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_38(qianzhi_38):
    """闸机B门通过安检，自助闸机复核通过，登机口人工报警"""
    card = "038338198312134390"
    flight = "qianzhi38"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""闸机B门通过安检，自助闸机复核通过，登机口人工报警""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 2 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 2 and \
           json_data["result"][0]['securityInfo']['passType'] == 2 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_39(qianzhi_39):
    """验票通过，通道复核通过，登机口人工报警"""
    card = "039338198312134390"
    flight = "qianzhi39"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验票通过，通道复核通过，登机口人工报警""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 0 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 2 and \
           json_data["result"][0]['securityInfo']['passType'] == 3 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_40(qianzhi_40):
    """验票通过，人工复核放行，登机口人工报警"""
    card = "040338198312134390"
    flight = "qianzhi40"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验票通过，人工复核放行，登机口人工报警""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 1 and \
           json_data["result"][0]['userInfo']['flightNo'] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 2 and \
           json_data["result"][0]['securityInfo']['passType'] == 3 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_41(qianzhi_41):
    """中转，登机口人工报警"""
    card = "041338198312134390"
    flight = "qianzhi41"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""中转，登机口人工报警""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo'] == None and \
           json_data["result"][0]['boardingInfo']["passType"] == 2 and \
           json_data["result"][0]['securityInfo'] == None and \
           json_data["result"][0]['transferInfo']["sourceType"] == 0


def test_1_42(qianzhi_42):
    """中转后退出去，1:1安检通过，通道复核通过，登机口人工报警"""
    card = "042338198312134390"
    flight = "qianzhi42"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""中转后退出去，1:1安检通过，通道复核通过，登机口人工报警""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo'] == None and \
           json_data["result"][0]['boardingInfo']["passType"] == 2 and \
           json_data["result"][0]['securityInfo'] == None and \
           json_data["result"][0]['transferInfo']["sourceType"] == 0


def test_1_43(qianzhi_43):
    """中转后退出去，安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口人工报警"""
    card = "043338198312134390"
    flight = "qianzhi43"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""中转后退出去，1:1安检通过，通道复核通过，登机口人工报警""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo']["flightNo"] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 2 and \
           json_data["result"][0]['securityInfo']["passType"] == 3 and \
           json_data["result"][0]['transferInfo']["sourceType"] == 0


def test_1_44(qianzhi_44):
    """中转后退出去，验票通过，通道复核通过，登机口人工报警"""
    card = "044338198312134390"
    flight = "qianzhi44"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""中转后退出去，验票通过，通道复核通过，登机口人工报警""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 0 and \
           json_data["result"][0]['userInfo']["flightNo"] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 2 and \
           json_data["result"][0]['securityInfo']["passType"] == 3 and \
           json_data["result"][0]['transferInfo']["sourceType"] == 0


def test_1_45(qianzhi_45):
    """中转后退出去，安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口人工报警"""
    card = "045338198312134390"
    flight = "qianzhi45"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""中转后退出去，安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口人工报警""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo']["flightNo"] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 2 and \
           json_data["result"][0]['securityInfo']["passType"] == 3 and \
           json_data["result"][0]['transferInfo']["sourceType"] == 0


def test_1_46(qianzhi_46):
    """1:1安检不通过，刷票通过,通道复核通过，登机口正常复核通过"""
    card = "046338198312134390"
    flight = "qianzhi46"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""1:1安检不通过，刷票通过,通道复核通过，登机口正常复核通过""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 0 and \
           json_data["result"][0]['userInfo']["flightNo"] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']["passType"] == 0 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_47(qianzhi_47):
    """经停后退出去，1:1安检不通过，人工复核放行，登机口正常复核通过"""
    card = "047338198312134390"
    flight = "qianzhi47"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""经停后退出去，1:1安检不通过，人工复核放行，登机口正常复核通过""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo']["flightNo"] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']["passType"] == 3 and \
           json_data["result"][0]['transferInfo']["sourceType"] == 0


def test_1_48(qianzhi_48):
    """1:1安检不通过，通道复核通过，登机口人工放行"""
    card = "048338198312134390"
    flight = "qianzhi48"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""1:1安检不通过，通道复核通过，登机口人工放行""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 0 and \
           json_data["result"][0]['userInfo']["flightNo"] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']["passType"] == 0 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_49(qianzhi_49):
    """验票通过，通道复核不通过，登机口正常复核通过"""
    card = "049338198312134390"
    flight = "qianzhi49"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验票通过，通道复核不通过，登机口正常复核通过""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo']["flightNo"] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']["passType"] == 3 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_50(qianzhi_50):
    """验票通过，人工复核报警，登机口正常复核通过"""
    card = "050338198312134390"
    flight = "qianzhi50"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验票通过，人工复核报警，登机口正常复核通过""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo']["passType"] == 3 and \
           json_data["result"][0]['userInfo']["flightNo"] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 0 and \
           json_data["result"][0]['securityInfo']["passType"] == 3 and \
           json_data["result"][0]['transferInfo'] == None


def test_1_51(qianzhi_51):
    """闸机B门通过安检，自助闸机复核不通过，登机口人工放行"""
    card = "051338198312134390"
    flight = "qianzhi51"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""闸机B门通过安检，自助闸机复核不通过，登机口人工放行""")
    assert json_data["status"] == 0 and \
           json_data["result"][0]['reviewInfo'] == None and \
           json_data["result"][0]['userInfo']["flightNo"] == flight and \
           json_data["result"][0]['boardingInfo']["passType"] == 1 and \
           json_data["result"][0]['securityInfo']["passType"] == 2 and \
           json_data["result"][0]['transferInfo'] == None


def test_2_1():
    """验证传入的reqId为空时服务器能正确响应"""
    card = "051338198312134390"
    flight = "qianzhi51"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=None,
                                     cardId=card,
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验证传入的reqId为空时服务器能正确响应""")
    assert json_data["status"] == 400 and json_data["msg"] == 'reqId is empty'


def test_2_2():
    """验证传入的cardId为空时服务器能正确响应"""
    card = "051338198312134390"
    flight = "qianzhi51"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId=None,
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验证传入的cardId为空时服务器能正确响应""")
    assert json_data["status"] == 0


def test_2_3():
    """验证传入的flightNo为空时服务器能正确响应"""
    card = "051338198312134390"
    flight = "qianzhi51"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId=card,
                                     flightNo=None,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验证传入的flightNo为空时服务器能正确响应""")
    assert json_data["status"] == 0


def test_2_4():
    """验证传入的flightDay为空时服务器能正确响应"""
    card = "051338198312134390"
    flight = "qianzhi51"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId=card,
                                     flightNo=flight,
                                     flightDay="",
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验证传入的flightDay为空时服务器能正确响应""")
    assert json_data["status"] == 400 and json_data["flightDay"] == 'flightDay is not empty'


def test_2_5():
    """验证传入的boardingNumber为空时服务器能正确响应"""
    card = "051338198312134390"
    flight = "qianzhi51"
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber=None
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验证传入的boardingNumber为空时服务器能正确响应""")
    assert json_data["status"] == 400 and json_data["msg"] == 'badparams<boardingNumber is empty> '


def test_3_1(qianzhi_3_1):
    """验证支持身份证号精确查询"""
    card="031238198312134391"
    flight="chaxuntest"
    n=40000
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId=card,
                                     flightNo=None,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验证支持身份证号精确查询""")
    assert json_data["status"] == 0 and json_data["result"] != None


def test_3_2(qianzhi_3_1):
    """验证支持航班号查询"""
    card="031238198312134391"
    flight="chaxuntest"
    n=40000
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId=None,
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验证支持航班号查询""")
    assert json_data["status"] == 0 and json_data["result"] != None


def test_3_3(qianzhi_3_1):
    """验证支持航班日查询"""
    card="031238198312134391"
    flight="chaxuntest"
    n=40000
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId=None,
                                     flightNo=None,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验证支持航班日查询"""+"实际测试不支持")
    assert json_data["status"] == 400


def test_3_4(qianzhi_3_1):
    """验证支持登机序列号查询"""
    card="031238198312134391"
    flight="chaxuntest"
    n=40000
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId=None,
                                     flightNo=None,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验证支持登机序列号查询"""+"实际测试不支持")
    assert json_data["status"] == 400


def test_3_5(qianzhi_3_1):
    """验证支持身份证号码和航班号混合查询"""
    card = "031238198312134391"
    flight = "chaxuntest"
    n= 40000
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_data_flowback_query(
                                     reqId=get_uuid(),
                                     cardId=card,
                                     flightNo=flight,
                                     flightDay=produce_flight_day(),
                                     boardingNumber="001"
    )
    json_data = json.loads(res.text)
    print(json_data)
    print("""验证支持航班号查询""")
    assert json_data["status"] == 0 and json_data["result"] != None

if __name__ == '__main__':
    pytest.main(["-q", "test_y_data_flowback_query.py"])