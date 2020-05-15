# from BaiTaAirport2_month.common.mysql_class import DataBase
from https_20190709.common.common_method import *
from https_20190709.API_https.AirportProcess import AirportProcess
from BaiTaAirport2_month.msgQueue.Autosendlk import *
import os,threading,xlwt


# print(to_base64("D:/pre_data/picture(现场照片)/146.jpg"))
# print(to_base64("D:/pre_data/picture_640_480/0.jpg"))
# print(to_base64(r"C:\Users\admin\Desktop\1现场照片.jpg"))

#清空特征，并添加1000个特征底库
# database = DataBase("192.168.5.15", 3306, "root", "123456", "htbusyinfo")
# sql = "TRUNCATE face_review_features;"
# database.cud(sql)
# cardPhoto = to_base64("D:/pre_data/picture(现场照片)/0.jpg")  # 身份证照片
largePhoto = to_base64(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture_640_480/1.jpg")  # 现场大图
#增加100个航班号序号重复的特征，座位号不一样
# while True:
#     for i in range(100):
#         date = produce_flight_date()      #当天日期YYYYMMDD
#         feature_8k = read_feature("D:/pre_data/picture8k/%s.txt"%i)     #读取8k特征
#         feature_8k_B = read_feature("D:/pre_data/picture8k/%s.txt" %(i+100) )  # 读取8k特征
#         lk_cname = "周志喜%s"%i        #中文姓名
#         # print("航班号:" + flight_no + ",登机序号:" + bdno)
#         #旅客去人工通道刷票
#         res = AirportProcess().api_face_security_manual_check(flightNo="AB0001",
#                                                                faceImage=cardPhoto,
#                                                                gateNo="T1AJ1",
#                                                                deviceCode="T1AJ001",
#                                                                boardingNumber=str(i),
#                                                                seatId=str(i),
#                                                                startPort="HET",
#                                                                flightDay=date[-2:],
#                                                                faceFeature=feature_8k,
#                                                                kindType=1,  # 类型：0：刷票 1：刷票放行
#                                                                largePhoto=largePhoto
#                                                                )
#         print("人工通道刷票响应" + res.text)
#         print("第%s个旅客特征添加完成..."%(i+1))
#         # 旅客去人工通道刷票
#         res = AirportProcess().api_face_security_manual_check(flightNo="AB0001",
#                                                               faceImage=cardPhoto,
#                                                               gateNo="T1AJ1",
#                                                               deviceCode="T1AJ001",
#                                                               boardingNumber=str(i),
#                                                               seatId=str(i+100),
#                                                               startPort="HET",
#                                                               flightDay=date[-2:],
#                                                               faceFeature=feature_8k_B,
#                                                               kindType=1,  # 类型：0：刷票 1：刷票放行
#                                                               largePhoto=largePhoto
#                                                               )
#         print("人工通道刷票响应" + res.text)
#         print("第%s个旅客特征添加完成..." % (i + 1))
#     time.sleep(555)


# while True:
#     for i in range(1000):
#         date = produce_flight_date()      #当天日期YYYYMMDD
#         feature_8k = read_feature("D:/pre_data/picture8k/%s.txt"%i)     #读取8k特征
#         lk_cname = "周志喜%s"%i        #中文姓名
#         # print("航班号:" + flight_no + ",登机序号:" + bdno)
#         #旅客去人工通道刷票
#         res = AirportProcess().api_face_security_manual_check(flightNo="AB0001",
#                                                                faceImage=cardPhoto,
#                                                                gateNo="T1AJ1",
#                                                                deviceCode="T1AJ001",
#                                                                boardingNumber=str(i),
#                                                                seatId=str(i),
#                                                                startPort="HET",
#                                                                flightDay=date[-2:],
#                                                                faceFeature=feature_8k,
#                                                                kindType=1,  # 类型：0：刷票 1：刷票放行
#                                                                largePhoto=largePhoto
#                                                                )
#         print("人工通道刷票响应" + res.text)
#         print("第%s个旅客特征添加完成..."%(i+1))
#     time.sleep(555)

#添加40个航班，每个航班350个人
main_path = r"D:\workfile\zhongkeyuan_workspace\test_photoes\\"
dir_list = os.listdir(main_path + "picture(现场照片)")
start_num = 50
end_num = 51
boarding_start = 0
boardingGate = "04A"
# flightNo = "AB1252"
# with open("feature_num.txt","w",encoding="utf-8") as f:
#     for dir in dir_list[:350]:
#         f.write(dir.split(".")[0] + "\n")

# print(dir_list[0].split(".")[0])
'''
cardPhoto = to_base64(main_path + "picture/%s"%dir_list[903])  # 身份证照片
feature_2k = read_feature(main_path + "picture2k/%s.txt" % dir_list[903].split(".")[0])  # 读取2k特征
# 旅客通道复核
res = AirportProcess().api_face_review_check(gateNo="T1AF1",
                              deviceId="T1AF001",
                              scenePhoto=cardPhoto,
                              sceneFeature=feature_2k)
print("通道复核响应" + res.text)
# '''

tmp_num_flight = 1
for j in range(start_num,end_num):
    date = produce_flight_date()  # 当天日期YYYYMMDD
    print("开始刷票采集航班AC12%s旅客。"%j)
    tmp_num_people = 1
    for i in range(boarding_start,boarding_start+1):
        cardPhoto = to_base64(main_path + "picture(现场照片)/%s"%dir_list[i])  # 身份证照片
        feature_8k = read_feature(main_path + "picture8k/%s.txt"%dir_list[i].split(".")[0])     #读取8k特征
        # feature_8k = read_feature(main_path + "picture8k/%s.txt" %i)  # 读取8k特征
        lk_cname = "测试%s"%i        #中文姓名
        # print("航班号:" + flight_no + ",登机序号:" + bdno)
        #旅客去人工通道刷票
        res = AirportProcess().api_face_security_manual_check(
                                                               flightNo="AC12%s"%j,
                                                               # flightNo=flightNo,
                                                               faceImage=cardPhoto,
                                                               gateNo="T1AJ1",
                                                               deviceCode="T1AJ001",
                                                               boardingNumber=str(tmp_num_people), #登机序列号
                                                               seatId=str(tmp_num_people) + "A",
                                                               startPort="HET",
                                                               flightDay=date[-2:],
                                                               faceFeature=feature_8k,
                                                               kindType=0,  # 类型：0：刷票 1：刷票放行
                                                               largePhoto=largePhoto
                                                               )
        print("人工通道刷票响应" + res.text)
        print("第%s个旅客特征添加完成..."%tmp_num_people)
        tmp_num_people += 1
    print("第%s个航班旅客特征添加完成..."%tmp_num_flight)
    tmp_num_flight += 1
    time.sleep(3)

    tmp_num = 1
    for h in range(boarding_start,boarding_start+1):
        cardPhoto = to_base64(main_path + "picture(现场照片)/%s"%dir_list[h])  # 身份证照片
        feature_2k = read_feature(main_path + "picture2k/%s.txt" % dir_list[h].split(".")[0])  # 读取2k特征
        # 旅客通道复核
        res = AirportProcess().api_face_review_check(gateNo="T1AF1",
                                      deviceId="T1AF001",
                                      scenePhoto=cardPhoto,
                                      sceneFeature=feature_2k)
        print("通道复核响应" + res.text)
        print("第%s个旅客复核完成..." %tmp_num)
        tmp_num += 1
        # time.sleep(0.1)
time.sleep(10)
#
flightDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:10]    #航班时间，格式为"2019-04-23"
tmp_num_flight = 1

