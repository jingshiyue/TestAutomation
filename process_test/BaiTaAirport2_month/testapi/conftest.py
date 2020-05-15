# coding:utf-8
from BaiTaAirport2_month.common.mysql_class import DataBase
from BaiTaAirport2_month.msgQueue.Autosendlk import *
import pytest
from BaiTaAirport2_month.API.AirportProcess import *
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture
shujuku = DataBase("192.168.1.105", 3306, "root", "123456", "htbusyinfo")
board_no_list = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028', '029', '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041', '042', '043', '044', '045', '046', '047', '048', '049', '050', '051', '052', '053', '054', '055', '056', '057', '058', '059', '060', '061', '062', '063', '064', '065', '066', '067', '068', '069', '070', '071', '072', '073', '074', '075', '076', '077', '078', '079', '080', '081', '082', '083', '084', '085', '086', '087', '088', '089', '090', '091', '092', '093', '094', '095', '096', '097', '098', '099', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298', '299', '300', '301', '302', '303', '304', '305', '306', '307', '308', '309', '310', '311', '312', '313', '314', '315', '316', '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328', '329', '330', '331', '332', '333', '334', '335', '336', '337', '338', '339', '340', '341', '342', '343', '344', '345', '346', '347', '348', '349', '350', '351', '352', '353', '354', '355', '356', '357', '358', '359', '360', '361', '362', '363', '364', '365', '366', '367', '368', '369', '370', '371', '372', '373', '374', '375', '376', '377', '378', '379', '380', '381', '382', '383', '384', '385', '386', '387', '388', '389', '390', '391', '392', '393', '394', '395', '396', '397', '398', '399', '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422', '423', '424', '425', '426', '427', '428', '429', '430', '431', '432', '433', '434', '435', '436', '437', '438', '439', '440', '441', '442', '443', '444', '445', '446', '447', '448', '449', '450', '451', '452', '453', '454', '455', '456', '457', '458', '459', '460', '461', '462', '463', '464', '465', '466', '467', '468', '469', '470', '471', '472', '473', '474', '475', '476', '477', '478', '479', '480', '481', '482', '483', '484', '485', '486', '487', '488', '489', '490', '491', '492', '493', '494', '495', '496', '497', '498', '499', '500']


@pytest.fixture()
def zhiji():
    send_lkxx(lk_cardid="500238199312134391",
              lk_chkt=get_time_mmss(),
              lk_cname="ckytest",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight="lkflightno",
              lk_id="1234567891",
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")


@pytest.fixture()
def zhiji_two():
    send_lkxx(lk_cardid="100238199312134390",
              lk_chkt=get_time_mmss(),
              lk_cname="ckytest",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight="flight1",
              lk_id="1234567891",
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    send_lkxx(lk_cardid="100238199312134390",
              lk_chkt=get_time_mmss(),
              lk_cname="ckytest",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight="flight2",
              lk_id="1234567891",
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)


@pytest.fixture()
def zhiji_to_manopcheck():
    """先值机，然后再多次安检1：1比对不通过"""
    # 开始先值机
    send_lkxx(lk_cardid="500238199312154390",
              lk_chkt=get_time_mmss(),
              lk_cname="ckytest",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight="manopcheck",
              lk_id="1234567891",
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    a = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard="500238199312154390",
                     nameZh="铁塔",
                     nameEn="CHENKEYUN",
                     age=25,
                     sex=1,
                     birthDate=get_birthday("300238199312134390"),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    b = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard="500238199312154390",
                     nameZh="铁塔",
                     nameEn="CHENKEYUN",
                     age=25,
                     sex=1,
                     birthDate=get_birthday("300238199312134390"),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5100)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanli8k_features+"/"+str(5101)+".txt"))
    print(a.text+"\n"+b.text)

    yield
    sql1 = "select certificate_number FROM face_review_features WHERE certificate_number='500238199312154390';"
    data = shujuku.find_all(sql1)
    if data[0] !=None:
        try:
            if data[0][0] == '500238199312154390':
                pass
        except Exception as e:
            print("异常"+str(e)+str(data))
    else:
        print("此人通过人工放行后没有入库")
        assert 1 == 0


@pytest.fixture()
def method_1():
    """服务复核流程。先进行安检"""
    # 进行人证1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard="700238199312134390",
                     nameZh="铁塔",
                     nameEn="CHENKEYUN",
                     age=25,
                     sex=1,
                     birthDate=get_birthday("300238199312134390"),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(5200)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(5200)+".txt"))
    print(res.text)
    time.sleep(1)


