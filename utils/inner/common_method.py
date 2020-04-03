# coding:utf-8
import hashlib
import base64
import json
import time,random
import uuid
from datetime import datetime
from _datetime import timedelta
import os
import linecache,logging
import re
from . import excel_operate

# from BaiTaAirport2_month.common.new_xingm import *
from https_20190709.common.new_xingm import *
"""
给定指定照片文件的路径，以及对应2K，和8K特征值的照片
"""
shiwanid = "C:/chenkeyun/OtherFile/IDcard"
shiwanid2k_features = "C:/chenkeyun/OtherFile/idcardf2k"
shiwanid8k_features = "C:/chenkeyun/OtherFile/idcardf8k"
shiwanli = "C:/chenkeyun/OtherFile/picture"
# shiwanli2k_features = "D:\pre_data\picture2k"   #1:N用
# shiwanli8k_features = "D:\pre_data\picture8k"   #1:1用


from https_20190709.common.Idcardnumber import get_random_id_number
#
# logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.DEBUG)
# handler = logging.FileHandler("log.log", encoding="utf-8")
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
#
# console = logging.StreamHandler()
# console.setFormatter(formatter)
# console.setLevel(logging.INFO)
#
# # logger.addHandler(handler)
# logger.addHandler(console)
import requests

# from BaiTaAirport2_month.common.logg import logger

id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]


def to_md5_str(str_code):
    """
    将字符串转换成md5加密字符串
    :param str_code: 待加密的对象    sign+timestamp+self.apiKey
    :return:
    """
    m = hashlib.md5()
    m.update(str_code.encode(encoding="utf-8"))
    str_encoding = m.hexdigest()
    return str_encoding


def to_base64(picturepath):
    """
    将图片转换成base64编码
    :param picturepath:图片文件路径
    :return:
    """
    with open(file=picturepath, mode="rb") as fp:
        imaga_data = fp.read()
        base64_data = base64.b64encode(imaga_data)
        return str(base64_data, encoding="utf-8")

def read_feature(filepath):
    '''读取txt文件内特征'''
    with open(filepath, 'r', encoding='utf-8') as f:  # 读取一个特征值
        feature = f.read()
    return feature

def get_time_stamp():
    """
    返回毫秒级的时间戳
    :return:
    """
    return str(round(time.time()*1000))


def delete_str(str1):
    """
    删除字符-
    :param str1:
    :return:
    """
    strr = str1.split("-")
    output = ''
    for b in range(len(strr)):
        output += strr[b]
    return output


def get_uuid():
    """
    获取32位uuid字符串
    :return:
    """
    m = str(uuid.uuid1())
    return delete_str(m)


def get_time_mmss():
    """
    返回YYYYMMDDhhmmss的时间格式
    :return:
    """
    return str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))


def get_time_month_ago():
    """
    获取当前时间和一个月以前的时间
    :return:
    """
    next_time = (datetime.now() - timedelta(days=20)).strftime("%Y%m%d%H%M%S")
    return str(next_time)


def produce_flight_date():
    """
    以当前时间，生成航班日期
    :return:
    """
    flight_date_old = get_time_mmss()
    flight_date = flight_date_old[0:8]
    return str(flight_date)


def produce_flight_day():
    """生成航班日"""
    return produce_flight_date()[6:8]


def produce_flight_number()->str:
    """
    随机生成YV97800示例的航班号
    :return:
    """
    zimu = string.ascii_uppercase
    shuzi = string.digits
    flight_no = zimu[random.randint(0, 25)]+zimu[random.randint(0, 25)]+shuzi[random.randint(0, 9)]+shuzi[random.randint(0, 9)]+shuzi[random.randint(0, 9)]\
    + shuzi[random.randint(0, 9)]+shuzi[random.randint(0, 9)]
    return flight_no


# def produce_flight_number_list(n=10):
#     """生成随机不同的航班号码到list"""
#     list1 = []
#     for i in range(0,n):
#         aa = produce_flight_number()
#         list1.append(aa)
#     if len(list1) != len(set(list1)):
#         kk = set(list1).add(produce_flight_number())
#         if len(kk) == n:
#             return list(list1)
#         else:
#             pass
#     else:
#         return list1


