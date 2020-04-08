# coding:utf-8
import hashlib
import base64
import json
import time,random
import uuid
from datetime import datetime
from _datetime import timedelta
import os
import linecache
import re
import string
from xpinyin import Pinyin
# """
# 给定指定照片文件的路径，以及对应2K，和8K特征值的照片
# """
# shiwanid = "C:/chenkeyun/OtherFile/IDcard"
# shiwanid2k_features = "C:/chenkeyun/OtherFile/idcardf2k"
# shiwanid8k_features = "C:/chenkeyun/OtherFile/idcardf8k"
# shiwanli = "C:/chenkeyun/OtherFile/picture"
# shiwanli2k_features = "D:\pre_data\picture2k"   #1:N用
# shiwanli8k_features = "D:\pre_data\picture8k"   #1:1用

import requests

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

# def read_case_title(exl,col_idx=0,read_row=0):
#     """
#     :param exl: excel 对象，如exl = excel_operate.excel_obj(sheet_name,exl_f_path)
#     :param col_idx: 标题所在的列
#     :param read_row: 读取第几行
#     :return:返回读取excel的大、小标题、关键参数
#     """
#     T1 = exl.get_col_data(0)  # 一级标题  列表形式
#     t1 = ""  #一级标题
#     tmp_idx = 0
#     for i in T1:
#         if i != "":
#             t1 = i
#         tmp_idx += 1
#         t2 = ""
#         if tmp_idx == read_row:
#             t2 = exl.get_cell_value(read_row,col_idx)   #子标题
#         if "=" in t2:
#             print("==================")
#             print(t1)
#             print(t2)
#             keyparam = t2.split(" ")[1].split("=")[0]
#             print(keyparam)
#             print("==================")
#             break
#     return t1,t2,keyparam

validate=['1','0','X','9','8','7','6','5','4','3','2']
def get_validate_checkout(id17):
    """
    获得校验码算法
    :param id17:
    :return:
    """
    weight = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]  # 十七位数字本体码权重
    validate = ['1','0','X','9','8','7','6','5','4','3','2']  # mod11,对应校验码字符值

    sum = 0
    mode = 0
    for i in range(0,len(id17)):
        sum = sum + int(id17[i])*weight[i]
    mode = sum % 11
    return validate[mode]


def get_random_id_number(sex=1, start="1960-01-01", end="2000-12-30"):
    """
    产生随机可用身份证号，sex = 1表示男性，sex = 0表示女性
    :param sex: sex = 1表示男性，sex = 0表示女性
    :param start: "1960-01-01"
    :param end:   "2000-12-30"
    :return:
    """
    # 地址码产生
    addrInfo = random.randint(0, len(addr.addr)-1)  # 随机选择一个值
    addrId = addr.addr[addrInfo][0]
    # addrName = addr[addrInfo][1]
    idNumber = str(addrId)
    # 出生日期码
    # 生日起止日期
    days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
    birthDays = datetime.datetime.strftime(datetime.datetime.strptime(start,"%Y-%m-%d") + datetime.timedelta(random.randint(0,days)),"%Y%m%d")
    idNumber = idNumber + str(birthDays)
    # 顺序码
    for i in range(2):  # 产生前面的随机值
        n = random.randint(0, 9)  # 最后一个值可以包括
        idNumber = idNumber + str(n)
    # 性别数字码
    sexId = random.randrange(sex, 10, step=2)  # 性别码
    idNumber = idNumber + str(sexId)
    return str(idNumber) + validate[random.randint(0, 10)]  # addrName,addrId,birthDays,sex


def get_info_from_id(id18):
    """
    从身份证号码中得出个人信息：地址、生日、性别
    :param id18:
    :return:
    """
    addrId = id18[0:6]
    for it in addr.addr:
        if addrId == str(it[0]):  # 校验码
            addrName = it[1]
            break
    else:  # 未被break终止
        addrName = 'unknown'
    birthDays = datetime.datetime.strftime(datetime.datetime.strptime(id18[6:14], "%Y%m%d"), "%Y-%m-%d")
    sex = 'man' if int(id18[-2]) % 2 else 'woman'   # 0为女性，1为男性
    return addrName, birthDays, sex

p = Pinyin()
last_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
                  '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
                  '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
                  '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
                  '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
                  '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
                  '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']

first_names = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
                   '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
                   '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于', '心', '学', '么', '之', '都', '好',
                   '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第', '样', '道', '想', '作', '种', '开', '美',
                   '总', '从', '无', '情', '己', '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又', '行', '意', '动',
                   '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯', '知',
                   '世', '什', '两', '次', '使', '身', '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正', '感',
                   '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果', '走',
                   '将', '月', '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真', '打',
                   '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主', '界', '门',
                   '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性', '马',
                   '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让', '母',
                   '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英', '军',
                   '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快', '原',
                   '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条', '呢',
                   '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片', '罗',
                   '钱', '紶', '吗', '语', '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合', '反',
                   '题', '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运', '及',
                   '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司', '巴',
                   '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落', '尽', '形', '影',
                   '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半', '热', '送', '兴', '造', '谈', '容',
                   '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计', '您',
                   '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻', '统',
                   '断', '福', '城', '故', '历', '惊', '脸', '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示', '愿',
                   '持', '千', '史', '谁', '准', '联', '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社', '算',
                   '义', '竟', '确', '酒', '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息', '功',
                   '官', '待', '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图', '具',
                   '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破', '引', '食',
                   '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微', '娘', '须', '试', '怀',
                   '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '座', '参', '八', '除', '跑',
                   '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香', '停', '际', '致', '阳', '纸', '李', '纳', '验',
                   '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿', '睡',
                   '展', '跳', '获', '艺', '六', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店', '否',
                   '害', '草', '排', '背', '止', '组', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河', '续',
                   '哥', '呼', '若', '推', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪', '索',
                   '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族', '低',
                   '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅', '街',
                   '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀', '律',
                   '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职', '属',
                   '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉', '遗',
                   '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳', '差',
                   '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府', '压',
                   '超', '负', '勒', '杂', '醒', '洗', '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童', '顶',
                   '派', '素', '脱', '农', '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯', '巨',
                   '琴', '免', '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层', '付',
                   '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探', '呀', '营',
                   '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优', '课', '鸟', '喊', '降',
                   '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财', '孤', '枪', '禁', '恐', '伙', '杰',
                   '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨', '菜', '划', '授', '归', '浪', '听', '凡', '预',
                   '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛', '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧', '误',
                   '乾', '坤']

def random_name(size=1, chars=string.ascii_letters + string.digits):
    print(chars)
    print(''.join(random.choice(chars) for _ in range(size)))
    return ''.join(random.choice(chars) for _ in range(size))

def first_name(size=2, ln=None, fn=None):
    _lst = []
    for i in range(size):
        _item = random_name(1, fn)
        if ln:
            while _item in ln:
                _item = random_name(1, fn)
            _lst.append(_item)
        else:
            _lst.append(_item)
    return "".join(_lst)


def last_name(size=1, names=None):
    return random_name(size, names)


def get_name(lns=last_names, fns=first_names):
    _last = last_name(1, lns)
    return "{}{}".format(_last, first_name(random.randint(1, 2), _last, fns))


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




