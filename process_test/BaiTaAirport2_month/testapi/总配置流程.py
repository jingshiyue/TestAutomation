
def qianzhi_27(idcard="027238198312134390",
              flight="qianzhi27",
              n=30027):
    """经停，登机口人工放行"""
    # 中转刷票采集
    # res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
    #     reqId=get_uuid(),
    #                                          flightNo=flight,
    #                                          faceImage=Base64Picture,
    #                                          deviceCode="T1ZZ001",
    #                                          gateNo="T1ZZ1",
    #                                          seatId="1",
    #                                          startPort="HET",
    #                                          boardingNumber="001",
    #                                          flightDay=produce_flight_day(),   # 传Dd
    #                                          faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                          sourceType="0"
    # )
    # print("开始进行中转刷票采集"+"\n"+res_collect.text)
    # 先值机
    # send_lkxx(lk_cardid=idcard,
    #           lk_chkt=get_time_mmss(),
    #           lk_cname="cky",
    #           lk_date=produce_flight_date(),
    #           lk_desk="TEN",
    #           lk_flight=flight,
    #           lk_id=get_uuid(),
    #           lk_bdno="001",
    #           lk_insur="1",
    #           lk_outtime=get_flight_out_time(2),
    #           lk_sex="1")
    # print("先开始值机")
    # time.sleep(1)

    # 闸门A-B进行安检
    # res_a = AirportProcess(host="http://192.168.1.105:9091/").api_security_ticket_check(reqId=get_uuid(),
    #                                                                                   gateNo="T1AJ1",
    #                                                                                   deviceId="T1AJ1",
    #                                                                                   cardType=0,
    #                                                                                   idCard=idcard,
    #                                                                                   nameZh="cky",
    #                                                                                   nameEn="cky",
    #                                                                                   age=get_age(idcard),
    #                                                                                   sex=0,
    #                                                                                   birthDate=get_birthday(idcard),
    #                                                                                   address="重庆市",
    #                                                                                   certificateValidity="20120101-20230202",
    #                                                                                   nationality="China",
    #                                                                                   ethnic="汉族",
    #                                                                                   contactWay="123456",
    #                                                                                   cardPhoto=Base64Picture,
    #                                                                                   fId=get_uuid())
    # print("经过闸门A"+"\n"+res_a.text)
    # time.sleep(1)

    # 进行闸门B
    # res_b = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard=idcard,
    #                                  nameZh="cky",
    #                                  nameEn="cky",
    #                                  age=get_age(idcard),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("开始进行闸门B"+"\n"+res_b.text)

    # 开始 安检1：1
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_anjian(anjiangateNo="T1AJ1",
    #                  anjiandeviceId="T1AJ001",
    #                  cardType=0,
    #                  idCard=idcard,
    #                  nameZh="cky",
    #                  nameEn="cky",
    #                  age=get_age(idcard),
    #                  sex=1,
    #                  birthDate=get_birthday(idcard),
    #                  address="重庆市大竹林街道",
    #                  nationality="中国",
    #                  ethnic="汉族",
    #                  scenePhoto=Base64Picture,
    #                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                  cardPhoto=Base64Picture,
    #                  cardFeature=get_txt(shiwanid8k_features+"/"+str(n)+".txt"))
    # print("安检1:1"+"\n"+res.text)

    # 安检人工放行
    # res = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_optcheck(reqId=get_uuid(),
    #                                       gateNo="T1AJ1",
    #                                       deviceId="T1AJ001",
    #                                       cardType="0",
    #                                       idCard=idcard,
    #                                       nameZh="cky",
    #                                       nameEn="cky",
    #                                       age=get_age(idcard),
    #                                       sex="1",
    #                                       birthDate=get_birthday(idcard),
    #                                       address="重庆市",
    #                                       certificateValidity="20120101-长期",
    #                                       nationality="China",
    #                                       ethnic="汉族",
    #                                       contactWay="0123456789",
    #                                       scenePhoto=Base64Picture,
    #                                       sceneFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                       cardPhoto=Base64Picture,
    #                                       cardFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"))
    # print("安检人工放行"+"\n"+res.text)
    # time.sleep(2)

    # 进行刷票
    # res_tricket = AirportProcess(host="http://192.168.1.105:9091/").api_face_security_manual_check(reqId=get_uuid(),
    #                                                                                                flightNo=flight,
    #                                                                                                faceImage=Base64Picture,
    #                                                                                                gateNo="T1AJ1",
    #                                                                                                deviceCode="T1AJ001",
    #                                                                                                boardingNumber="001",
    #                                                                                                seatId="001",
    #                                                                                                startPort="HET",
    #                                                                                                flightDay=produce_flight_day(),
    #                                                                                                faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
    #                                                                                                kindType=0)
    # print("开始进行刷票通过"+"\n"+res_tricket.text)

    # 开始进行通道复核
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_check(
    #     reqId=get_uuid(),
    #     gateNo="T1AF1",
    #     deviceId="T1AF001",
    #     scenePhoto=Base64Picture,
    #     sceneFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt")
    # )
    # print("通道复核"+"\n"+res1.text)

    # 进行通道复核放行
    # time.sleep(2)
    # res1 = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_manual_check(reqId=get_uuid(),
    #                                   gateNo="T1AF1",
    #                                   deviceId="T1AF001",
    #                                   scenePhoto=Base64Picture,
    #                                   cardNo=idcard,
    #                                   passengerName="cky",
    #                                   passengerEnglishName="cky",
    #                                   securityStatus="0",
    #                                   securityPassTime=get_time_mmss(),
    #                                   securityGateNo="T1AJ1",
    #                                   securityDeviceNo="T1AJ001",
    #                                   flightNo=flight,
    #                                   boardingNumber="001",
    #                                   sourceType="0")
    # print("通道复核放行"+"\n"+res1.text)

    # 进行自助闸机复核
    # time.sleep(2)
    # res_self = AirportProcess(host="http://192.168.1.105:9091/").api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"))
    # print("开始进行自助闸机复核"+"\n"+res_self.text)

    # 进行中转刷票采集
    res_collect = AirportProcess(host="http://192.168.1.105:9091/").api_face_transfergate_ticket_collect(
        reqId=get_uuid(),
                                             flightNo=flight,
                                             faceImage=Base64Picture,
                                             deviceCode="T1ZZ001",
                                             gateNo="T1ZZ1",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay=produce_flight_day(),   # 传Dd
                                             faceFeature=get_txt(shiwanli8k_features+"/"+str(n)+".txt"),
                                             sourceType="0"
    )
    print("开始进行中转刷票采集"+"\n"+res_collect.text)

    # 开始进行登机口建库
    time.sleep(1)
    res2 = AirportProcess(host="http://192.168.1.105:9091/").api_face_notice_cratelib(reqId=get_uuid(),
                                                                                      flightNo=flight,
                                                                                      date=produce_flight_date(),
                                                                                      boardingGate="22",
                                                                                      deviceCode="T1DJ001",
                                                                                      number=1,
                                                                                      outTime=get_flight_out_time(1))
    print("登机口建库"+"\n"+res2.text)
    time.sleep(1)

    # 开始进行登机口复核
    # res3 = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_review_check(
    #                             faceImage=Base64Picture,
    #                             faceFeature=get_txt(shiwanli2k_features+"/"+str(n)+".txt"),
    #                             deviceCode="T1DJ001",
    #                             boardingGate="22",
    #                             flightNo=flight,
    #                             flightDay=produce_flight_date()   # （yyyyMMdd）
    # )
    # print("登机口复核"+"\n"+res3.text)
    # time.sleep(1)

    # 进行登机口人工放行
    res_board_fang = AirportProcess(host="http://192.168.1.105:9091/").api_face_boarding_manual_check(
        reqId=get_uuid(),
        flightNo=flight,
        date=produce_flight_date(),
        boardingGate="22",
        deviceCode="T1DJ0011",
        gateNo="T1DJ1",
        cardId=idcard,
        scenePhoto=Base64Picture,
        sourceType="0",
        passengerName="cky",
        boardingNumber="001"
    )
    print("登机口人工放行"+"\n"+res_board_fang.text)
    time.sleep(1)