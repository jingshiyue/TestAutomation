# coding:utf-8
import random
import time


def idcard_generator():
    """ 随机生成新的18为身份证号码 
    """
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99), random.randint(1, 99), random.randint(1, 99), random.randint(t - 80, t - 18), random.randint(1, 12), random.randint(1, 28), random.randint(1, 999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]
        IDCard = '%s%s' % (x, LAST[y % 11])
    return IDCard


def check_true(x1):
    """
    验证身份证号码是否是真实号码
    :param x1:
    :return:
    """
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    xlen = len(x1)
    if xlen != 18 and xlen != 15:
        return "身份证号码长度错误"
    try:
        if xlen == 18:
            x2 = x1[6:14]
            x3 = time.strptime(x2, '%Y%m%d')
            if x2 < '19000101' or x3 > time.localtime():
                return '时间错误，超过允许的时间范围'
        else:
            x2 = time.strptime(x1[6:12], '%y%m%d')
    except Exception as e:
        return '时间错误，非合法时间' + str(e)
    if xlen == 18:
        y = 0
        for i in range(17):
            y += int(x1[i]) * ARR[i]
        if LAST[y % 11] != x1[-1].upper():
            return '验证码错误'
    return 'YES'


if __name__ == '__main__':
    a =idcard_generator()
    print(a)
    print(check_true(a))

    m = "20180829"
    print(m[6:8])