@pytest.fixture()
def method_2():
    """传入刷机票的人脸信息"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                       flightNo="hangban001",
                                       faceImage=Base64Picture,
                                       gateNo="T1AJ1",
                                       deviceCode="T1AJ001",
                                       boardingNumber="010",
                                       seatId="001",
                                       startPort="HET",
                                       flightDay=produce_flight_day(),
                                       faceFeature=get_txt(shiwanli8k_features+"/"+str(5201)+".txt"),
                                       kindType="0")
    print(res.text)


@pytest.fixture()
def method_3():
    """传入刷票人工放行"""
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                       flightNo="hangban002",
                                       faceImage=Base64Picture,
                                       gateNo="T1AJ1",
                                       deviceCode="T1AJ001",
                                       boardingNumber="012",
                                       seatId="001",
                                       startPort="HET",
                                       flightDay=produce_flight_day(),
                                       faceFeature=get_txt(shiwanli8k_features+"/"+str(5202)+".txt"),
                                       kindType="1")
    print(res.text)


@pytest.fixture()
def method_4():
    """传入值机信息,以便进行人工放行"""
    send_lkxx(lk_cardid="511228199312134390",
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight="flightnofang1",
              lk_id="1234567891",
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    yield
    sql1 = "select certificate_number FROM aib_security_check_review_1_3 WHERE certificate_number='511228199312134390';"
    data = shujuku.find_all(sql1)
    try:

        if data[0][0] == '511228199312134390':
            pass
        else:
            raise Exception
    except Exception as e:
        assert 1 == 0
        print("异常为：%s" % (str(e)))


@pytest.fixture()
def method_5():
    """传入值机信息,以便复核口进行人工报警"""
    send_lkxx(lk_cardid="511228199312134391",
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight="flightnofang2",
              lk_id="1234567891",
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")


@pytest.fixture()
def method_6():
    yield
    time.sleep(1)
    sql_data = "select flight_number,boarding_number,source_type,channel_code FROM face_review_features WHERE boarding_number='001' AND flight_number='test006';"
    data = shujuku.find_all(sql_data)
    try:
        flight_no = data[0][0]
        boarding_no = data[0][1]
        source_type = data[0][2]
        channel_code = data[0][3]
        if flight_no == 'test006' and boarding_no == '001' and source_type == 2 and channel_code == "T1zz1":
            print("success")
        else:
            print("failed")
            raise Exception
    except Exception as e:
        print("失败"+str(data))
        assert 1 == 0


@pytest.fixture()
def method_7():
    yield
    time.sleep(1)
    sql_data = "select flight_number,boarding_number,source_type FROM face_review_features WHERE boarding_number='001' AND flight_number='test007';"
    data = shujuku.find_all(sql_data)
    try:
        flight_no = data[0][0]
        boarding_no = data[0][1]
        source_type = data[0][2]
        print(flight_no, boarding_no, source_type)
        if flight_no == 'test007' and boarding_no == '001' and source_type == 3:
            print("success")
        else:
            print("failed")
            pytest.fail()
    except Exception as e:
        print("失败"+str(data))
        assert 1 == 0


@pytest.fixture()
def method_8():
    """服务于登机口复核建库人数查询接口 ,500本地，0中转，0经停
    :return:
    """
    # 调用500次人工验票接口
    for i in range(0, 500):
        res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                       flightNo="bendiflight",
                                       faceImage=Base64Picture,
                                       gateNo="T1AJ1",
                                       deviceCode="T1AJ001",
                                       boardingNumber=board_no_list[i],
                                       seatId="001",
                                       startPort="HET",
                                       flightDay=produce_flight_day(),
                                       faceFeature=get_txt(shiwanli8k_features+"/"+str(i+20000)+".txt"),
                                       kindType=0)   # 0为刷票
    time.sleep(3)
    # 开始调用登机口建库接口
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo="bendiflight",
                                 date=produce_flight_date(),
                                 boardingGate="01",
                                 deviceCode="T1DJ001",
                                 number=500,
                                 outTime=get_flight_out_time(1))


@pytest.fixture()
def method_9():
    """
    服务于登机口复核建库人数查询接口 ,0本地，500中转，0经停
    :return:
    """
    # 调用500次中转接口
    for i in range(0, 500):
        res = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(reqId=get_uuid(),
                                             flightNo="zhongzhuanflight",
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ002",
                                             gateNo="T1ZZ2",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber=board_no_list[i],
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(i+20700)+".txt"),
                                             sourceType="0")   # 0是中转

    time.sleep(3)
    # 开始调用建库接口
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo="zhongzhuanflight",
                                 date=produce_flight_date(),
                                 boardingGate="02",
                                 deviceCode="T1DJ002",
                                 number=500,
                                 outTime=get_flight_out_time(1))


@pytest.fixture()
def method_10():
    """
    服务于登机口复核建库人数查询接口 ,0本地，0中转，500经停
    :return:
    """
    # 调用500次中转接口
    for i in range(0, 500):
        res = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(reqId=get_uuid(),
                                             flightNo="jingtingflight",
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ003",
                                             gateNo="T1ZZ3",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber=board_no_list[i],
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(i+21300)+".txt"),
                                             sourceType="1")   # 0是中转,1是经停

    time.sleep(3)
    # 开始调用建库接口
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo="jingtingflight",
                                 date=produce_flight_date(),
                                 boardingGate="03",
                                 deviceCode="T1DJ003",
                                 number=500,
                                 outTime=get_flight_out_time(1))


@pytest.fixture()
def method_11():
    """
    服务于登机口复核建库人数查询接口 ,498本地，1中转，1经停
    :return:
    """
    # 开始调用安检人工刷票接口
    for i in range(0, 498):
        res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                       flightNo="hunheflight",
                                       faceImage=Base64Picture,
                                       gateNo="T1AJ1",
                                       deviceCode="T1AJ001",
                                       boardingNumber=board_no_list[i],
                                       seatId="001",
                                       startPort="HET",
                                       flightDay=produce_flight_day(),
                                       faceFeature=get_txt(shiwanli8k_features+"/"+str(i+22000)+".txt"),
                                       kindType=0)   # 0为刷票
    time.sleep(2)
    # 开始调用 一次中转
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(reqId=get_uuid(),
                                             flightNo="hunheflight",
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ004",
                                             gateNo="T1ZZ4",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber=board_no_list[498],
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(498+21300)+".txt"),
                                             sourceType="0")   # 0是中转,1是经停
    # 开始调用一次经停
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(reqId=get_uuid(),
                                             flightNo="hunheflight",
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ004",
                                             gateNo="T1ZZ4",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber=board_no_list[499],
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(499+21300)+".txt"),
                                             sourceType="1")   # 0是中转,1是经停
    # 开始调用建库接口
    time.sleep(3)
    res33 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo="hunheflight",
                                 date=produce_flight_date(),
                                 boardingGate="03",
                                 deviceCode="T1DJ004",
                                 number=500,
                                 outTime=get_flight_out_time(1))


@pytest.fixture()
def method_12():
    # 先进行一次中转
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(reqId=get_uuid(),
                                             flightNo="zhengchangflight",
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ004",
                                             gateNo="T1ZZ4",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber=board_no_list[0],
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(25000)+".txt"),
                                             sourceType="0")   # 0是中转,1是经停
    time.sleep(2)
    # 调用建库接口
    res33 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo="zhengchangflight",
                                 date=produce_flight_date(),
                                 boardingGate="06",
                                 deviceCode="T1DJ004",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)


@pytest.fixture()
def method_13(n=25003):
    # 先值机
    send_lkxx(lk_cardid="222238199312134392",
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight="zhengchang1",
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 通过安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard="222238199312134392",
                     nameZh="cky",
                     nameEn="cky",
                     age=26,
                     sex=1,
                     birthDate=get_birthday("300238199312134390"),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("anjian1:1"+res.text)
    time.sleep(2)
    # 经过安检复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    print("anjianfuhe"+res3.text)
    time.sleep(2)

    # 登机口复核建库
    res4 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo="zhengchang1",
                                 date=produce_flight_date(),
                                 boardingGate="07",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(2)


@pytest.fixture()
def method_14(n=25004):
    # 先值机
    send_lkxx(lk_cardid="222238199312134393",
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight="zhengchang2",
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 通过安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard="222238199312134393",
                     nameZh="cky",
                     nameEn="cky",
                     age=26,
                     sex=1,
                     birthDate=get_birthday("300238199312134390"),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("anjian1:1"+res.text)
    time.sleep(2)
    # 经过复核人工放行
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(
        reqId=get_uuid(), gateNo="T1AF1", deviceId="T1AF001", scenePhoto=Base64Picture, cardNo="222238199312134393",
                                     passengerName="cky", passengerEnglishName="cky", securityStatus="0",
                                     securityPassTime=get_time_mmss(), securityGateNo="T1AJ1", securityDeviceNo="T1AJ001",
                                     flightNo="zhengchang2", boardingNumber="001",
                                     sourceType="0"
    )
    print("anjianfuhe"+res3.text)
    time.sleep(2)

    # 登机口复核建库
    res4 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo="zhengchang2",
                                 date=produce_flight_date(),
                                 boardingGate="08",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    print(res4.text)
    time.sleep(2)


@pytest.fixture()
def method_15(n=25005):
    # 先值机
    send_lkxx(lk_cardid="222238199312134394",
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight="zhengchang3",
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 通过安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard="222238199312134394",
                     nameZh="cky",
                     nameEn="cky",
                     age=26,
                     sex=1,
                     birthDate=get_birthday("300238199312134390"),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("anjian1:1"+res.text)
    time.sleep(2)
    # 经过复核人工报警
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(
        reqId=get_uuid(), gateNo="T1AF1", deviceId="T1AF001", scenePhoto=Base64Picture, cardNo="222238199312134394",
                                     passengerName="cky", passengerEnglishName="cky", securityStatus="0",
                                     securityPassTime=get_time_mmss(), securityGateNo="T1AJ1", securityDeviceNo="T1AJ001",
                                     flightNo="zhengchang3", boardingNumber="001",
                                     sourceType="1"
    )
    print("anjianfuhe"+res3.text)
    time.sleep(2)

    # 登机口复核建库
    res4 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo="zhengchang3",
                                 date=produce_flight_date(),
                                 boardingGate="09",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    print(res4.text)
    time.sleep(2)


@pytest.fixture()
def method_16():
    # 值机进行中转通道
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(reqId=get_uuid(),
                                             flightNo="method16",
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ004",
                                             gateNo="T1ZZ4",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber=board_no_list[0],
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(25000)+".txt"),
                                             sourceType="0")   # 0是中转,1是经停
    print(res1.text)
    time.sleep(2)
    # 进行建库
    res4 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo="method16",
                                 date=produce_flight_date(),
                                 boardingGate="10",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    print(res4.text)
    time.sleep(2)


@pytest.fixture()
def method_17():
    # 值机进行中转通道
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(reqId=get_uuid(),
                                             flightNo="method17",
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ004",
                                             gateNo="T1ZZ4",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber=board_no_list[0],
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(25000)+".txt"),
                                             sourceType="0")   # 0是中转,1是经停
    print(res1.text)
    time.sleep(2)
    # 进行建库
    res4 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo="method16",
                                 date=produce_flight_date(),
                                 boardingGate="11",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    print(res4.text)
    time.sleep(2)


@pytest.fixture()
def qianzhi_1(idcard="001238198312134390",
              flight="qianzhi1",
              n=30001):
    """1:1安检通过，通道复核通过，登机口正常复核通过"""
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("anjian1:1"+"\n"+res.text)
    time.sleep(2)
    # 开始进行通道复核
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
                              reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 开始进行登机口建库
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_2(idcard="002238198312134390",
              flight="qianzhi2",
              n=30002):
    """1:1安检通过，人工复核放行，登机口正常复核通过"""
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("anjian1:1"+"\n"+res.text)
    time.sleep(2)
    # 开始进行通道复核
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)
    # 进行通道复核放行
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 开始进行登机口建库
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_3(idcard="003238198312134390",
              flight="qianzhi3",
              n=30003):
    """安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口正常复核通过"""
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("anjian1:1"+"\n"+res.text)

    # 安检人工放行
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard=idcard,
                                          nameZh="cky",
                                          nameEn="cky",
                                          age=get_age(idcard),
                                          sex="1",
                                          birthDate=get_birthday(idcard),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    print("安检人工放行"+"\n"+res.text)
    time.sleep(2)
    # 开始进行通道复核
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
                              reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)
    # 进行通道复核放行
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 开始进行登机口建库
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_4(idcard="004238198312134390",
              flight="qianzhi4",
              n=30004):
    """安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口正常复核通过"""
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("anjian1:1"+"\n"+res.text)

    # 安检人工放行
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard=idcard,
                                          nameZh="cky",
                                          nameEn="cky",
                                          age=get_age(idcard),
                                          sex="1",
                                          birthDate=get_birthday(idcard),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    print("安检人工放行"+"\n"+res.text)
    time.sleep(2)
    # 开始进行通道复核
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)
    # 进行通道复核放行
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 开始进行登机口建库
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_5(idcard="005238198312134390",
              flight="qianzhi5",
              n=30005):
    """闸机B门通过安检，人工复核放行，登机口正常复核通过"""
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard=idcard,
                                                                                      nameZh="cky",
                                                                                      nameEn="cky",
                                                                                      age=get_age(idcard),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday(idcard),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-20230202",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    print("经过闸门A"+"\n"+res_a.text)
    time.sleep(1)

    # 进行闸门B
    res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard=idcard,
                                     nameZh="cky",
                                     nameEn="cky",
                                     age=get_age(idcard),
                                     sex="1",
                                     birthDate=get_birthday(idcard),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("anjian1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)
    # 开始进行通道复核
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)


    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 开始进行登机口建库
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_6(idcard="006238198312134390",
              flight="qianzhi6",
              n=30006):
    """闸机B门通过安检，自助闸机复核通过，登机口正常复核通过"""
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard=idcard,
                                                                                      nameZh="cky",
                                                                                      nameEn="cky",
                                                                                      age=get_age(idcard),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday(idcard),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-20230202",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    print("经过闸门A"+"\n"+res_a.text)
    time.sleep(1)

    # 进行闸门B
    res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard=idcard,
                                     nameZh="cky",
                                     nameEn="cky",
                                     age=get_age(idcard),
                                     sex="1",
                                     birthDate=get_birthday(idcard),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("anjian1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)
    # 开始进行通道复核
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)


    # 进行通道复核放行
    time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
                                   gateno="T1AF1",
                                   deviceid="T1AF001",
                                   scenephoto=Base64Picture,
                                   scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))

    # 开始进行登机口建库
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_7(idcard="007238198312134390",
              flight="qianzhi7",
              n=30007):
    """验票通过，通道复核通过，登机口正常复核通过"""
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("anjian1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                       flightNo=flight,
                                       faceImage=Base64Picture,
                                       gateNo="T1AJ1",
                                       deviceCode="T1AJ001",
                                       boardingNumber="001",
                                       seatId="001",
                                       startPort="HET",
                                       flightDay=produce_flight_day(),
                                       faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                       kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)
    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
                              reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)


    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 开始进行登机口建库
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_8(idcard="008238198312134390",
              flight="qianzhi8",
              n=30008):
    """验票通过，人工复核放行，登机口正常复核通过"""
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("anjian1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                       flightNo=flight,
                                       faceImage=Base64Picture,
                                       gateNo="T1AJ1",
                                       deviceCode="T1AJ001",
                                       boardingNumber="001",
                                       seatId="001",
                                       startPort="HET",
                                       flightDay=produce_flight_day(),
                                       faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                       kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)
    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)


    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 开始进行登机口建库
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_9(idcard="009238198312134390",
              flight="qianzhi9",
              n=30009):
    """验票通过，人工复核放行，登机口正常复核通过"""
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("anjian1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                    flightNo=flight,
    #                                    faceImage=Base64Picture,
    #                                    gateNo="T1AJ1",
    #                                    deviceCode="T1AJ001",
    #                                    boardingNumber="001",
    #                                    seatId="001",
    #                                    startPort="HET",
    #                                    flightDay=produce_flight_day(),
    #                                    faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                    kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)
    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)


    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)


    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_10(idcard="010238198312134390",
              flight="qianzhi10",
              n=30010):
    """验票通过，人工复核放行，登机口正常复核通过"""
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("anjian1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                    flightNo=flight,
    #                                    faceImage=Base64Picture,
    #                                    gateNo="T1AJ1",
    #                                    deviceCode="T1AJ001",
    #                                    boardingNumber="001",
    #                                    seatId="001",
    #                                    startPort="HET",
    #                                    flightDay=produce_flight_day(),
    #                                    faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                    kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)
    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)


    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="1"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)


    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_11(idcard="011238198312134390",
              flight="qianzhi11",
              n=30011):
    """中转后退出去，1:1安检通过，通道复核通过，登机口正常复核通过"""
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("anjian1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                    flightNo=flight,
    #                                    faceImage=Base64Picture,
    #                                    gateNo="T1AJ1",
    #                                    deviceCode="T1AJ001",
    #                                    boardingNumber="001",
    #                                    seatId="001",
    #                                    startPort="HET",
    #                                    flightDay=produce_flight_day(),
    #                                    faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                    kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)
    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
                              reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)


    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)


    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_12(idcard="012238198312134390",
              flight="qianzhi12",
              n=30012):
    """中转后退出去，1:1安检通过，人工复核放行，登机口正常复核通过"""
    # 中转采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                    flightNo=flight,
    #                                    faceImage=Base64Picture,
    #                                    gateNo="T1AJ1",
    #                                    deviceCode="T1AJ001",
    #                                    boardingNumber="001",
    #                                    seatId="001",
    #                                    startPort="HET",
    #                                    flightDay=produce_flight_day(),
    #                                    faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                    kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)
    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_13(idcard="012338198312134390",
              flight="qianzhi13",
              n=30013):
    """中转后退出去，安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口正常复核通过"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard=idcard,
                                          nameZh="cky",
                                          nameEn="cky",
                                          age=get_age(idcard),
                                          sex="1",
                                          birthDate=get_birthday(idcard),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    print("安检人工放行"+"\n"+res.text)
    time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                    flightNo=flight,
    #                                    faceImage=Base64Picture,
    #                                    gateNo="T1AJ1",
    #                                    deviceCode="T1AJ001",
    #                                    boardingNumber="001",
    #                                    seatId="001",
    #                                    startPort="HET",
    #                                    flightDay=produce_flight_day(),
    #                                    faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                    kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)
    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
                              reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_14(idcard="014238198312134390",
              flight="qianzhi14",
              n=30014):
    """中转后退出去，安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口正常复核通过"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard=idcard,
                                          nameZh="cky",
                                          nameEn="cky",
                                          age=get_age(idcard),
                                          sex="1",
                                          birthDate=get_birthday(idcard),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    print("安检人工放行"+"\n"+res.text)
    time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                    flightNo=flight,
    #                                    faceImage=Base64Picture,
    #                                    gateNo="T1AJ1",
    #                                    deviceCode="T1AJ001",
    #                                    boardingNumber="001",
    #                                    seatId="001",
    #                                    startPort="HET",
    #                                    flightDay=produce_flight_day(),
    #                                    faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                    kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)
    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_15(idcard="015238198312134390",
              flight="qianzhi15",
              n=30015):
    """中转后退出去，验票通过，通道复核通过，登机口正常复核通过"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                       flightNo=flight,
                                       faceImage=Base64Picture,
                                       gateNo="T1AJ1",
                                       deviceCode="T1AJ001",
                                       boardingNumber="001",
                                       seatId="001",
                                       startPort="HET",
                                       flightDay=produce_flight_day(),
                                       faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                       kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)
    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
                              reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_16(idcard="016238198312134390",
              flight="qianzhi16",
              n=30016):
    """中转后退出去，验票通过，人工复核放行，登机口正常复核通过"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                       flightNo=flight,
                                       faceImage=Base64Picture,
                                       gateNo="T1AJ1",
                                       deviceCode="T1AJ001",
                                       boardingNumber="001",
                                       seatId="001",
                                       startPort="HET",
                                       flightDay=produce_flight_day(),
                                       faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                       kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)
    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    time.sleep(1)
    print("登机口建库"+"\n"+res2.text)
    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_17(idcard="017238198312134390",
              flight="qianzhi17",
              n=30017):
    """1:1安检通过，通道复核通过，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                    flightNo=flight,
    #                                    faceImage=Base64Picture,
    #                                    gateNo="T1AJ1",
    #                                    deviceCode="T1AJ001",
    #                                    boardingNumber="001",
    #                                    seatId="001",
    #                                    startPort="HET",
    #                                    flightDay=produce_flight_day(),
    #                                    faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                    kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)
    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
                              reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo=flight,
                                       date=produce_flight_date(),
                                       boardingGate="22",
                                       deviceCode="T1DJ0011",
                                       gateNo="T1DJ1",
                                       cardId=idcard,
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="cky",
                                       boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_18(idcard="018238198312134390",
              flight="qianzhi18",
              n=30018):
    """1:1安检通过，人工复核放行，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                    flightNo=flight,
    #                                    faceImage=Base64Picture,
    #                                    gateNo="T1AJ1",
    #                                    deviceCode="T1AJ001",
    #                                    boardingNumber="001",
    #                                    seatId="001",
    #                                    startPort="HET",
    #                                    flightDay=produce_flight_day(),
    #                                    faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                    kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo=flight,
                                       date=produce_flight_date(),
                                       boardingGate="22",
                                       deviceCode="T1DJ0011",
                                       gateNo="T1DJ1",
                                       cardId=idcard,
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="cky",
                                       boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_19(idcard="019238198312134390",
              flight="qianzhi19",
              n=30019):
    """安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard=idcard,
                                          nameZh="cky",
                                          nameEn="cky",
                                          age=get_age(idcard),
                                          sex="1",
                                          birthDate=get_birthday(idcard),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    print("安检人工放行"+"\n"+res.text)
    time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                    flightNo=flight,
    #                                    faceImage=Base64Picture,
    #                                    gateNo="T1AJ1",
    #                                    deviceCode="T1AJ001",
    #                                    boardingNumber="001",
    #                                    seatId="001",
    #                                    startPort="HET",
    #                                    flightDay=produce_flight_day(),
    #                                    faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                    kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
                              reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo=flight,
                                       date=produce_flight_date(),
                                       boardingGate="22",
                                       deviceCode="T1DJ0011",
                                       gateNo="T1DJ1",
                                       cardId=idcard,
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="cky",
                                       boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_20(idcard="020238198312134390",
              flight="qianzhi20",
              n=30020):
    """安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard=idcard,
                                          nameZh="cky",
                                          nameEn="cky",
                                          age=get_age(idcard),
                                          sex="1",
                                          birthDate=get_birthday(idcard),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    print("安检人工放行"+"\n"+res.text)
    time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                    flightNo=flight,
    #                                    faceImage=Base64Picture,
    #                                    gateNo="T1AJ1",
    #                                    deviceCode="T1AJ001",
    #                                    boardingNumber="001",
    #                                    seatId="001",
    #                                    startPort="HET",
    #                                    flightDay=produce_flight_day(),
    #                                    faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                    kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo=flight,
                                       date=produce_flight_date(),
                                       boardingGate="22",
                                       deviceCode="T1DJ0011",
                                       gateNo="T1DJ1",
                                       cardId=idcard,
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="cky",
                                       boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_21(idcard="021238198312134390",
              flight="qianzhi21",
              n=30021):
    """安检人工放行（没有检测到人脸）通过，人工复核放行，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard=idcard,
                                          nameZh="cky",
                                          nameEn="cky",
                                          age=get_age(idcard),
                                          sex="1",
                                          birthDate=get_birthday(idcard),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature="",
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    print("安检人工放行"+"\n"+res.text)
    time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                    flightNo=flight,
    #                                    faceImage=Base64Picture,
    #                                    gateNo="T1AJ1",
    #                                    deviceCode="T1AJ001",
    #                                    boardingNumber="001",
    #                                    seatId="001",
    #                                    startPort="HET",
    #                                    flightDay=produce_flight_day(),
    #                                    faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                    kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo=flight,
                                       date=produce_flight_date(),
                                       boardingGate="22",
                                       deviceCode="T1DJ0011",
                                       gateNo="T1DJ1",
                                       cardId=idcard,
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="cky",
                                       boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_22(idcard="022238198312134390",
              flight="qianzhi22",
              n=30022):
    """闸机B门通过安检，人工复核放行，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard=idcard,
                                                                                      nameZh="cky",
                                                                                      nameEn="cky",
                                                                                      age=get_age(idcard),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday(idcard),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-20230202",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    print("经过闸门A"+"\n"+res_a.text)
    time.sleep(1)

    # 进行闸门B
    res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard=idcard,
                                     nameZh="cky",
                                     nameEn="cky",
                                     age=get_age(idcard),
                                     sex="1",
                                     birthDate=get_birthday(idcard),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                    flightNo=flight,
    #                                    faceImage=Base64Picture,
    #                                    gateNo="T1AJ1",
    #                                    deviceCode="T1AJ001",
    #                                    boardingNumber="001",
    #                                    seatId="001",
    #                                    startPort="HET",
    #                                    flightDay=produce_flight_day(),
    #                                    faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                    kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo=flight,
                                       date=produce_flight_date(),
                                       boardingGate="22",
                                       deviceCode="T1DJ0011",
                                       gateNo="T1DJ1",
                                       cardId=idcard,
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="cky",
                                       boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_23(idcard="023238198312134390",
              flight="qianzhi23",
              n=30023):
    """闸机B门通过安检，自助闸机复核通过，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard=idcard,
                                                                                      nameZh="cky",
                                                                                      nameEn="cky",
                                                                                      age=get_age(idcard),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday(idcard),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-20230202",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    print("经过闸门A"+"\n"+res_a.text)
    time.sleep(1)

    # 进行闸门B
    res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard=idcard,
                                     nameZh="cky",
                                     nameEn="cky",
                                     age=get_age(idcard),
                                     sex="1",
                                     birthDate=get_birthday(idcard),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                    flightNo=flight,
    #                                    faceImage=Base64Picture,
    #                                    gateNo="T1AJ1",
    #                                    deviceCode="T1AJ001",
    #                                    boardingNumber="001",
    #                                    seatId="001",
    #                                    startPort="HET",
    #                                    flightDay=produce_flight_day(),
    #                                    faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                    kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #                           reqId=get_uuid(),
    #                           gateNo="T1AF1",
    #                           deviceId="T1AF001",
    #                           scenePhoto=Base64Picture,
    #                           sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    time.sleep(2)
    res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
                                   gateno="T1AF1",
                                   deviceid="T1AF001",
                                   scenephoto=Base64Picture,
                                   scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo=flight,
                                       date=produce_flight_date(),
                                       boardingGate="22",
                                       deviceCode="T1DJ0011",
                                       gateNo="T1DJ1",
                                       cardId=idcard,
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="cky",
                                       boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_24(idcard="024238198312134390",
              flight="qianzhi24",
              n=30024):
    """验票通过，通道复核通过，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                       flightNo=flight,
                                       faceImage=Base64Picture,
                                       gateNo="T1AJ1",
                                       deviceCode="T1AJ001",
                                       boardingNumber="001",
                                       seatId="001",
                                       startPort="HET",
                                       flightDay=produce_flight_day(),
                                       faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                       kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
                              reqId=get_uuid(),
                              gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=Base64Picture,
                              sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                 flightNo=flight,
                                 date=produce_flight_date(),
                                 boardingGate="22",
                                 deviceCode="T1DJ001",
                                 number=1,
                                 outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
                                       flightNo=flight,
                                       date=produce_flight_date(),
                                       boardingGate="22",
                                       deviceCode="T1DJ0011",
                                       gateNo="T1DJ1",
                                       cardId=idcard,
                                       scenePhoto=Base64Picture,
                                       sourceType="0",
                                       passengerName="cky",
                                       boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_25(idcard="025238198312134390",
              flight="qianzhi25",
              n=30025):
    """验票通过，人工复核放行，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="0",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_26(idcard="026238198312134390",
              flight="qianzhi26",
              n=30026):
    """中转，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="0",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(2)


@pytest.fixture()
def qianzhi_27(idcard="027238198312134390",
              flight="qianzhi27",
              n=30027):
    """经停，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="1"
    )
    print("开始进行经停刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    a = get_uuid()
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=a,
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="0",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text+str(a))
    time.sleep(1)


