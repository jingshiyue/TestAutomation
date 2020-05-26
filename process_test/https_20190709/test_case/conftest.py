#!/usr/bin/python3
# Time : 2019/8/22 10:48 
# Author : zcl
import pytest,sys,pymysql,random
from https_20190709.common.common_method import *
from BaiTaAirport2_month.common import Idcardnumber
from BaiTaAirport2_month.msgQueue import Autosendlk
import logging,time
logger = logging.getLogger(__name__)

from datetime import datetime
import pytest
from py._xmlgen import html



@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    # cells.insert(1,html.th("Test_nodeid"))
    cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
    # cells.insert(1,html.td(report.nodeid))
    cells.pop()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")   #设置编码显示中文



###################################################################################
def read_from_config(confPath,secion_name, item_name):
    import configparser
    config = configparser.ConfigParser()
    config.read(confPath,encoding='utf-8')
    print("reids",config.get(secion_name, item_name))
    return config.get(secion_name, item_name)

def write_to_config(confPath,secion_name, item_name, value):
    import configparser
    config = configparser.ConfigParser()
    config.read(confPath,encoding='utf-8')
    if(config.has_section(secion_name) == False):
        config.add_section(secion_name)
    config.set(secion_name,item_name,value)
    with open(confPath, 'w', encoding="utf-8") as config_file:
        config.write(config_file)

@pytest.fixture()
def struct_pho():
    """
    初始化照片、特征
    :return:
    """
    pho_dic = {}
    largePhoto = to_base64(r"process_test\test_photoes\picture(现场照片)\1018.jpg")
    idx_pic = random.randint(402, 741)  #照片在这段401--743连续，照片可以重复使用，仅作标识使用
    #主要是特征值不能重复使用，照片可以重复使用.特征值和照片分开
    idx_feature = read_from_config(r"process_test\https_20190709\test_case\pytest.ini","config","idx_feature")
    idx_feature = int(idx_feature)
    idx_feature_increase = idx_feature + 1  #特征文件700--1087，连续
    write_to_config(r"process_test\https_20190709\test_case\pytest.ini","config","idx_feature",str(idx_feature_increase))
    cardPhoto = to_base64(os.path.join(r"process_test\test_photoes\picture(现场照片)", "%d.jpg" % (idx_pic-1)))
    scenePhoto = to_base64(os.path.join(r"process_test\test_photoes\picture(现场照片)","%d.jpg" % (idx_pic)))
    scenePhoto_fuhe = to_base64(os.path.join(r"process_test\test_photoes\picture(现场照片)","%d.jpg" % (idx_pic+1)))
    scenePhoto_fuhe_dengji = to_base64(os.path.join(r"process_test\test_photoes\picture(现场照片)","%d.jpg" % (idx_pic+2)))
    sceneFeature = read_feature(os.path.join(r"process_test\test_photoes\picture8k","%d.txt" % idx_feature))
    sceneFeature_2k = read_feature(os.path.join(r"process_test\test_photoes\picture2k","%d.txt" % idx_feature))
    cardFeature = read_feature(os.path.join(r"process_test\test_photoes\idcard8k","%d.txt" % idx_feature))
    pho_dic["scenePhoto"] = scenePhoto  #安检现场照
    pho_dic["scenePhoto_fuhe"] = scenePhoto_fuhe  #复核现场照
    pho_dic["scenePhoto_fuhe_dengji"] = scenePhoto_fuhe_dengji  #登机口复核现场照
    pho_dic["cardPhoto"] = cardPhoto
    pho_dic["largePhoto"] = largePhoto
    pho_dic["cardFeature"] = cardFeature
    pho_dic["sceneFeature"] = sceneFeature
    pho_dic["sceneFeature_2k"] = sceneFeature_2k
    logger.info(r"证件照: test_photoes\picture(现场照片)\%d.jpg" % (idx_pic-1) )
    logger.info(r"安检现场照: test_photoes\picture(现场照片)\%d.jpg" % (idx_pic))
    logger.info(r"复核现场照: test_photoes\picture(现场照片)\%d.jpg" % (idx_pic+1))
    logger.info(r"登机口复核现场照: test_photoes\picture(现场照片)\%d.jpg" % (idx_pic+2))
    return pho_dic