for m in range(start_num,end_num):
    # flightNo = "AB12%s"%m
    flightNo = "AB1250"
    # flightNo = flightNo
    # boardingGate = str(m)

    #http其他航班
    res = AirportProcess().api_face_boarding_strange(flightNo=flightNo,
                                                     boardingGate=boardingGate,
                                                     deviceCode="T1ZZ002",
                                                     gateNo="01",
                                                     flightDay=flightDate               #YYYY-MM-DD
                                                     )
    print("变更登机口响应：" + res.text)
    time.sleep(0.2)
    #http开始登机
    res = AirportProcess().api_face_boarding_start(flightNo=flightNo,
                                                     boardingGate=boardingGate,
                                                     deviceCode="T1ZZ002",
                                                     gateNo="01",
                                                     flightDay=flightDate
                                                     )
    print("第%s个航班开始登机响应："%(m+1) + res.text)

    tmp_num = 1
    for n in range(boarding_start,boarding_start+1):
        cardPhoto = to_base64(main_path + "picture(现场照片)/%s"%dir_list[n])  # 身份证照片
        feature_2k = read_feature(main_path + "picture2k/%s.txt" % dir_list[n].split(".")[0])  # 读取2k特征
        # 登机口复核
        # res = AirportProcess().api_face_boarding_review_check(faceImage=cardPhoto,
        #                                                       faceFeature=feature_2k,
        #                                                       deviceCode="T1DJ001",
        #                                                       boardingGate=boardingGate,
        #                                                       flightNo=flightNo,
        #                                                       flightDay=produce_flight_date(),  # （yyyyMMdd）
        #                                                       gateNo="01"
        #                                                       )
        # print("第%s个旅客登机口复核响应"%tmp_num + res.text)

        #登机口人工通道
        print()
        res = AirportProcess().api_face_boarding_manual_check(
            reqId=get_uuid(),
            flightNo="AB1250",
            date="20200422",
            boardingGate="04A",
            deviceCode="T1DJ001",
            gateNo="01",
            #cardId="50038219990909707%d" %n,
            scenePhoto="",
            sourceType=0,  #0-放行，1-报警
            passengerName="旅客姓名", #旅客姓名
            boardingNumber=str(n),
            #seatId=str(tmp_num_people) + "A"  # 座位号
        )
        print("登机口人工通道: "+res.text)
        tmp_num += 1
    # #结束登机
    # res = AirportProcess().api_face_boarding_finish(flightNo=flightNo,
    #                                                  boardingGate=boardingGate,
    #                                                  deviceCode="T1ZZ002",
    #                                                  gateNo="01",
    #                                                  flightDay=flightDate  # YYYY-MM-DD
    #                                                  )
    # print("第%s个航班结束登机响应：" %tmp_num_flight + res.text)

