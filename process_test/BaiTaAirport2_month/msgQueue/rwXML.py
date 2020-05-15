# coding:utf-8
from xml.etree import ElementTree as ET

from Airport.msgQueue.msg import *

ET.register_namespace(prefix="", uri="http://schemas.datacontract.org/2004/07/Xasd.FASC.SECM.Entity")
tree = ET.parse(r"C:\Users\admin\Desktop\lkxx.xml")
root = tree.getroot()

lk_id = root[3][0]
for i in lk_id:
    print(i.text)
print(root[3][0][15].text)
root[3][0][15].text = "0001"  # 航班号
root[3][0][9].text = "20180929"  # 航班日期
root[3][0][6].text = "20180929103700"  # 值机日期
root[3][0][20].text = "20180929103700"  # 离港日期

tree.write(file_or_filename="lkxx1.xml",
           encoding="utf-8",
           #default_namespace="http://schemas.datacontract.org/2004/07/Xasd.FASC. SECM.Entity",
           xml_declaration=True)

with open("lkxx1.xml", "rb") as fp:
    data = fp.read().decode("utf-8")
    print(data)
    send_msg(data)





















