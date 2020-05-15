# coding:utf-8
from BaiTaAirport2_month.common.common_method import get_features
import multiprocessing


def get_features_txt(picturespath: str, txtpath: str, mode: str, startpictureindex: int,
                     endpictureindex: int) ->None:
    """
    :param picturespath: 要提取的图片的路径
    :param txtpath: 提取后的图片特征存放的文件夹路径
    :param mode: 提取特征的模式
    :param startpictureindex:  图片文件夹的开始索引
    :param endpictureindex:  图片文件夹的结束索引
    :return:
    """
    for i in range(startpictureindex, endpictureindex+1):
        a = get_features(picturespath+"/"+str(i)+".jpg", mode=mode)
        with open(txtpath+"/"+str(i)+".txt", "w") as fp:
            fp.write(a)
        print("第%d次提取结束" % i)


class LiveFeature2k(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)

    def run(self):
        get_features_txt(picturespath="C:/chenkeyun/OtherFile/picture",
                         txtpath="C:/chenkeyun/OtherFile/picturef2k",
                         mode="2K",
                         startpictureindex=41510,
                         endpictureindex=100000)


class LiveFeature8k(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)

    def run(self):
        get_features_txt(picturespath="C:/chenkeyun/OtherFile/picture",
                         txtpath="C:/chenkeyun/OtherFile/picturef8k",
                         mode="8K",
                         startpictureindex=41509,
                         endpictureindex=100000)

if __name__ == '__main__':
    threadings_lisrt = []
    threadings_lisrt.append(LiveFeature2k())
    threadings_lisrt.append(LiveFeature8k())
    for l in threadings_lisrt:
        l.start()