# 建库人数查询
# def query_num():
#     flightDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:10]    #航班时间，格式为"2019-04-23"
#     while True:
#         num = random.randint(50,100)
#         start_time = time.clock()
#         res = AirportProcess().api_v1_face_boarding_passenger_query(flightNo="AB12%s"%num,  # 必须,航班号
#                                                                     date=flightDate,  # 必须,日期yyyy-MM-dd
#                                                                     queryType=0,  # 必须,查询类型：0-建库旅客查询；1-已登机旅客查询；2-未登机旅客查询
#                                                                     pageNum=1,  # 必须，分页页码
#                                                                     pageSize=1000,  # 必须，分页长度
#                                                                     isCount=1,  # 必须，为1返回总数
#                                                                     gateNo="",
#                                                                     boardingGate=str(num)
#                                                                     )
#         end_time = time.clock()
#         print("建库人数查询" + res.text)
#         print("查询用时%s秒。"%(end_time-start_time))
# for i in range(1):
#     th = threading.Thread(target=query_num)
#     th.start()

# def boarding_review_check():
#     while True:
#         num = random.randint(50, 70)
#         boardingGate = str(num)
#         flightNo = "AB12%s"%num
#         cardPhoto = to_base64(main_path + "picture(现场照片)/%s"%dir_list[0])  # 身份证照片
#         feature_2k = read_feature(main_path + "picture2k/%s.txt" % dir_list[0].split(".")[0])  # 读取2k特征
#         # 登机口复核
#         res = AirportProcess().api_face_boarding_review_check(faceImage=cardPhoto,
#                                                               faceFeature=feature_2k,
#                                                               deviceCode="T1DJ001",
#                                                               boardingGate=boardingGate,
#                                                               flightNo=flightNo,
#                                                               flightDay=produce_flight_date(),  # （yyyyMMdd）
#                                                               gateNo="01"
#                                                               )
#         print(res.text)
# for j in range(20):
#     th = threading.Thread(target=boarding_review_check)
#     th.start()


# #把图片按0开始重命名
# dir_list = os.listdir(r"D:\pre_data\picture(现场照片)")
# print("共%s张图片。"%len(dir_list))
# for i in range(len(dir_list)):
#     with open("D:/pre_data/picture(现场照片)/"+dir_list[i],"rb") as f:
#         img = f.read()
#     with open("D:/pre_data/新建文件夹/%s.jpg"%i,"wb") as f:
#         f.write(img)
#     print("第%s张图片copy完成。"%(i+1))


# tmp文件中图片（旧版SDK提取的特征），服务器用新版SDK识别，统计识别分数并写入excel
# import xlwt
#
#
#
#
#
#
# workbook = xlwt.Workbook()
# worksheet = workbook.add_sheet('登机口识别分数统计')
# for i in range(10):
#     worksheet.write(i,2,i)
# workbook.save(r'C:\Users\admin\Desktop\登机口识别分数统计.xlsx')




