# coding:utf-8
import logging
import os
current_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")

logger_man = logging.getLogger(__name__)
logger_man.setLevel(level=logging.DEBUG)
handler = logging.FileHandler(current_path+"/"+"测试人工通道网关异常.log", encoding="utf-8")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.INFO)
logger_man.addHandler(handler)
logger_man.addHandler(console)