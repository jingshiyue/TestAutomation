from django.shortcuts import render
from django.http import HttpResponse
from .models import TestCase
import logging
from product_manage.models import Product,Notifier,Modular
from django.http import JsonResponse
from django.conf import settings
logger = logging.getLogger(__name__)
from conftest import read_from_config,write_to_config
import queue,threading
import time,os

def run_test(que):
    import os
    os.system("python runCase.py")
    logger.info("Thread: run_test complate ...")
    que.put("COMPLATE")
    exit()

def testcase_index(request):
    if request.method =="GET":
        products = Product.objects.all()
        modulars = Modular.objects.all()
        # cases = TestCase.objects.all().filter(product_name__name=product,modular_name__name=modular)
        cases = TestCase.objects.all()
        # return HttpResponse(obj)
        return render(request,'testcase_manage/index.html',locals())  #context={'objs':objs}
    if request.method =="POST":
        logger.info(request.POST)  # <QueryDict: {'modularNum': ['4', '6'], 'products': ['动态布控']}>
        product = request.POST.get("products")
        modular_ids_list = request.POST.getlist("modularNum")
        casesJson = {}
        ids = ""
        for id in modular_ids_list:
            cases = TestCase.objects.all().filter(product_name__name=product,modular_name__id=id)
            logger.info(id)
            ids += id + ","
            for case in cases:
                casesJson.setdefault(case.id,{})
                casesJson[case.id].setdefault("casename",case.casename)
                casesJson[case.id].setdefault("api",case.api)
                casesJson[case.id].setdefault("desc",case.desc)
                casesJson[case.id].setdefault("file_path",case.file_path)
        rst = JsonResponse(casesJson)
        logger.info(casesJson)
        try:
            write_to_config("testbed.ini","Product","name",product)
            write_to_config("testbed.ini","Modular","id",ids)
        except Exception as e:
            logger.info(e)
        return rst

def detail(request):
    if request.method =='GET':
        id = request.GET.get("id")
        logger.info(id)
        case = TestCase.objects.all().get(id=id)
        logger.info(case.casename)
        time.sleep(.5)
        return render(request,"testcase_manage/detail.html",locals())

def login(request):
    return render(request,"testcase_manage/login.html",locals())

def queryModulars(request):
    if request.method == 'POST':
        logger.info(request.POST)
        productName = request.POST.get("products")
        logger.info(productName)
        logger.info(type(productName))
        modulars = Product.objects.all().get(name=productName).modular.all()
        modularsJson = {}
        for modular in modulars:
            # modularsJson.setdefault("id",modular.id)
            modularsJson.setdefault(modular.id,modular.name)
        logger.info(modularsJson)
        rst = JsonResponse(modularsJson)
        logger.info(rst)
        return rst

def generateCaseInfo(request):
    """
    生成runCase.py脚本
    """
    from startRun import send_email
    if request.method == 'POST':
        logger.info(request.POST) #<QueryDict: {'caseNum': ['6', '7']}
        #ids = request.POST.getlist('caseNum') #['6', '7']
        ids = [int(x) for x in request.POST.getlist('caseNum')]
        timeStr = time.strftime('%Y%m%d%H%M%S',time.localtime())
        from startRun import head,foot,content_danjiekou,content_liucheng
        f = open("runCase.py","w",encoding='utf-8')
        f.write(head)
        casesStr = ""
        for id in ids:
            case = TestCase.objects.all().get(id=id)
            casesStr += case.casename + ","
            if case.case_type == "单接口":
                f.write(content_danjiekou %(case.casename.replace("-","_"),case.casename,case.desc))
            if case.case_type == "流程":
                scripts_path = case.file_path
                f.write(content_liucheng.format(case.casename.replace("-","_"),scripts_path,case.desc) )
        f.write(foot.format(timeStr))
        f.close()

        write_to_config("testbed.ini","TestCase","name",casesStr)
        write_to_config("testbed.ini","TestCase","id",str(ids))
        productName = read_from_config("testbed.ini","Product","name")
        que = queue.Queue()
        t1 = threading.Thread(target=run_test,args=[que])
        t1.setDaemon(True)
        t1.start()
        
        t2 = threading.Thread(target=send_email,args=[que,productName,timeStr])
        t2.setDaemon(True)
        t2.start()

        content = """
            <h3>后台正在测试，测试完毕后会收到邮件提醒...</h3>
            <p>当前测试用例条数: {0} </p>
            <p>测试报告路径:<a href="{1}">{1}</a></p>
        """.format(len(ids),r"http://192.168.1.42:8000/report/report_"+timeStr+".html")
        time.sleep(2)
        return HttpResponse(content)

def getReport(request,file):
    logger.info("********getReport**************")
    logger.info(file)
    return render(request, file + '.html')

