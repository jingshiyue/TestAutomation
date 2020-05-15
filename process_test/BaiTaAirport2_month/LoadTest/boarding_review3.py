# coding:utf-8
from locust import HttpLocust,seq_task,TaskSequence,task
from BaiTaAirport2_month.API.AirportProcess import *
import json
from multiprocessing import Process

"""3、40个航班（每个航班500人），对一个航班进行30个并发压力测试（随机一个航班500人特征），
服务器响应时间小于1s，识别成功率100%，持续时间半小时。"""

"""操作步骤
1.先通过刷票接口建立40航班500人的底库
2.在对其他航班人员（随机取值）进行30并发压力测试
3.查看服务器响应情况
"""

board_no_list = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028', '029', '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041', '042', '043', '044', '045', '046', '047', '048', '049', '050', '051', '052', '053', '054', '055', '056', '057', '058', '059', '060', '061', '062', '063', '064', '065', '066', '067', '068', '069', '070', '071', '072', '073', '074', '075', '076', '077', '078', '079', '080', '081', '082', '083', '084', '085', '086', '087', '088', '089', '090', '091', '092', '093', '094', '095', '096', '097', '098', '099', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298', '299', '300', '301', '302', '303', '304', '305', '306', '307', '308', '309', '310', '311', '312', '313', '314', '315', '316', '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328', '329', '330', '331', '332', '333', '334', '335', '336', '337', '338', '339', '340', '341', '342', '343', '344', '345', '346', '347', '348', '349', '350', '351', '352', '353', '354', '355', '356', '357', '358', '359', '360', '361', '362', '363', '364', '365', '366', '367', '368', '369', '370', '371', '372', '373', '374', '375', '376', '377', '378', '379', '380', '381', '382', '383', '384', '385', '386', '387', '388', '389', '390', '391', '392', '393', '394', '395', '396', '397', '398', '399', '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422', '423', '424', '425', '426', '427', '428', '429', '430', '431', '432', '433', '434', '435', '436', '437', '438', '439', '440', '441', '442', '443', '444', '445', '446', '447', '448', '449', '450', '451', '452', '453', '454', '455', '456', '457', '458', '459', '460', '461', '462', '463', '464', '465', '466', '467', '468', '469', '470', '471', '472', '473', '474', '475', '476', '477', '478', '479', '480', '481', '482', '483', '484', '485', '486', '487', '488', '489', '490', '491', '492', '493', '494', '495', '496', '497', '498', '499', '500']

board_gate = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']

flight_no_list = ['YQ87264', 'LF04673', 'WI94570', 'SG33727', 'YD59312', 'ID53023', 'GE07650', 'IX18314', 'LK99271', 'JZ60127', 'EG25502', 'OH04807', 'XW94601', 'EA26124', 'MD59156', 'BE99637', 'HS92900', 'IV60357', 'SS26807', 'HF86028', 'YP98722', 'SA30101', 'XM48762', 'QU04414', 'XT49240', 'OZ43100', 'ZX17938', 'NS42195', 'IP92479', 'DC87739', 'XS62552', 'JF79829', 'MG08632', 'MS18093', 'GZ63802', 'CJ43689', 'NB59671', 'KS98119', 'ID78931', 'TO89296']


class MyProcess3(Process):
    def __init__(self, nub):
        Process.__init__(self)
        self.no = nub

    def run(self):
            flight_no = flight_no_list[self.no-1]
            logger.info("开始开启多进程"+"flight_no为："+flight_no+"index为"+str(self.no)+self.name)
            aa = 0
            start_index = self.no*500-500
            end_index = self.no*500
            while start_index < end_index:
                # 开始进行中转采集
                res = AirportProcess().api_face_transfergate_ticket_collect(reqId=get_uuid(),
                                                                            flightNo=flight_no,
                                                                            faceImage=to_base64(r"C:\chenkeyun\OtherFile\IDcard\0.jpg"),
                                                                            deviceCode="T3ZZ003",
                                                                            gateNo="T3ZZ3",
                                                                            boardingNumber=board_no_list[aa],
                                                                            flightDay=produce_flight_day(),
                                                                            faceFeature=get_txt(shiwanid8k_features+"/"+str(start_index)+".txt"),
                                                                            sourceType="0")
                aa += 1
                start_index += 1
                print(res)
            logger.info("flight_no为："+flight_no+"index为"+str(self.no)+self.name+"\n"+"加载完毕")


class BoardingReview3(TaskSequence):
    # 登机口复核接口
    @staticmethod
    def build_feature3():
        for i in range(0, 40):
            a = AirportProcess().api_face_notice_cratelib(reqId=get_uuid(),
                                                          flightNo=flight_no_list[i],
                                                          date=produce_flight_date(),
                                                          boardingGate=board_gate[i],
                                                          deviceCode="T3DJ001",
                                                          number=500,
                                                          outTime=get_flight_out_time())
            print(a)
        print("40个登机口全部建库完成")

    @task
    def post_boarding_review3(self):
        # self.host + self.boardinggate_server + "/api/v1/face/boarding/check"  # 登机口复核
        random_index = random.randint(1, 40)
        features_index = random.randint(random_index*500-500, random_index*500-500-1)
        board = board_no_list[random_index]
        body = {"reqId": get_uuid(),
                "faceImage": to_base64(r"C:\chenkeyun\OtherFile\IDcard\0.jpg"),
                "faceFeature": get_txt(shiwanid2k_features+"/"+str(features_index)+".txt"),
                "deviceCode": "T3DJ001",
                "boardingGate": str(board_gate[random_index-1]),
                "flightNo": flight_no_list[random_index-1],
                "flightDay": produce_flight_date()}
        with self.client.post(url="/boardinggate-server/api/v1/face/boarding/check",
                              json=body,
                              headers=AirportProcess().get_headers("/api/v1/face/boarding/check"),
                              verify=False,
                              catch_response=True) as response:
            json_data = json.loads(str(response.text))
            try:
                if json_data["status"] == 0 and json_data["result"] == 0:
                    response.success()
                    print(json_data)
                else:
                    response.failure("识别错误")
            except:
                response.failure("解析错误")
                logger.error(json_data)


class BehaviorBoardingReview1(HttpLocust):
    task_set = BoardingReview3
    max_wait = 6000
    min_wait = 6000
    host = "http://192.168.1.106:9091"


if __name__ == '__main__':
    # 开启多进程进行40个航班500人员加入
    thre = []
    for i in range(1, 41):
        thre.append(MyProcess3(i))
    for k in thre:
        k.start()
    # 建库通知
    # BoardingReview3.build_feature3()
    # print("结束")
    # time.sleep(10000)

    # current_path = os.path.dirname(os.path.realpath(__file__))
    # command1 = "c:"
    # command2 = r"cd %s" % current_path
    # command3 = r"locust -f boarding_review2.py -P 8100 --web-host=127.0.0.1"
    # os.system(command1)
    # os.system(command2)
    # os.system(command3)
    pass