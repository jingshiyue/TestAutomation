#!/usr/bin/python3
# Time : 2019/7/17 17:04 
# Author : zcl
import requests
import random
from https_20190709.API_https.BlackList import *
from https_20190709.common.common_method import *
from https_20190709.common.params_init_z import params
from https_20190709.common.common_method import *
blApi = BlackListApi()

#https://192.168.5.15:4433/security-server/api/v1/face/security/face-check
host = "https://192.168.5.15:4433/security-server"
# certificate_file = "D:/workfile/workspace/https_20190709/API_https/cacert.crt"
certificate_file = "D:/workfile/workspace/https_20190709/API_https/cacert.crt"
# url: api/v1/face/security/face-check

photo_base64 = to_base64(r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture(现场照片)\0.jpg")
idcard8k = r"D:\workfile\zhongkeyuan_workspace\test_photoes\idcard8k"
picture8k = r"D:\workfile\zhongkeyuan_workspace\test_photoes\picture8k"
cnt = 1001 #idcard8k文件夹里文件数量
jpg_name = str(random.randint(0,cnt))+".jpg"
def test_api_face_security_face_check(reqId="", #必须 "3Fc5353D-87f0-946c-53FE-17BB6BB6",
                                      gateNo="", #必须  "T1AJ1"
                                      deviceId="",#必须 "T1AJ001"
                                      cardType="", #2 必须,integer
                                      idCard="",#必须 "500382199512303576"
                                      nameZh="",#必须 "蒋勇"
                                      nameEn="",
                                      age="",#integer
                                      sex="",#integer
                                      birthDate="",  #必须  string "1976-12-23"
                                      address="",
                                      certificateValidity="", #必须  "20120222-20220222"
                                      nationality="", #必须 "哈巴河县"
                                      ethnic="", #必须 "蒙古族"
                                      contactWay="", #必须  "STow"
                                      scenePhoto="",#必须  "TlEb"
                                      sceneFeature="",#必须 "wB0@["
                                      cardPhoto="",#必须 "$n&X925"
                                      cardFeature=""):#必须 "hr03w"
                                      #largePhoto=""): #必须 "sgQO"

    body = {
    "reqId":reqId,
    "gateNo":gateNo,
    "deviceId":deviceId,
    "cardType":cardType,
    "idCard":idCard,
    "nameZh":nameZh,
    "nameEn":nameEn,
    "age":age,
    "sex":sex,
    "birthDate":birthDate,
    "address":address,
    "certificateValidity":certificateValidity,
    "nationality":nationality,
    "ethnic":ethnic,
    "contactWay":contactWay,
    "scenePhoto":scenePhoto,
    "sceneFeature":sceneFeature,
    "cardPhoto":cardPhoto,
    "cardFeature":cardFeature,
    # "largePhoto":largePhoto
    }
    url =host + "/api/v1/face/security/face-check"
    headers = blApi.get_headers(sign="/api/v1/face/security/face-check")
    # headers = blApi.get_headers("/api/v1/face/security/face-check")
    certificate = certificate_file
    # res = requests.post(url=url,headers=blApi.get_headers("/api/v1/face/security/face-check"),json=body,verify=certificate)

    res = requests.post(url=url,
                        headers=headers,
                        json=body,
                        verify=certificate)
    logger.debug(url)
    logger.debug(res.status_code)
    res.close()
    return res

params_instance = params("my_interface_test.yml","test_api_face_security_face_check")
all_params = params_instance.get_all_params()
must_params = params_instance.get_must_params()

for key in all_params.keys():
    if key == "reqId":
        all_params[key] = get_uuid()
    elif key == "scenePhoto":
        all_params[key] = photo_base64
    elif key == "sceneFeature":
        all_params[key] = read_feature(os.path.join(picture8k,str(random.randint(0,cnt))+".txt"))
    elif key == "cardPhoto":
        all_params[key] = photo_base64
    elif key == "cardFeature":
        all_params[key] = read_feature(os.path.join(idcard8k,str(random.randint(0,cnt))+".txt"))
    # elif key == "largePhoto":
    #     all_params[key] = photo_base64

# logger.debug(all_params)
content = test_api_face_security_face_check(all_params)
logger.debug(content.text)





















