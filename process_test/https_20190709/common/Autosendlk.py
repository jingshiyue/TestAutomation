# coding:utf-8
import os
import random
from xml.etree import ElementTree as ET
#from BaiTaAirport2_month.common.common_method import *
from https_20190709.common.common_method import *
#from BaiTaAirport2_month.msgQueue.msg import send_msg
from https_20190709.common.msg import send_msg

name = os.path.realpath(__file__).split("\\")[-1].split(".")[0]

def send_lkxx(lk_IsInternation="0",
              lk_bdno="01",
              lk_card="0",
              lk_cardid="500238199312134390",
              lk_chkt="20180929103700",
              lk_cname="陈克云",
              lk_date="20180929",
              lk_del="0",
              lk_desk="CTU",
              lk_ename="HHHH",
              lk_flight="3U8317",
              lk_gateno="10",
              lk_id="0000001",
              lk_inf=" ",
              lk_insur="0",
              lk_outtime="20140626102446",
              lk_sex="1",
              lk_vip="0",
              lk_seat=""):
    #值机信息: 身份证、登机序号、不一致
    # 航班号、中文名、可以一致
    # 座位号可以为空
    """
    发送旅客信息表到消息队列
    :param lk_IsInternation:  1     是否国际 0否，1是，2未知
    :param lk_bdno:           2     <!--2 10 登机序号 -->  3位
    :param lk_cardid:         4     证件号码
    :param lk_chkt:           6     值机日期
    :param lk_cname:          8     旅客中文姓名80
    :param lk_date:           9     9航班日期 8 YYYYMMDD
    :param lk_del:            10    10是否删除 0否  1是
    :param lk_desk:           11    11目的地  机场三字代表码
    :param lk_ename:          12    旅客英文姓名
    :param lk_flight:         13    航班号 12
    :param lk_gateno          14    登机口号码 无意义
    :param lk_id:             15    旅客ID 主键 str 36
    :param lk_inf:            16    16婴儿标志3 INF带婴儿 “”表示未带婴儿
    :param lk_insur:          18    是否购保1
    :param lk_outtime:        20    旅客起飞时间
    :param lk_sex:            23    性别  1男性 2女性 0 未知
    :param lk_vip:            26    是否是贵宾1 否0，是1，未知2
    :return:
    """
    # list_data = []
    # person_info = {"lk_IsInternation": lk_IsInternation, "lk_bdno": lk_bdno, "lk_cardid": lk_cardid,
    #                "lk_chkt": lk_chkt, "lk_cname": lk_cname, "lk_date": lk_date, "lk_desk": lk_desk,
    #                "lk_ename": lk_ename, "lk_flight": lk_flight, "lk_id": lk_id, "lk_inf": lk_inf,
    #                "lk_insur": lk_insur, "lk_outtime": lk_outtime, "lk_sex": lk_sex, "lk_vip": lk_vip
    #                }
    # with open("./info.json", "r") as fp1:
    #     list_11 = list(fp1.read())
    #     print(type(list_11))
    #     list_data.extend(list_11)
    #     list_data.append(person_info)
    # with open("./info.json", "w", encoding="utf-8") as fp2:
    #     json.dump(fp2, list_data)

    base_file_path = os.path.realpath(__file__)
    base_dir_path = os.path.dirname(base_file_path)
    project_path = os.path.dirname(base_dir_path)
    xml_path = os.path.join(project_path, "aj系统xml文件")
    ET.register_namespace(prefix="", uri="http://schemas.datacontract.org/2004/07/Xasd.FASC.SECM.Entity")
    tree = ET.parse((xml_path+"/"+"lkxx.xml"))
    root = tree.getroot()
    root[3][0][1].text = lk_IsInternation
    root[3][0][2].text = lk_bdno
    root[3][0][3].text = lk_card
    root[3][0][4].text = lk_cardid
    root[3][0][6].text = lk_chkt
    root[3][0][8].text = lk_cname
    root[3][0][9].text = lk_date
    root[3][0][10].text = lk_del
    root[3][0][11].text = lk_desk
    root[3][0][12].text = lk_ename
    root[3][0][13].text = lk_flight
    root[3][0][14].text = lk_gateno
    root[3][0][15].text = lk_id
    root[3][0][16].text = lk_inf
    root[3][0][18].text = lk_insur
    root[3][0][20].text = lk_outtime
    root[3][0][22].text = lk_seat
    root[3][0][23].text = lk_sex
    root[3][0][26].text = lk_vip

    tree.write(file_or_filename=base_dir_path+"./lkxx1.xml",
               encoding="utf-8",
               xml_declaration=True)

    with open(base_dir_path+"./lkxx1.xml", "rb") as fp:
        data = fp.read().decode("utf-8")
        send_msg(data)


def send_ajxx(ajxxb_id="1138301",
              lk_id="0000001",
              safe_flag="0",
              safe_no="20",
              safe_oper="PA0100",
              safe_time="20180930091420"):
    """
    发送安检信息到消息队列
    :param ajxxb_id:     1 安检信息id 主键35
    :param lk_id:        3 旅客id 35旅客在安检系统主键
    :param safe_flag:    4 安检状态 0未安检，1：已安检
    :param safe_no:      5 安检通道号20
    :param safe_oper:    6 安检验证员60
    :param safe_time:    10 安检时间14 YYYYMMDDhhmmss
    :return:
    """
    base_file_path = os.path.realpath(__file__)
    base_dir_path = os.path.dirname(base_file_path)
    project_path = os.path.dirname(base_dir_path)
    xml_path = os.path.join(project_path, "aj系统xml文件")
    ET.register_namespace(prefix="", uri="http://schemas.datacontract.org/2004/07/Xasd.FASC.SECM.Entity")
    tree = ET.parse((xml_path+"/"+"ajxx.xml"))
    root = tree.getroot()
    root[3][0][1].text = ajxxb_id
    root[3][0][3].text = lk_id
    root[3][0][4].text = safe_flag
    root[3][0][5].text = safe_no
    root[3][0][6].text = safe_oper
    root[3][0][10].text = safe_time
    tree.write(file_or_filename="ajxx1.xml",
               encoding="utf-8",
               xml_declaration=True)
    with open("ajxx1.xml", "rb") as fp:
        data = fp.read().decode("utf-8")
        print(data)
        send_msg(data)


