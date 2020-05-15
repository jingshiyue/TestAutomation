# import os

# import pytest
# from django.http import HttpResponse


# def get_data(req):
#     pytest.main(["-vv", "-s", "testcase_manage/test_api.py", "--color=no", "--alluredir=./report/xml"])
#     os.system("allure generate --clean ./report/xml/ -o ./report/html/ ")
#     return HttpResponse("测试完成")

from django.shortcuts import render
from django.http import HttpResponse
from .models import TestCase
import logging
from product_manage.models import Product,Notifier,Modular
from django.http import JsonResponse

logger = logging.getLogger(__name__)
def testcase_index(request):
    if request.method =="GET":
        products = Product.objects.all()
        modulars = Modular.objects.all()
        # cases = TestCase.objects.all().filter(product_name__name=product,modular_name__name=modular)
        cases = TestCase.objects.all()
        # return HttpResponse(obj)
        return render(request,'testcase_manage/index.html',locals())  #context={'objs':objs}
    if request.method =="POST":
        logger.info(request.POST) #<QueryDict: {'products': ['动态布控'], 'modulars': ['数据平台']}>
        product = request.POST.get("products")
        modular = request.POST.get("modulars")
        cases = TestCase.objects.all().filter(product_name__name=product,modular_name__name=modular)
        logger.info(cases)
        casesJson = {}
        for case in cases:
            logger.info(case.id)
            casesJson.setdefault(case.id,{})
            casesJson[case.id].setdefault("casename",case.casename)
            casesJson[case.id].setdefault("api",case.api)
            casesJson[case.id].setdefault("user",case.user.get_username())
            # casesJson.setdefault("url",case.url)
        logger.info(casesJson)
        rst = JsonResponse(casesJson)
        logger.info(rst)
        return rst


def queryModulars(request):
    if request.method == 'POST':
        logger.info("queryModulars.POST")
        productName = request.POST.get("product")
        logger.info(productName)
        modulars = Product.objects.all().get(name=productName).modular.all()
        modularsStr = "["
        for modular in modulars:
            modularsStr = modularsStr + modular.name + ","
        modularsStr = modularsStr[:-1] + "]"
        rst = HttpResponse(modularsStr)
        # logger.info(modularsStr)
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
        import time,os
        timeStr = time.strftime('%Y%m%d%H%M%S',time.localtime())
        from startRun import head,foot,content_danjiekou,content_liucheng
        f = open("runCase.py","w",encoding='utf-8')
        f.write(head)
        for id in ids:
            case = TestCase.objects.all().get(id=id)
            if case.case_type == "单接口":
                f.write(content_danjiekou %(case.casename.replace("-","_"),case.casename))
            if case.case_type == "流程":
                scripts_path = case.file_path
                f.write(content_liucheng.format(case.casename.replace("-","_"),case.casename,scripts_path))
        f.write(foot.format(timeStr))
        f.close()
        os.system("start runCase.py")
        content = """<h3>后台正在测试，测试完毕后会收到邮件提醒...</h3>
                     <p>当前测试用例条数: {0} </p>
                     <p>测试报告路径:<a href="{1}">{1}</a></p>
                     """.format(len(ids),r"http://192.168.1.42:8000/report/report_"+timeStr+".html")
        send_email("动态布控",timeStr)
        return HttpResponse(content)