@pytest.fixture()  #安检系统表里创建数据
def insert_data_into_mysql(request):
    logger.info("insert_data_into_mysql")
    ########database config##
    host = "172.18.2.199"
    port = "3306"
    user = "root"
    password = "123456"
    db = "secsystem"
    charset = "utf8mb4"
    ######################
    try:
        # Connect to the database
        connection = pymysql.connect(
                                         host=host,
                                         port=int(port),
                                         user=user,
                                         password=password,
                                         db=db,
                                         charset=charset,
                                         cursorclass=pymysql.cursors.DictCursor)
    except pymysql.err.OperationalError as e:
        logger.error("Mysql Error %d: %s" % (e.args[0], e.args[1]))
    bdno = str(random.randint(1, 999))
    date = produce_flight_date()
    flight_no = produce_flight_number()
    if "bdno" in request.param:
        bdno = request.param["bdno"]
    if "date" in request.param:
        date = request.param["date"]
    if "flight_no" in request.param:
        flight_no = request.param["flight_no"]
    sql = "insert into sec_passenger_entity(bdno,date,flight,strt) values ('%s','%s','%s','het');" % (bdno, date, flight_no)
    with connection.cursor() as cursor:
        try:
            cursor.execute(sql)
            connection.commit()
            logger.info("表:sec_passenger_entity 插入数据成功")
        except:
            connection.rollback()
            logger.error("表:sec_passenger_entity 插入数据失败...")
            exit()
    return bdno,date,flight_no


@pytest.fixture()
def creat_zhiji_random(request):
    """
    在值机前先往表里（sec_passenger_entity）加入数据
    产生随机的值机人信息（起飞时间不管，主要是航班号，序号，身份证号码），信息在lkxx1.xml里
    """
    logger.info("creat_zhiji_random.............")
    import string
    # slcLetter = random.choice(string.ascii_uppercase)
    zhiji_dic = {}
    sex = random.randint(1, 2)
    idNo = Idcardnumber.get_random_id_number(sex=sex)
    lk_chkt = get_time_mmss()
    lk_outtime = get_flight_out_time()
    lk_date = produce_flight_date()
    lk_bdno  = str(random.randint(1,999))
    lk_seat = lk_bdno + "A"   #座位号
    lk_flight = produce_flight_number()
    lk_id = str(random.randint(1, 999))
    lk_inf = ""
    lk_cname = "大西瓜7"
    lk_ename = "DAXIGUA"
    lk_gateno = "10"  #需要指定登机口
    lk_desk = "CTU"
    if "lk_flight" in request.param:
        lk_flight = request.param["lk_flight"]
    if "lk_date" in request.param:
        lk_date = request.param["lk_date"]
    if "lk_outtime" in request.param:
        lk_outtime = request.param["lk_outtime"]
    if "lk_inf" in request.param:
        lk_inf = request.param["lk_inf"]
    if "lk_gateno" in request.param:
        lk_gateno = request.param["lk_gateno"]
    if "lk_cname" in request.param:
        lk_cname = request.param["lk_cname"]
    if "lk_ename" in request.param:
        lk_ename = request.param["lk_ename"]
    if "lk_seat" in request.param:
        lk_seat = request.param["lk_seat"]
    if "lk_desk" in request.param:
        lk_desk = request.param["lk_desk"]
    if "lk_bdno" in request.param:
        lk_bdno = request.param["lk_bdno"]
        lk_seat = lk_bdno + "A"  # 座位号
    Autosendlk.send_lkxx(
        lk_IsInternation="0",  # 1     是否国际 0否，1是，2未知
        lk_bdno=lk_bdno,  # 2     <!--2 10 登机序号 -->  3位
        lk_cardid=idNo,  # 4     证件号码
        lk_chkt=lk_chkt,  # 6     值机日期
        lk_cname=lk_cname,  # 8     旅客中文姓名80
        lk_date=lk_date,  # 9     9航班日期 8 YYYYMMDD 1
        lk_del="0",  # 10    是否删除 0否  1是
        lk_desk=lk_desk,  # 11    11目的地  机场三字代表码 1
        lk_ename=lk_ename,  # 12    旅客英文姓名
        lk_flight=lk_flight,  # 13    航班号 12    1
        lk_gateno=lk_gateno,  # 14    登机口号码 无意义k_g  1
        lk_id=lk_id,  # 15    旅客ID 主键 str 36
        lk_inf=lk_inf,  # 16    16婴儿标志3 INF带婴儿 “”表示未带婴儿
        lk_insur="0",  # 18    是否购保1
        lk_outtime=lk_outtime,  # 20    旅客起飞时间
        lk_sex=str(sex),  # 23    性别  1男性 2女性 0 未知
        lk_vip="0",
        lk_seat=lk_seat)  #座位号
    zhiji_dic["idNo"] = idNo #身份证号
    zhiji_dic["sex"] = sex #性别
    zhiji_dic["lk_flight"] = lk_flight #航班号
    zhiji_dic["lk_gateno"] = lk_gateno #登机口
    zhiji_dic["lk_date"] = lk_date #航班日期 8 YYYYMMDD
    zhiji_dic["lk_chkt"] = lk_chkt #值机日期 返回YYYYMMDDhhmmss的时间格式
    zhiji_dic["lk_inf"] = lk_inf
    zhiji_dic["lk_outtime"] = lk_outtime
    zhiji_dic["lk_cname"] = lk_cname
    zhiji_dic["lk_ename"] = lk_ename
    zhiji_dic["lk_seat"] = lk_seat #座位号
    zhiji_dic["lk_desk"] = lk_desk
    zhiji_dic["lk_bdno"] = lk_bdno  #登机序号
    time.sleep(2)
    return zhiji_dic




