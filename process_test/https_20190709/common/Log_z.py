#!/usr/bin/python3
# Time : 2019/7/19 9:29
# Author : zcl

"""
封装log方法

"""
import logging
import os
import time

import logging
import time
import os
import threading

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = os.path.join(parentdir,"Log",("test_log_" + str(time.time()).split(".")[0] + ".log"))
#     path = os.path.dirname(os.path.join(os.path.abspath(os.pardir),'Log'))
#     log_file = path+'/Log/log.log'
#     err_file = path+'/Log/err.log'
#print(log_file)
class Log:
        #----------------------------------------------------------------------
        def __init__(self):
                """"""
                #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                format='%(asctime)s[%(filename)s line:%(lineno)d] %(levelname)s: %(message)s'
                formatter = logging.Formatter(format)
                # 1、创建一个logger
                self.logger = logging.getLogger()
                self.logger.setLevel(logging.DEBUG)

                # 2、创建一个handler，用于写入日志文件
                fh = logging.FileHandler(log_file)
                fh.setLevel(logging.DEBUG)
                fh.setFormatter(formatter)  #给handler添加formatter

                #3、 再创建一个handler，用于输出到控制台
                ch = logging.StreamHandler()
                ch.setLevel(logging.INFO)
                #ch.setLevel(logging.INFO)
                ch.setFormatter(formatter)  #给handler添加formatter

                #4、给logger添加handler
                self.logger.addHandler(fh)
                self.logger.addHandler(ch)

        #----------------------------------------------------------------------
        def get_logger(self):
                """"""
                return self.logger


        #----------------------------------------------------------------------
        def start_case(self,case_name):
                """"""
                self.logger.debug("**********%s starts*************" %case_name)







########################################################################
class mylog:
        logger = None
        mutex = threading.Lock()

        @staticmethod
        def get_log():

                if mylog.logger is None:
                        mylog.mutex.acquire()
                        mylog.logger = Log()
                        mylog.mutex.release()

                return mylog.logger





if __name__ == '__main__':
        logger = mylog.get_log().get_logger()
        logger.debug("i am ok")
        mylog.get_log().start_case("first case test")

