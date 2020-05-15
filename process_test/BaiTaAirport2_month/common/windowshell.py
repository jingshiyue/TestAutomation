# coding:utf-8
import os
import psutil
import json
import subprocess
import time


def cuowuInfo():
    string ='error'
    with open('C:/Users/chenkeyun/Desktop/xx.txt') as f:
        data = f.readlines()
        for p, line in enumerate(data):
            if string in line:
                print(p+1, line)
            else:
                pass


def memory1():
    """
    #内存使用率方法
    :return:
    """
    memory = psutil.virtual_memory()
    b = {'已经使用的内存：': memory.used, '一共的内存：': memory.total, '使用率：': float(memory.used)/float(memory.total)*100}
    print(b)


def cpu():
    """#cpu使用率"""
    while True:
        time.sleep(1)
        cpu_liyonglv = psutil.cpu_percent()
        print(json.dumps(cpu_liyonglv))
        if cpu_liyonglv > 10:
            baojing()


def cipan():
    """
    #磁盘使用率
    :return:
    """
    disk=psutil.disk_partitions()
    # 以列表的形式返回挂载的分(设备，安装点，fstype, opts)“opts”字段是一个用逗号分隔的原始字符串，表示挂载
    for i in disk:
        disk_use = psutil.disk_usage(i.device)
        a = {'磁盘': i.device,
             '分区格式': i.fstype,
             '使用了：': disk_use.used/1024/1024/1024,
             '空闲：': disk_use.free/1024/1024/1024,
             '使用率：': disk_use.percent}
        print(json.dumps(a))





def baojing():
        # winsound.PlaySound("ALARM8",winsound.SND_ALIAS)
        print('报警了')


def get():
    pid = psutil.pids()  # 所有线程 返回一个list的pid
    print(pid)
    for k, i in enumerate(pid):
        try:
            proc = psutil.Process(i)
            print(proc)
            s = {'序号:': k, 'PID:': i, 'cpu占用率:': proc.memory_percent(), '执行程序名字:': proc.name()}
            print(s)
        except psutil.AccessDenied:
            print("psutil.AccessDenied")
    mount = subprocess.getoutput("cat  /etc/fstab  >/zhaokexin/a.txt")
    size = subprocess.getoutput("df  >/zhaokexin/b.txt")


def panduanguazai():
    str=input('请输入你要查询的挂载盘符:')
    with open('/zhaokexin/a.txt', encoding='utf-8') as e, open('/zhaokexin/b.txt', encoding='utf-8') as k:
        data1 = e.readlines()
        data2 = k.readlines()
        for t in data1:
            for r in data2:
                if str in t.split() and str in r.split():
                    print(str + "挂载盘存在！")
                else:
                    print("挂载盘不存在，请重新挂载...")


def oom_adj():
    pid = psutil.pids()
    pids = subprocess.getoutput("ps aux |grep mysql ")
    for pid1 in pids:
        p = psutil.process_iter(pid1)  # 返回一个生成器，为所有对象生成一个流程实例运行流程。
        print(pid, p.name())


def get_oom_id(processname):
    fd = os.popen("ps -e|grep "+ processname)
    list = fd.readlines()
    dict = {}
    for line in list:
        res = line.split()[0]
        fs = os.popen('cat /proc/'+res+'/oom_adj')
        data = fs.read()
        dict[res] = data
    return dict


if __name__ == '__main__':
    get()