@pytest.fixture()
def qianzhi_28(idcard="028238198312134390",
              flight="qianzhi28",
              n=30028):
    """中转后退出去，1:1安检通过，通道复核通过，登机口人工放行"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF001",
        scenePhoto=Base64Picture,
        sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="0",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_29(idcard="029238198312134390",
              flight="qianzhi29",
              n=30029):
    """中转后退出去，1:1安检通过，人工复核放行，登机口人工放行"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="0",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_30(idcard="030238198312134390",
              flight="qianzhi30",
              n=30030):
    """中转后退出去，验票通过，通道复核通过，登机口人工放行"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF001",
        scenePhoto=Base64Picture,
        sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="0",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_31(idcard="031238198312134390",
              flight="qianzhi31",
              n=30031):
    """中转后退出去，验票通过，人工复核放行，登机口人工放行"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="0",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_32(idcard="032238198312134390",
              flight="qianzhi32",
              n=30032):
    """经停后退出去，验票通过，通道复核通过，登机口人工放行"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="1"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF001",
        scenePhoto=Base64Picture,
        sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="0",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_33(idcard="033238198312134390",
              flight="qianzhi33",
              n=30033):
    """1:1安检通过，通道复核通过，登机口人工报警"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    print("先值机")

    # 闸门A-B进行安检
    # time.sleep(1)
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("安检1:1"+"\n"+res.text)
    time.sleep(1)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(3)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF001",
        scenePhoto=Base64Picture,
        sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="1",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_34(idcard="034238198312134390",
              flight="qianzhi34",
              n=30034):
    """1:1安检通过，人工复核放行，登机口人工报警"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    print("先值机")
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="1",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工报警"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_35(idcard="035238198312134390",
              flight="qianzhi35",
              n=30035):
    """安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口人工报警"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard=idcard,
                                          nameZh="cky",
                                          nameEn="cky",
                                          age=get_age(idcard),
                                          sex="1",
                                          birthDate=get_birthday(idcard),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    print("安检人工放行"+"\n"+res.text)
    time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF001",
        scenePhoto=Base64Picture,
        sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="1",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工报警"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_36(idcard="036238198312134390",
              flight="qianzhi36",
              n=30036):
    """安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口人工报警"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard=idcard,
                                          nameZh="cky",
                                          nameEn="cky",
                                          age=get_age(idcard),
                                          sex="1",
                                          birthDate=get_birthday(idcard),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    print("安检人工放行"+"\n"+res.text)
    time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="1",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工报警"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_37(idcard="037238198312134390",
              flight="qianzhi37",
              n=30037):
    """闸机B门通过安检，人工复核放行，登机口人工报警"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    print("先值机")
    time.sleep(1)
    # 闸门A-B进行安检
    res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard=idcard,
                                                                                      nameZh="cky",
                                                                                      nameEn="cky",
                                                                                      age=get_age(idcard),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday(idcard),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-20230202",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    print("经过闸门A"+"\n"+res_a.text)
    time.sleep(1)

    # 进行闸门B
    res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard=idcard,
                                     nameZh="cky",
                                     nameEn="cky",
                                     age=get_age(idcard),
                                     sex="1",
                                     birthDate=get_birthday(idcard),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="1",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工报警"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_38(idcard="038238198312134390",
              flight="qianzhi38",
              n=30038):
    """经停，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    print("值机")
    # 闸门A-B进行安检
    res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard=idcard,
                                                                                      nameZh="cky",
                                                                                      nameEn="cky",
                                                                                      age=get_age(idcard),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday(idcard),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-20230202",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    print("经过闸门A"+"\n"+res_a.text)
    time.sleep(1)

    # 进行闸门B
    res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard=idcard,
                                     nameZh="cky",
                                     nameEn="cky",
                                     age=get_age(idcard),
                                     sex="1",
                                     birthDate=get_birthday(idcard),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    time.sleep(2)
    res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
                                   gateno="T1AF1",
                                   deviceid="T1AF001",
                                   scenephoto=Base64Picture,
                                   scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="1",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工报警"+"\n"+res_board_fang.text)
    time.sleep(1)

@pytest.fixture()
def qianzhi_39(idcard="039238198312134390",
              flight="qianzhi39",
              n=30039):
    """验票通过，通道复核通过，登机口人工报警"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    print("先值机")
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF001",
        scenePhoto=Base64Picture,
        sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="1",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工baojing"+"\n"+res_board_fang.text)
    time.sleep(1)

