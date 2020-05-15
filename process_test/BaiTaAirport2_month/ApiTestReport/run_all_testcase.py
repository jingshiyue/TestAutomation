# coding:utf-8
import os
if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.realpath(__file__)
    testcasepath1 = os.path.dirname(current_path)
    testcasepath2 = os.path.join(testcasepath1, "testapi")
    print(current_path)
    print(testcasepath2)
    comm2 = "cd %s" % testcasepath2
    comm3 = r"pytest C:\chenkeyun\projectself\pythonproject\BaiTaAirport2_month\testapi\ --html=./report.html"
    os.system(comm2)
    os.system(comm3)
