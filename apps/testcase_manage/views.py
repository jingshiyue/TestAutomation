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
logger = logging.getLogger(__name__)
def testcase_index(request):
    objs = TestCase.objects.all()
    # return HttpResponse(obj)
    logger.info(objs)
    return render(request,'testcase_manage/index.html',locals())  #context={'objs':objs}