@pytest.fixture()
def creat_zhiji_byFlight(request):
    """
    在值机前先往表里（sec_passenger_entity）加入数据
    产生随机的值机人信息（起飞时间不管，主要是航班号，序号，身份证号码），信息在lkxx1.xml里
    """
    from process_test.https_20190709.test_case.data import flightInfo
    import string
    # slcLetter = random.choice(string.ascii_uppercase)
    zhiji_dic = {}
    sex = random.randint(1, 2)
    idNo = Idcardnumber.get_random_id_number(sex=sex)
    lk_chkt = get_time_mmss()
    lk_outtime = get_flight_out_time()
    lk_date = produce_flight_date()
    # lk_bdno  = str(random.randint(1,999))
    lk_bdno = read_from_config(r"process_test\https_20190709\test_case\pytest.ini","config","lk_bdno")
    lk_bdno = int(lk_bdno) + 1
    lk_bdno = str(lk_bdno).zfill(3)
    write_to_config(r"process_test\https_20190709\test_case\pytest.ini","config","lk_bdno",lk_bdno)
    lk_seat = lk_bdno + "A"   #座位号
    lk_flight = flightInfo["flight_no"]
    lk_id = str(random.randint(1, 999))
    lk_inf = ""
    lk_cname = "测试" + lk_bdno
    lk_ename = "DAXIGUA7"
    lk_gateno = flightInfo["bdno"]  #需要指定登机口
    lk_desk = "CTU"
    if "lk_outtime" in request.param:
        lk_outtime = request.param["lk_outtime"]
    if "lk_inf" in request.param:
        lk_inf = request.param["lk_inf"]
    if "lk_cname" in request.param:
        lk_cname = request.param["lk_cname"] + lk_bdno
    if "lk_ename" in request.param:
        lk_ename = request.param["lk_ename"]
    if "lk_seat" in request.param:
        lk_seat = request.param["lk_seat"]
    if "lk_desk" in request.param:
        lk_desk = request.param["lk_desk"]
    if "lk_bdno" in request.param:
        lk_bdno = request.param["lk_bdno"]
        lk_seat = lk_bdno + "A"  # 座位号
    Autosendlk.send_lkxx(
        lk_IsInternation="0",  # 1     是否国际 0否，1是，2未知
        lk_bdno=lk_bdno,  # 2     <!--2 10 登机序号 -->  3位
        lk_cardid=idNo,  # 4     证件号码
        lk_chkt=lk_chkt,  # 6     值机日期
        lk_cname=lk_cname,  # 8     旅客中文姓名80
        lk_date=lk_date,  # 9     9航班日期 8 YYYYMMDD 1
        lk_del="0",  # 10    是否删除 0否  1是
        lk_desk=lk_desk,  # 11    11目的地  机场三字代表码 1
        lk_ename=lk_ename,  # 12    旅客英文姓名
        lk_flight=lk_flight,  # 13    航班号 12    1
        lk_gateno=lk_gateno,  # 14    登机口号码 无意义k_g  1
        lk_id=lk_id,  # 15    旅客ID 主键 str 36
        lk_inf=lk_inf,  # 16    16婴儿标志3 INF带婴儿 “”表示未带婴儿
        lk_insur="0",  # 18    是否购保1
        lk_outtime=lk_outtime,  # 20    旅客起飞时间
        lk_sex=str(sex),  # 23    性别  1男性 2女性 0 未知
        lk_vip="0",
        lk_seat=lk_seat)  #座位号
    zhiji_dic["idNo"] = idNo #身份证号
    zhiji_dic["sex"] = sex #性别
    zhiji_dic["lk_flight"] = lk_flight #航班号
    zhiji_dic["lk_gateno"] = lk_gateno #登机口
    zhiji_dic["lk_date"] = lk_date #航班日期 8 YYYYMMDD
    zhiji_dic["lk_chkt"] = lk_chkt #值机日期 返回YYYYMMDDhhmmss的时间格式
    zhiji_dic["lk_inf"] = lk_inf
    zhiji_dic["lk_outtime"] = lk_outtime
    zhiji_dic["lk_cname"] = lk_cname
    zhiji_dic["lk_ename"] = lk_ename
    zhiji_dic["lk_seat"] = lk_seat #座位号
    zhiji_dic["lk_desk"] = lk_desk
    zhiji_dic["lk_bdno"] = lk_bdno  #登机序号
    time.sleep(1)
    return zhiji_dic