def produce_flight_list_only(n):
    """生成唯一的航班号码到list
    :param n: 要生成的航班号码的数量
    :return: list
    """
    list_1 = []
    while True:
        list_1.append(produce_flight_number())
        if set(list_1).__len__() == n:
            return list(set(list_1))


def produce_board_three(x, y):
    """返回以x开头，y结束的list用来存放boarding_number"""
    list1 = []
    while x <= y:
        if len(str(x)) == 1:
            mm = "00"+str(x)
            list1.append(mm)
        elif len(str(x)) == 2:
            kk = "0" + str(x)
            list1.append(kk)
        if len(str(x)) == 3:
            list1.append(str(x))
        x += 1
    return list1


def produce_board_two(x,y):
    list1 = []
    while x <= y:
        if len(str(x)) == 1:
            mm = "0"+str(x)
            list1.append(mm)
        if len(str(x)) == 2:
            kk = str(x)
            list1.append(kk)
        x += 1
    return list1


def get_flight_out_time(h=3):
    """
    在当前时间上加上对应的延迟时间作为起飞时间
    :param h: 需要延迟的时间
    :return:
    """
    next_time = (datetime.now() + timedelta(hours=h)).strftime("%Y%m%d%H%M%S")
    return str(next_time)


def get_flight_out_time_min(min=20):
    """
    在当前时间上加上对应的延迟时间作为起飞时间
    :param h: 需要延迟的时间
    :return:
    """
    next_time = (datetime.now() + timedelta(minutes=min)).strftime("%Y%m%d%H%M%S")
    return str(next_time)


def get_zhiji(h=1):
    """以当前之间之前的时间作为值机日期获取值机日期"""
    next_time = (datetime.now() - timedelta(hours=h)).strftime("%Y%m%d%H%M%S")
    return str(next_time)


def get_age(id_number):
    """通过身份证号获取年龄"""
    current = int(time.strftime("%Y"))
    year = int((id_number[6:10]))
    age = current-year
    return age


def get_bir_year(id_number):
    """
    获取旅客的出生年
    :param id_number:
    :return:
    """
    year = int(id_number[6:10])
    return year


def get_birthday(id_number):
    """
    通过身份证号码获取生日日期
    :param id_number:
    :return:
    """
    birthday_date = id_number[6:14]
    return str(birthday_date)


def get_lk_bdno():
    """
    生成三位随机的登机序列号
    :return:
    """
    lk_bdno = random.randint(100, 999)
    return str(lk_bdno)


def get_lk_desk():
    """
    生成随机的机场目的地
    :return:
    """
    current_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file_path = os.path.join(current_path, "aj系统xml文件")
    list_desk = linecache.getlines(file_path+"/"+"air.txt")
    return str(list_desk[random.randint(0, 154)]).rstrip("\n")


def get_add_idcard(card, p=0, l=18):
    """
    讲当前的数字生成规定位数的数字，:param card: 号码:param p: 替补的数字:param l: 一共需要的位数
    :param card: 号码
    :param p: 替补的数字
    :param l: 一共需要的位数
    :return:
    """
    m = str(0)
    if (len(str(card)) < l):
        for k in range(0,l-len(str(card))-1):
                m = m + str(p)
    else:
        raise Exception
    return m+str(card)


def get_txt(txtpath):
    with open(txtpath, "r") as fp:
        data = fp.read().rstrip()
    return str(data)


def get_features(filepath:str, mode="8K") ->str:
    global json_data
    body = {"FileName": filepath}
    header = {"Content-type": "application/json"}
    res = requests.post(url="http://127.0.0.1:7081/feature/v1/request",
                        headers=header,
                        json=body,
                        verify=False)
    res.close()
    try:
        json_data = json.loads(res.text)
        if mode.__eq__("8K"):
            feature = json_data["Feature8K"]
        else:
            feature = json_data["Feature2K"]
        logger.info(feature)
        return feature
    except:
        logger.warning("质量不好，提取失败")


def produce_idcard_to_only_list(n: int)->list:
    """
    生成随机不同的身份证到list
    :param n: 生成随机随机身份证的个数
    :return: list
    """
    idcard_list = []
    while True:
        idcard_list.append(get_random_id_number())
        if set(idcard_list).__len__() == n:
            return list(set(idcard_list))


