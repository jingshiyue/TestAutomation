import requests,time
'''
flight_scheduling_instruction
航班调度指令
#redis中写入航班状态：0-等待，1-已建库，2-开始登机，3-结束登机，4-航班离港，5-取消航班
'''
url_ip = 'http://192.168.5.15:8194'     #服务ip:端口

flightDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:10]  # 航班时间，格式为"2019-04-23"


def startboarding_rfid(rfid=""):
    '''rfid开始登机消息'''
    res = requests.post(url=url_ip + '/api/startboarding/rfid',
                        headers={'content-type':'application/json'},
                        json={'rfid':rfid})
    print(res.text)
    return res.text

def airtakeoff_three(flightnumber="",flightdate=flightDate,rfid=""):
    '''飞机起飞三字码（有filghtdate,格式yy-mm-dd）'''
    res = requests.post(url=url_ip + '/api/airtakeoff/three',
                        headers={'content-type':'application/json'},
                        json={"flightnumber":flightnumber,"flightdate":flightdate,"rfid":rfid})
    print(res.text)
    return res.text

def endboarding_rfid(rfid=""):
    '''rfid结束登机消息'''
    res = requests.post(url=url_ip + '/api/endboarding/rfid',
                        headers={'content-type':'application/json'},
                        json={'rfid':rfid})
    print(res.text)
    return res.text

def flighttime_change(rfid="",flightnumber="",flightdate=flightDate,timechg=""):
    '''
    航班时间变更
    :param timechg格式"1210-1320"
    '''
    res = requests.post(url=url_ip + '/api/flighttime/change',
                        headers={'content-type':'application/json'},
                        json={"rfid":rfid,"flightdate":flightdate,"flightnumber":flightnumber,"timechg":timechg})
    print(res.text)
    return res.text

def boardinggate_change(rfid="",flightnumber="",flightdate=flightDate,gatechg=""):
    '''
    发送登机口改变消息
    :param rfid:   str  和航班计划中的具体航班对应,先去航班计划中去获取对应航班的rfid信息
    :param gatechg: str  格式"12-10"
    '''
    res = requests.post(url=url_ip + '/api/boardinggate/change',
                        headers={'content-type':'application/json'},
                        json={"gatechg":gatechg,"flightnumber":flightnumber,"flightdate":flightdate,"rfid":rfid})
    print(res.text)
    return res.text

def flight_add(rfid=""):
    '''
    增加航班
    :param rfid:和航班计划中的具体航班对应(航班计划里面修改航班状态为空字符串)
    '''
    res = requests.post(url=url_ip + '/api/flight/add',
                        headers={'content-type':'application/json'},
                        json={"rfid":rfid})
    print(res.text)
    return res.text

def flight_delete(rfid=""):
    '''
    删除航班
    :param rfid:和航班计划中的具体航班对应(航班计划里面需要删除对应rfid的航班信息)
    '''
    res = requests.post(url=url_ip + '/api/flight/delete',
                        headers={'content-type':'application/json'},
                        json={"rfid":rfid})
    print(res.text)
    return res.text

def flight_cancel(rfid=""):
    '''
    取消航班
    :param rfid:和航班计划中的具体航班对应(航班计划里面需要删除对应rfid的航班信息)
    '''
    res = requests.post(url=url_ip + '/api/flight/cancel',
                        headers={'content-type':'application/json'},
                        json={"code":"06005","rfid":rfid})
    print(res.text)
    return res.text

def flight_getplan():
    '''获取航班计划内容'''
    res = requests.get(url=url_ip + '/api/flight/getplan')
    print(res.text)
    return res.text

def flight_getplanone(rfid=""):
    '''获取航班计划内容中单个航班'''
    res = requests.post(url=url_ip + '/api/flight/getplanone',
                        headers={'content-type':'application/json'},
                        json={"rfid":rfid})
    print(res.text)
    return res.text




def read_feature(filepath):
    '''读取txt文件内特征'''
    with open(filepath, 'r', encoding='utf-8') as f:  # 读取一个特征值
        feature = f.read()
    return feature


if __name__ == '__main__':
    startboarding_rfid(rfid="133683")
    # endboarding_rfid(rfid="133801")
    # airtakeoff_three(flightnumber="CQH8586", flightdate=flightDate, rfid="133675")
    # endboarding_rfid(rfid="134195")
    # flighttime_change(rfid="134162", flightnumber="HXA2891", flightdate=flightDate, timechg="1234-1711")
    # boardinggate_change(rfid="134162", flightnumber="HXA2891", flightdate=flightDate, gatechg="12-10")
    # flight_cancel(rfid="134162")
    # flight_add(rfid="134162")
    # endboarding_rfid(rfid="134158")