if __name__ == '__main__':
    # lk_sex = str(random.randint(1, 2))
    send_lkxx(lk_cardid="400228199612134390",
              lk_chkt=get_time_mmss(),
              lk_cname="博尔济吉特·布木布泰",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight="neimeng1",
              lk_id="1234567891",
              lk_bdno="001",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")


    # a = 1
    # while a < 10 :
    #     print("开始第%d"%a+"次值机")
    #     send_lkxx(lk_cardid=get_random_id_number(),
    #               lk_chkt=get_zhiji(2),
    #               lk_cname=get_name(),
    #               lk_date=produce_flight_date(),
    #               lk_desk=get_lk_desk(),
    #               lk_flight=produce_flight_number(),
    #               lk_id=get_uuid(),
    #               lk_bdno=get_lk_bdno(),
    #               lk_insur="1",
    #               lk_outtime=get_flight_out_time(2),
    #               lk_sex="1")
    #     a += 1
    # print("值机%d" % a+"次结束")

    # for i in range(0, 20):
    #     idcard = get_random_id_number()
    #     flight_no = produce_flight_number()
    #     send_lkxx(lk_cardid=idcard,
    #               lk_chkt=get_time_mmss(),
    #               lk_cname="bukongname"+str(i+300),
    #               lk_date=produce_flight_date(),
    #               lk_desk="TEN",
    #               lk_flight=flight_no,
    #               lk_id="1234567891",
    #               lk_bdno="001",
    #               lk_insur="1",
    #               lk_outtime=get_flight_out_time(2),
    #               lk_sex="1")
    #     log.logger.info("第"+str(i)+"次证件号码为："+idcard+"姓名为："+"bukongname"+str(i+300)+"航班号码为："+flight_no)

    # idcard = get_random_id_number()
    # flight_no = produce_flight_number()
    # lk_bdno = str(random.randint(1,999))
    # send_lkxx(lk_IsInternation="0",                 #1     是否国际 0否，1是，2未知
    #           lk_bdno=lk_bdno,                      #2     <!--2 10 登机序号 -->  3位
    #           lk_cardid=idcard,                     #4     证件号码
    #           lk_chkt=get_time_mmss(),              #6     值机日期
    #           lk_cname="陈克云",                    #8     旅客中文姓名80
    #           lk_date=produce_flight_date(),        #9     9航班日期 8 YYYYMMDD
    #           lk_del="0",                           #10    是否删除 0否  1是
    #           lk_desk="CTU",                        #11    11目的地  机场三字代表码
    #           lk_ename="HHHH",                      #12    旅客英文姓名
    #           lk_flight="JD5283",                  #13    航班号 12
    #           lk_gateno="10",                       #14    登机口号码 无意义k_g
    #           lk_id=str(random.randint(1,999)),     #15    旅客ID 主键 str 36
    #           lk_inf=" ",                           #16    16婴儿标志3 INF带婴儿 “”表示未带婴儿
    #           lk_insur="0",                         #18    是否购保1
    #           lk_outtime="20190506201500",    #20    旅客起飞时间
    #           lk_sex="1",                           #23    性别  1男性 2女性 0 未知
    #           lk_vip="0")                           #26    是否是贵宾1 否0，是1，未知2
    # log.logger.info("证件号码为："+idcard+"登机序列号为："+lk_bdno)




    # send_lkxx(lk_IsInternation="0",  # 1     是否国际 0否，1是，2未知
    #           lk_bdno="556",  # 2     <!--2 10 登机序号 -->  3位
    #           lk_cardid="500382199907027070",  # 4     证件号码
    #           lk_chkt=get_time_mmss(),  # 6     值机日期
    #           lk_cname="西瓜088",  # 8     旅客中文姓名80
    #           lk_date=produce_flight_date(),  # 9     9航班日期 8 YYYYMMDD
    #           lk_del="0",  # 10    是否删除 0否  1是
    #           lk_desk="CTY",  # 11    11目的地  机场三字代表码
    #           lk_ename="xigua",  # 12    旅客英文姓名
    #           lk_flight="JD5892",  # 13    航班号 12
    #           lk_gateno="T1AJ1",  # 14    登机口号码 无意义
    #           lk_id=str(random.randint(1, 999)),  # 15    旅客ID 主键 str 36
    #           lk_inf=" ",  # 16    16婴儿标志3 INF带婴儿 “”表示未带婴儿
    #           lk_insur="0",  # 18    是否购保1
    #           lk_outtime="20191106195500",  # 20    旅客起飞时间
    #           lk_sex="1",  # 23    性别  1男性 2女性 0 未知
    #           lk_vip="0")
    # print("值机成功！")
    # import string
    #
    # slcLetter = random.choice(string.ascii_uppercase)
    # i = random.randint(1, 99)
    # print(str(i)+slcLetter)

