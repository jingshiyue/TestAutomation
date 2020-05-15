# coding:utf-8
# from ..common.common_method import *
from https_20190709.common.common_method import *
import requests


class BlackListApi(object):
    """
    对黑名单管理的CRUD类
    20190702新增白名单
    """
    def __init__(self, host="http://175.168.1.199:9091/"):
        # self.certificate = "D:/WorkSpace/https_20190709/API_https/cacert.crt"
        # self.certificate = "D:\workfile\zhongkeyuan_workspace\https_20190709\API_https\cacert.crt"  #用于Https
        self.certificate = None   #用于http
        self.apiId = "123456"
        self.apiKey = "1285384ddfb057814bad78127bc789be"
        self.host = host
        self.anjian_server = "security-server"
        self.review_server = "review-server"
        self.boardinggate_server = "boardinggate-server"
        self.data_platform_server = "data-platform-server"
        self.black_list_save = self.host+self.data_platform_server+"/api/v1/face/backlist/save"
        self.black_list_delete = self.host+self.data_platform_server+"/api/v1/face/backlist/delete"
        self.black_list_query = self.host+self.data_platform_server+"/api/v1/face/backlist/query"
        self.black_list_record_query = self.host+self.data_platform_server+"/api/v1/face/backlist/record/query"
        self.backlist_record_latest = self.host+self.data_platform_server+"/api/v1/face/backlist/record/latest"  # 黑名单最新记录查询接口
        self.white_list_save = self.host+self.data_platform_server+"/api/v1/face/whitelist/save"  #白名单新增
        self.white_list_delete = self.host + self.data_platform_server + "/api/v1/face/whitelist/delete"   #白名单删除
        self.white_list_query = self.host + self.data_platform_server + "/api/v1/face/whitelist/query"   #白名单查询
        self.white_list_record_query = self.host + self.data_platform_server + "/api/v1/face/whitelist/record/query"   #安检员工记录查询
        self.jms_server = "jms-server"

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def get_headers(self, sign):
        """获取各个接口的请求头"""
        timestamp = get_time_stamp()
        sign = to_md5_str(sign+timestamp+self.apiKey)
        header = {"apiId": self.apiId, "sign": sign, "timestamp": timestamp}
        return header

    def api_black_list_save(self,
                            this_sign="/api/v1/face/backlist/save",
                            reqId=get_uuid(),   #必须
                            id="",
                            certificateNumber="",
                            peopleName="",      #必须
                            focusType=0,       #必须int 0：布控人员  1：失信人员  2：重点检查人员  3：本场关注人员  4：嫌疑人  5：上访人员  6：其他人员
                            img="",
                            focusTime="",    #布控时间yyyyMMddHHmmss（新增必给）
                            cancelTime="",   #撤控时间yyyyMMddHHmmss
                            sex=0,           #性别int
                            focusReason="布控原因",
                            note="备注",#必须
                            isAllowPass=0 #integer	非必须 新增请求字段isAllowPass，标记布控人员是否允许通过大闸机，默认是0 不允许通过
    ):
        """黑名单增加接口"""
        body = {"reqId": reqId,
                "id": id,  # 32位UUID，流水表记录ID，有就更新，无则增加
                "certificateNumber":certificateNumber,
                "peopleName": peopleName,
                "focusType": focusType,
                "img": img,
                "focusTime":focusTime,
                "cancelTime":cancelTime,
                "sex":sex,
                "focusReason":focusReason,
                "note":note,}

        res = requests.post(url=self.black_list_save, headers=self.get_headers(this_sign),
                            json=body,
                            verify=self.certificate)
        print(res.text)
        res.close()
        return res.text

    def api_black_list_delete(self,
                              this_sign="/api/v1/face/backlist/delete",
                              reqId=get_uuid(),
                              ids=""):
        """黑名单删除接口"""
        body = {"reqId": reqId,
                "ids": ids}
        print("url",self.black_list_delete)
        print(self.get_headers(this_sign))
        res = requests.post(url=self.black_list_delete, headers=self.get_headers(this_sign),
                            json=body,
                            verify=self.certificate)
        res.close()
        print(res.text)
        return res.text

    def api_black_list_query(self,
                             reqId=get_uuid(),
                             page=1,       #必须
                             pageSize=1,   #必须
                             passengerName="",
                             sex=0,        #int类型
                             cardId="",
                             kindType=0,  #int 0：布控人员  1：失信人员  2：重点检查人员  3：本场关注人员  4：嫌疑人  5：上访人员  6：其他人员
                             isCount=None):   #为1的时候查询总记录数
        """黑名单查询接口"""
        this_sign = "/api/v1/face/backlist/query"
        body = {"reqId": reqId,
                "page": page,
                "pageSize": pageSize,
                "passengerName":passengerName,
                "sex":sex,
                "cardId":cardId,
                "kindType":kindType,
                "isCount": isCount}
        res = requests.post(url=self.black_list_query, headers=self.get_headers(this_sign),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res.text

    def api_black_list_record_query(self,
                                    reqId=get_uuid(),
                                    areaCode="",    #区域编号
                                    date="",        #开始时间，格式yyyymmdd
                                    passengerName="",
                                    sex=0,           # 性别int
                                    cardId="",
                                    kindType="",        #必须int 0：布控人员  1：失信人员  2：重点检查人员  3：本场关注人员  4：嫌疑人  5：上访人员  6：其他人员
                                    addressType="",     # 出现地点类型 0：自助闸机 1：复核闸机
                                    page=1,
                                    pageSize=1,
                                    isCount=None):
        """黑名单报警记录查询接口"""
        this_sign = "/api/v1/face/backlist/record/query"
        body = {"reqId": reqId,
                "areaCode": areaCode,
                "date": date,    # 开始时间，格式yyyymmdd。如2018070109
                "passengerName": passengerName,   # 姓名
                "sex": sex,
                "cardId": cardId,   # 证件号
                "kindType": kindType,  # 布控类型 0：布控人员 1：失信人员 2：重点检测人员
                "addressType": addressType,  # 出现地点类型 0：自助闸机 1：复核闸机
                "page": page,
                "pageSize": pageSize,
                "isCount": isCount}
        res = requests.post(url=self.black_list_record_query, headers=self.get_headers(this_sign),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res.text

    def api_face_backlist_record_latest(self,
                                        reqId=get_uuid(),
                                        areaCode="",
                                        deviceCode=""):
        """2.4.16.5黑名单最新记录获取接口"""
        body = {"reqId": reqId,
                "areaCode": areaCode,   # 否
                "deviceCode": deviceCode}  # 否
        res = requests.post(url=self.black_list_record_query,
                            headers=self.get_headers("/api/v1/face/backlist/record/latest"),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res.text

    def api_white_list_save(self,
                            this_sign="/api/v1/face/whitelist/save",
                            reqId=get_uuid(),   #必须
                            ids="",
                            employeeName="",   #姓名
                            employeeId="",      #员工编号  必须
                            certificateNumber="",       #身份证号码  必须
                            faceImage="",    #人脸图片 base64加密   必须
                            sex=1,           #性别int
                            birthday="",    #出生年月yyyyMMdd
                            position="",    #职务
                            national="",    #民族
                            address="",     #家庭住址
                            contact=""      #联系电话
                            ):
        """白名单增加接口"""
        body = {"reqId": reqId,
                "id": ids,  # 32位UUID，流水表记录ID，有就更新，无则增加
                "employeeName": employeeName,
                "employeeId": employeeId,
                "certificateNumber": certificateNumber,
                "faceImage": faceImage,
                "sex":sex,
                "birthday":birthday,
                "position":position,
                "national":national,
                "address":address,
                "contact":contact
                }
        res = requests.post(url=self.white_list_save, headers=self.get_headers(this_sign),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res.text

    def api_white_list_delete(self,
                              this_sign="/api/v1/face/whitelist/delete",
                              reqId=get_uuid(),
                              ids=""):
        """白名单删除接口"""
        body = {"reqId": reqId,
                "ids": ids}
        res = requests.post(url=self.white_list_delete, headers=self.get_headers(this_sign),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res.text

    def api_white_list_query(self,
                             reqId=get_uuid(),
                             page=1,       #必须
                             pageSize=1,   #必须
                             employeeName="",
                             employeeId="",        #员工编号
                             certificateNumber="",         #证件号
                             sex=0,         #int 性别
                             isCount=1):   #int 为1的时候查询总记录数
        """白名单查询接口"""
        this_sign = "/api/v1/face/whitelist/query"
        body = {"reqId": reqId,
                "page": page,
                "pageSize": pageSize,
                "employeeName":employeeName,
                "employeeId":employeeId,
                "certificateNumber":certificateNumber,
                "sex":sex,
                "isCount": isCount}
        res = requests.post(url=self.white_list_query, headers=self.get_headers(this_sign),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res.text

    def api_white_list_record_query(self,
                                    reqId=get_uuid(),
                                    channelCode="",    #通道编号
                                    employeeName="",        #姓名
                                    employeeId="",      #员工编号
                                    certificateNumber="",          #证件号
                                    sex=0,           # 性别int
                                    page=1,
                                    pageSize=1,
                                    isCount=1):
        """安检员工记录查询接口"""
        this_sign = "/api/v1/face/whitelist/record/query"
        body = {"reqId": reqId,
                "channelCode": channelCode,
                "employeeName": employeeName,    # 开始时间，格式yyyymmdd。如2018070109
                "employeeId": employeeId,   # 姓名
                "certificateNumber": certificateNumber,
                "sex": sex,
                "page": page,
                "pageSize": pageSize,
                "isCount": isCount}
        res = requests.post(url=self.white_list_record_query, headers=self.get_headers(this_sign),
                            json=body,
                            verify=self.certificate)
        res.close()
        return res.text






if __name__ == '__main__':
    pass
    # blacklist = BlackListApi()
    # blacklist.api_black_list_save(peopleName="某某",focusTime="20180808080800",note="重点嫌疑人")
    # faceImage = to_base64(r"D:/pre_data/2.jpg")
    # # faceImage = to_base64(r"D:/pre_data/1.png")
    # print(blacklist.api_white_list_save(reqId=get_uuid(),   #必须
    #                                     ids="",
    #                                     employeeName="张三",   #姓名
    #                                     employeeId="124",      #员工编号  必须
    #                                     certificateNumber="123",       #身份证号码  必须
    #                                     faceImage=faceImage,    #人脸图片 base64加密   必须
    #                                     sex=1,           #性别int
    #                                     birthday="19990101",    #出生年月yyyyMMdd
    #                                     position="地勤",    #职务
    #                                     national="维吾尔族",    #民族
    #                                     address="重庆渝北光电园",     #家庭住址
    #                                     contact="13312345678"      #联系电话
    #                                     ))
    # print(blacklist.api_white_list_delete(ids="0cfc1ae603b44053b2e0c2d11abc1e18"))
    # blacklist.api_black_list_delete()