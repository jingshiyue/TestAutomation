#!/usr/bin/python3
# Time : 2019/8/22 10:48 
# Author : zcl
import pytest,sys,pymysql,random
from https_20190709.common.common_method import *
from BaiTaAirport2_month.common import Idcardnumber
from BaiTaAirport2_month.msgQueue import Autosendlk
import logging
#log surpport

@pytest.fixture()
def struct_pho():
    """
    初始化照片、特征
    :return:
    """
    pho_dic = {}
    largePhoto = to_base64(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\1018.jpg")
    idx_pic = random.randint(10, 74)
    # idx_pic = 31
    idx_feature = random.randint(10, 74)
    # idx_feature = 31
    idx_pic = idx_feature

    cardPhoto = to_base64(os.path.join(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)", "%d.jpg" % (idx_pic-1)))
    scenePhoto = to_base64(os.path.join(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)","%d.jpg" % (idx_pic+0)))
    scenePhoto_fuhe = to_base64(os.path.join(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)","%d.jpg" % (idx_pic+1)))
    sceneFeature = read_feature(os.path.join(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture8k","%d.txt" % idx_feature))
    sceneFeature_2k = read_feature(os.path.join(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture2k","%d.txt" % idx_feature))
    cardFeature = read_feature(os.path.join(r"D:\workfile\zhongkeyuan_workspace\test_photoes\idcard8k","%d.txt" % idx_feature))
    pho_dic["scenePhoto"] = scenePhoto
    pho_dic["scenePhoto_fuhe"] = scenePhoto_fuhe
    pho_dic["cardPhoto"] = cardPhoto
    pho_dic["largePhoto"] = largePhoto
    pho_dic["cardFeature"] = cardFeature
    pho_dic["sceneFeature"] = sceneFeature
    pho_dic["sceneFeature_2k"] = sceneFeature_2k
    logging.info("cardPhoto: D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\%d.jpg" % (idx_pic-1) )
    logging.info(r"scenePhoto: D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\%d.jpg" % (idx_pic))
    logging.info("scenePhoto_fuhe: D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\%d.jpg" % (idx_pic+1))
    return pho_dic


@pytest.fixture()  #安检系统表里创建数据
def insert_data_into_mysql(request):
    logging.info("insert_data_into_mysql")
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
        logging.error("Mysql Error %d: %s" % (e.args[0], e.args[1]))
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
            logging.info("表:sec_passenger_entity 插入数据成功")
        except:
            connection.rollback()
            logging.error("表:sec_passenger_entity 插入数据失败...")
            exit()
    return bdno,date,flight_no


@pytest.fixture()
def creat_zhiji_random(request):
    """
    在值机前先往表里（sec_passenger_entity）加入数据
    产生随机的值机人信息（起飞时间不管，主要是航班号，序号，身份证号码），信息在lkxx1.xml里
    """
    logging.info("creat_zhiji_random.............")
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
    from .test_process import dataInfo   #{'flight_no': 'DR6562', 'bdno': '02', 'date': '2020-05-09'}
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
    lk_flight = dataInfo["flight_no"]
    lk_id = str(random.randint(1, 999))
    lk_inf = ""
    lk_cname = "大西瓜7"
    lk_ename = "DAXIGUA7"
    lk_gateno = dataInfo["bdno"]  #需要指定登机口
    lk_desk = "CTU"
    if "lk_outtime" in request.param:
        lk_outtime = request.param["lk_outtime"]
    if "lk_inf" in request.param:
        lk_inf = request.param["lk_inf"]
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
    time.sleep(1)
    return zhiji_dic


def creat_zhiji_byFlight_useInFunc(**request):
    """
    在值机前先往表里（sec_passenger_entity）加入数据
    产生随机的值机人信息（起飞时间不管，主要是航班号，序号，身份证号码），信息在lkxx1.xml里
    没有@pytest.fixture()，仅做函数调用使用
    """
    from .test_process import dataInfo   #{'flight_no': 'DR6562', 'bdno': '02', 'date': '2020-05-09'}
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