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
        logger.info(request.POST) #<QueryDict: {'products': ['机场流程']}>
        import os
        os.system("startRun.py")
        return HttpResponse("<h2>配置完成，可以进行下一步测试...</h2>")

def queryModulars(request):
    logger.info("+++++++++")
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
        logger.info(modularsStr)
        return rst