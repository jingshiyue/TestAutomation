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
    if request.method == 'POST':
        logger.info(request.POST) #<QueryDict: {'caseNum': ['6', '7']}
        #ids = request.POST.getlist('caseNum') #['6', '7']
        ids = [int(x) for x in request.POST.getlist('caseNum')]
        import time,os
        time.sleep(3)
        from startRun import head,foot,content
        f = open("runCase.py","w",encoding='utf-8')
        f.write(head)
        for id in ids:
            case = TestCase.objects.all().get(id=id)
            f.write(content %(case.casename.replace("-","_"),case.casename))
        f.write(foot)
        f.close()
        os.system("runCase.py")
        content = """<h3>generate config sucessfully...</h3>
                     %d 条用例将要执行测试...""" %len(ids)
                     
        return HttpResponse(content)