def produce_flight_number_list(n=10):
    """生成随机不同的航班号码到list"""
    list1 = []
    for i in range(0,n):
        aa = produce_flight_number()
        list1.append(aa)
    if len(list1) != len(set(list1)):
        kk = set(list1).add(produce_flight_number())
        if len(kk) == n:
            return list(list1)
        else:
            pass
    else:
        return list1


def get_time_format(format: str)->str:
    """
    获取特定的日期格式
    :param format: format
    :return: string
    """
    formatter = time.strftime(format, time.localtime())
    return str(formatter)


def get_id_re_match():
    idcardlist = []
    list_log = linecache.getlines(r"C:\chenkeyun\projectself\pythonproject\BaiTaAirport2_month\log"+"/"+"Autosendlk.log")
    for i in list_log:
        patten = '号码为：.*?姓名'
        string1 = re.findall(pattern=patten, string=i)[0].replace("号码为：", "").replace("姓名", "")
        idcardlist.append(string1)
    return idcardlist


def get_filght_re_match():
    idcardlist = []
    list_log = linecache.getlines(r"C:\chenkeyun\projectself\pythonproject\BaiTaAirport2_month\log"+"/"+"Autosendlk.log")
    for i in list_log:
        patten = '航班号码为：.*'
        string1 = re.findall(pattern=patten, string=i)[0].replace("航班号码为：", "")
        idcardlist.append(string1)
    return idcardlist


def get_headers(sign):
    """
    sing:"/api/v1/face/backlist/save""
    """
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign = to_md5_str(sign + timestamp + apiKey)
    header = {"apiId": apiId, "sign": sign, "timestamp": timestamp}
    return header

def read_case_title(exl,col_idx=0,read_row=0):
    """
    :param exl: excel 对象，如exl = excel_operate.excel_obj(sheet_name,exl_f_path)
    :param col_idx: 标题所在的列
    :param read_row: 读取第几行
    :return:返回读取excel的大、小标题、关键参数
    """
    T1 = exl.get_col_data(0)  # 一级标题  列表形式
    t1 = ""  #一级标题
    tmp_idx = 0
    for i in T1:
        if i != "":
            t1 = i
        tmp_idx += 1
        t2 = ""
        if tmp_idx == read_row:
            t2 = exl.get_cell_value(read_row,col_idx)   #子标题
        if "=" in t2:
            print("==================")
            print(t1)
            print(t2)
            keyparam = t2.split(" ")[1].split("=")[0]
            print(keyparam)
            print("==================")
            break
    return t1,t2,keyparam



if __name__ == '__main__':
    print(random.randint(0,8))
    # print(get_id_re_match())
    # print(get_filght_re_match())
    # print(get_time_format("%Y-%m-%d %H:%M:%S"))
    # pass

    # idpath = r"C:\chenkeyun\Tools\test1000\idphoto"
    # lipath = r"C:\chenkeyun\Tools\test1000\livephoto"
    # for i in range(0, 1000):
    #     data = to_base64(idpath+"/"+str(i)+".jpg")
    #     with open("C:/chenkeyun/Tools/test1000/idbase64"+"/"+str(i)+".txt", "w") as fp:
    #         fp.write(data)
    # print("id提取完毕")
    # for i in range(0, 1000):
    #     data = to_base64(lipath+"/"+str(i)+".jpg")
    #     with open("C:/chenkeyun/Tools/test1000/libase64"+"/"+str(i)+".txt", "w") as fp:
    #         fp.write(data)

    picture_path = r"C:\Users\Original Dream\Desktop\buk"
    # for i in range(1, 10):
    #     data = get_features(picture_path+"/"+"p"+str(i)+".jpg")
    #     with open(picture_path+"/"+"p"+str(i)+".txt", "w") as fp:
    #         fp.write(data)
    #     print("第%d次完毕"%i)
# 
#     data = get_features(r"C:\Users\Original Dream\Desktop\p0.jpg", mode="2k")
#     with open("./p0.txt","w") as fp:
#         fp.write(data)