@pytest.fixture()
def qianzhi_40(idcard="040238198312134390",
              flight="qianzhi40",
              n=30040):
    """验票通过，人工复核放行，登机口人工报警"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    time.sleep(1)
    print("先值机")
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="1",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工报警"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_41(idcard="041238198312134390",
              flight="qianzhi41",
              n=30041):
    """中转，登机口人工报警"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId="",
        scenePhoto=Base64Picture,
        sourceType="1",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工报警"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_42(idcard="042238198312134390",
              flight="qianzhi42",
              n=30042):
    """中转后退出去，1:1安检通过，通道复核通过，登机口人工报警"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF001",
        scenePhoto=Base64Picture,
        sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId="",
        scenePhoto=Base64Picture,
        sourceType="1",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工报警"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_43(idcard="043238198312134390",
              flight="qianzhi43",
              n=30043):
    """中转后退出去，安检人工放行（有绑定照片检测到人脸）通过，通道复核通过，登机口人工报警"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard=idcard,
                                          nameZh="cky",
                                          nameEn="cky",
                                          age=get_age(idcard),
                                          sex="1",
                                          birthDate=get_birthday(idcard),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    print("安检人工放行"+"\n"+res.text)
    time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF001",
        scenePhoto=Base64Picture,
        sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId="",
        scenePhoto=Base64Picture,
        sourceType="1",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工报警"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_44(idcard="044238198312134390",
              flight="qianzhi44",
              n=30044):
    """中转后退出去，验票通过，通道复核通过，登机口人工报警"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF001",
        scenePhoto=Base64Picture,
        sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId="",
        scenePhoto=Base64Picture,
        sourceType="1",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_45(idcard="045238198312134390",
              flight="qianzhi45",
              n=30045):
    """中转后退出去，安检人工放行（有绑定照片检测到人脸）通过，人工复核放行，登机口人工报警"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
                                          gateNo="T1AJ1",
                                          deviceId="T1AJ001",
                                          cardType="0",
                                          idCard=idcard,
                                          nameZh="cky",
                                          nameEn="cky",
                                          age=get_age(idcard),
                                          sex="1",
                                          birthDate=get_birthday(idcard),
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto=Base64Picture,
                                          sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                          cardPhoto=Base64Picture,
                                          cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId="",
        scenePhoto=Base64Picture,
        sourceType="1",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工baojing"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_46(idcard="046238198312134390",
              flight="qianzhi46",
              n=30046):
    """1:1安检不通过，刷票通过,通道复核通过，登机口正常复核通过"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    print("开始值机")
    time.sleep(1)

    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(1)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("安检1:1不通过"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF001",
        scenePhoto=Base64Picture,
        sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)

    # 进行登机口人工放行
    # res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
    #     reqId=get_uuid(),
    #     flightNo=flight,
    #     date=produce_flight_date(),
    #     boardingGate="22",
    #     deviceCode="T1DJ0011",
    #     gateNo="T1DJ1",
    #     cardId=idcard,
    #     scenePhoto=Base64Picture,
    #     sourceType="0",
    #     passengerName="cky",
    #     boardingNumber="001"
    # )
    # print("登机口人工放行"+"\n"+res_board_fang.text)
    # time.sleep(1)


@pytest.fixture()
def qianzhi_47(idcard="047238198312134390",
              flight="qianzhi47",
              n=30047):
    """经停后退出去，1:1安检不通过，人工复核放行，登机口正常复核通过"""
    # 中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # print("先开始值机")
    # time.sleep(1)
    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(2)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="0",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="0")
    print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)

    # 进行登机口人工放行
    # res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
    #     reqId=get_uuid(),
    #     flightNo=flight,
    #     date=produce_flight_date(),
    #     boardingGate="22",
    #     deviceCode="T1DJ0011",
    #     gateNo="T1DJ1",
    #     cardId=idcard,
    #     scenePhoto=Base64Picture,
    #     sourceType="0",
    #     passengerName="cky",
    #     boardingNumber="001"
    # )
    # print("登机口人工放行"+"\n"+res_board_fang.text)
    # time.sleep(1)


@pytest.fixture()

def qianzhi_48(idcard="048238198312134390",
              flight="qianzhi48",
              n=30048):
    """1:1安检不通过，通道复核通过，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    print("先开始值机")
    time.sleep(1)


    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard=idcard,
                     nameZh="cky",
                     nameEn="cky",
                     age=get_age(idcard),
                     sex=1,
                     birthDate=get_birthday(idcard),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(1)+".txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF001",
        scenePhoto=Base64Picture,
        sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    )
    print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="0",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_49(idcard="049238198312134390",
              flight="qianzhi49",
              n=30049):
    """验票通过，通道复核不通过，登机口正常复核通过"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    print("先开始值机")
    time.sleep(1)

    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
        reqId=get_uuid(),
        gateNo="T1AF1",
        deviceId="T1AF001",
        scenePhoto=Base64Picture,
        sceneFeature=get_txt(shiwanli2k_features+"/"+str(50000)+".txt")
    )
    print("通道复核不通过"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)

    # 进行登机口人工放行
    # res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
    #     reqId=get_uuid(),
    #     flightNo=flight,
    #     date=produce_flight_date(),
    #     boardingGate="22",
    #     deviceCode="T1DJ0011",
    #     gateNo="T1DJ1",
    #     cardId=idcard,
    #     scenePhoto=Base64Picture,
    #     sourceType="0",
    #     passengerName="cky",
    #     boardingNumber="001"
    # )
    # print("登机口人工放行"+"\n"+res_board_fang.text)
    # time.sleep(1)


@pytest.fixture()
def qianzhi_50(idcard="050238198312134390",
              flight="qianzhi50",
              n=30050):
    """验票通过，人工复核报警，登机口正常复核通过"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    print("先开始值机")
    time.sleep(1)

    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
                                                                                                   flightNo=flight,
                                                                                                   faceImage=Base64Picture,
                                                                                                   gateNo="T1AJ1",
                                                                                                   deviceCode="T1AJ001",
                                                                                                   boardingNumber="001",
                                                                                                   seatId="001",
                                                                                                   startPort="HET",
                                                                                                   flightDay=produce_flight_day(),
                                                                                                   faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                                                                                   kindType=0)
    print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    time.sleep(2)
    res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
                                      gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=Base64Picture,
                                      cardNo=idcard,
                                      passengerName="cky",
                                      passengerEnglishName="cky",
                                      securityStatus="3",
                                      securityPassTime=get_time_mmss(),
                                      securityGateNo="T1AJ1",
                                      securityDeviceNo="T1AJ001",
                                      flightNo=flight,
                                      boardingNumber="001",
                                      sourceType="1")
    print("通道复核baojing"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)

    # 进行登机口人工放行
    # res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
    #     reqId=get_uuid(),
    #     flightNo=flight,
    #     date=produce_flight_date(),
    #     boardingGate="22",
    #     deviceCode="T1DJ0011",
    #     gateNo="T1DJ1",
    #     cardId=idcard,
    #     scenePhoto=Base64Picture,
    #     sourceType="0",
    #     passengerName="cky",
    #     boardingNumber="001"
    # )
    # print("登机口人工放行"+"\n"+res_board_fang.text)
    # time.sleep(1)