def creat_zhiji_byFlight_useInFunc(**request):
    """
    产生随机的值机人信息（起飞时间不管，主要是航班号，序号，身份证号码），信息在lkxx1.xml里
    可接收航班信息
    """
    import string
    # slcLetter = random.choice(string.ascii_uppercase)
    zhiji_dic = {}
    sex = random.randint(1, 2)
    idNo = Idcardnumber.get_random_id_number(sex=sex)
    lk_chkt = get_time_mmss()
    lk_outtime = get_flight_out_time()
    lk_date = produce_flight_date()
    lk_bdno  = str(random.randint(1,999))
    lk_seat = lk_bdno + "A"   #座位号
    lk_flight = produce_flight_number()
    lk_id = str(random.randint(1, 999))
    lk_inf = ""
    lk_cname = "大西瓜7"
    lk_ename = "DAXIGUA7"
    lk_desk = "CTU"
    lk_gateno = "10"
    # print(request)  #{'request': {'flight_no': 'CA8128', 'lk_gateno': '10', 'lk_bdno': '02'}}
    # print({"request.keys():":list(request["request"].keys())})
    # print(type())
    if "lk_flight" in list(request["request"].keys()):
        lk_flight = request["request"]["lk_flight"]
    if "lk_gateno" in list(request["request"].keys()):
        lk_gateno = request["request"]["lk_gateno"]
    if "lk_outtime" in list(request["request"].keys()):
        lk_outtime = request["request"]["lk_outtime"]
    if "lk_inf" in list(request["request"].keys()):
        lk_inf = request["request"]["lk_inf"]
    if "lk_cname" in list(request["request"].keys()):
        lk_cname = request["request"]["lk_cname"]
    if "lk_ename" in list(request["request"].keys()):
        lk_ename = request["request"]["lk_ename"]
    if "lk_seat" in list(request["request"].keys()):
        lk_seat = request["request"]["lk_seat"]
    if "lk_desk" in list(request["request"].keys()):
        lk_desk = request["request"]["lk_desk"]
    if "lk_bdno" in list(request["request"].keys()):
        lk_bdno = request["request"]["lk_bdno"]
        lk_seat = lk_bdno + "A"  # 座位号
    Autosendlk.send_lkxx(
        lk_IsInternation="0",  # 1     是否国际 0否，1是，2未知
        lk_bdno=lk_bdno,  # 2     <!--2 10 登机序号 -->  3位
        lk_cardid=idNo,  # 4     证件号码
        lk_chkt=lk_chkt,  # 6     值机日期
        lk_cname=lk_cname,  # 8     旅客中文姓名80
        lk_date=lk_date,  # 9     9航班日期 8 YYYYMMDD 1
        lk_del="0",  # 10    是否删除 0否  1是
        lk_desk=lk_desk,  # 11    11目的地  机场三字代表码 1
        lk_ename=lk_ename,  # 12    旅客英文姓名
        lk_flight=lk_flight,  # 13    航班号 12    1
        lk_gateno=lk_gateno,  # 14    登机口号码 无意义k_g  1
        lk_id=lk_id,  # 15    旅客ID 主键 str 36
        lk_inf=lk_inf,  # 16    16婴儿标志3 INF带婴儿 “”表示未带婴儿
        lk_insur="0",  # 18    是否购保1
        lk_outtime=lk_outtime,  # 20    旅客起飞时间
        lk_sex=str(sex),  # 23    性别  1男性 2女性 0 未知
        lk_vip="0",
        lk_seat=lk_seat)  #座位号
    zhiji_dic["idNo"] = idNo #身份证号
    zhiji_dic["sex"] = sex #性别
    zhiji_dic["lk_flight"] = lk_flight #航班号
    zhiji_dic["lk_gateno"] = lk_gateno #登机口
    zhiji_dic["lk_date"] = lk_date #航班日期 8 YYYYMMDD
    zhiji_dic["lk_chkt"] = lk_chkt #值机日期 返回YYYYMMDDhhmmss的时间格式
    zhiji_dic["lk_inf"] = lk_inf
    zhiji_dic["lk_outtime"] = lk_outtime
    zhiji_dic["lk_cname"] = lk_cname
    zhiji_dic["lk_ename"] = lk_ename
    zhiji_dic["lk_seat"] = lk_seat #座位号
    zhiji_dic["lk_desk"] = lk_desk
    zhiji_dic["lk_bdno"] = lk_bdno  #登机序号
    time.sleep(1)
    return zhiji_dic