@pytest.fixture()
def qianzhi_51(idcard="051238198312134390",
              flight="qianzhi51",
              n=30051):
    """闸机B门通过安检，自助闸机复核不通过，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    print("先开始值机")
    time.sleep(1)

    # 闸门A-B进行安检
    res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard=idcard,
                                                                                      nameZh="cky",
                                                                                      nameEn="cky",
                                                                                      age=get_age(idcard),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday(idcard),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-20230202",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    print("经过闸门A"+"\n"+res_a.text)
    time.sleep(1)

    # 进行闸门B
    res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard=idcard,
                                     nameZh="cky",
                                     nameEn="cky",
                                     age=get_age(idcard),
                                     sex="1",
                                     birthDate=get_birthday(idcard),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    time.sleep(2)
    res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
                                   gateno="T1AF1",
                                   deviceid="T1AF001",
                                   scenephoto=Base64Picture,
                                   scenefeature=get_txt(shiwanli2k_features+"/"+str(50001)+".txt"))
    print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId="",
        scenePhoto=Base64Picture,
        sourceType="0",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)


@pytest.fixture()
def qianzhi_3_1(idcard="031238198312134391",
              flight="chaxuntest",
              n=40000):
    """配置全流程"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    send_lkxx(lk_cardid=idcard,
              lk_chkt=get_time_mmss(),
              lk_cname="cky",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight=flight,
              lk_id=get_uuid(),
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")
    print("先开始值机")
    time.sleep(1)

    # 闸门A-B进行安检
    res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
                                                                                      gateNo="T1AJ1",
                                                                                      deviceId="T1AJ1",
                                                                                      cardType=0,
                                                                                      idCard=idcard,
                                                                                      nameZh="cky",
                                                                                      nameEn="cky",
                                                                                      age=get_age(idcard),
                                                                                      sex=0,
                                                                                      birthDate=get_birthday(idcard),
                                                                                      address="重庆市",
                                                                                      certificateValidity="20120101-20230202",
                                                                                      nationality="China",
                                                                                      ethnic="汉族",
                                                                                      contactWay="123456",
                                                                                      cardPhoto=Base64Picture,
                                                                                      fId=get_uuid())
    print("经过闸门A"+"\n"+res_a.text)
    time.sleep(1)

    # 进行闸门B
    res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
                                     gateNo="T1AJ1",
                                     deviceId="T1AJ001",
                                     cardType="0",
                                     idCard=idcard,
                                     nameZh="cky",
                                     nameEn="cky",
                                     age=get_age(idcard),
                                     sex="1",
                                     birthDate=get_birthday(idcard),
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto=Base64Picture,
                                     sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                     cardPhoto=Base64Picture,
                                     cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    time.sleep(2)
    res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
                                   gateno="T1AF1",
                                   deviceid="T1AF001",
                                   scenephoto=Base64Picture,
                                   scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
                                faceImage=Base64Picture,
                                faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
                                deviceCode="T1DJ001",
                                boardingGate="22",
                                flightNo=flight,
                                flightDay=produce_flight_date()   # （yyyyMMdd）
    )
    print("登机口复核"+"\n"+res3.text)
    time.sleep(1)

    # # 进行登机口人工放行
    # res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
    #     reqId=get_uuid(),
    #     flightNo=flight,
    #     date=produce_flight_date(),
    #     boardingGate="22",
    #     deviceCode="T1DJ0011",
    #     gateNo="T1DJ1",
    #     cardId=idcard,
    #     scenePhoto=Base64Picture,
    #     sourceType="0",
    #     passengerName="cky",
    #     boardingNumber="001"
    # )
    # print("登机口人工放行"+"\n"+res_board_fang.text)
    # time.sleep(1)

if __name__ == '__main__':
    # sql1 = "select flight_number,boarding_number,source_type FROM face_review_features WHERE boarding_number='001' AND flight_number='test006';"
    # data = shujuku.find_all(sql1)
    # print(data)
    # method_2()
    list1 = [1, 2, 3, 4, 6, 1, 2, 6]
    a = list1.count(4)
    print(a)
    method_13()