def get_useful_flight(gateNoList:list):
    """
    return 从172.18.2.199 redis中获取可用测试的航班
    parm:gateNoList 登机口列表 如["02","02A","03","03A",]
    """
    import redis
    # from process_test.https_20190709.test_case.data import config
    try:
        sr=redis.StrictRedis(host=read_from_config(r"process_test\https_20190709\test_case\pytest.ini","config","redis"), port=6379, db=2,password='cigit')
    except Exception as e:
        print(e)
        raise e
    import time
    flightTemp = "plan-" + time.strftime("%Y-%m-%d",time.localtime()) #plan-2020-05-08
    for gate in gateNoList:
        flightNum = flightTemp + "-" + gate  #plan-2020-05-08-02
        zsetRes = sr.zrange(flightNum,0,-1,withscores=True)   #当天每个登机口里的航班
        for flight in zsetRes:
            try:
                detailFlight = "status-" + time.strftime("%Y-%m-%d",time.localtime()) + "-" + str(flight[0][:6])[2:-1]  #status-2020-05-08-3U8747
                hRes = sr.hmget(detailFlight, "flightDate","depTimeJ","twoFlightNo","gateNo","status")  #航班详细信息
                depTimeJ = str(hRes[0])[2:-1] + " " + str(hRes[1])[2:-1]   #redis中预计起飞时间， 日期 + 时间:2020-05-09 0725
                timeArray = time.strptime(depTimeJ, "%Y-%m-%d %H%M")
                timeStamp = int(time.mktime(timeArray))
                offsetTime = int((timeStamp-time.time())/60)  #redis中的起飞时间与现在时间的时间差(min)
                if offsetTime > 60*1:    #时间差大于1小时
                    return hRes   #byte类型 [b'2020-05-09', b'1150', b'CA1118', b'14', b'0']
            except Exception as e:
                print(e)
                print("该次格式化航班出错，将跳过筛选...")
        flightNum = flightTemp
    