from django.urls import path
from django.conf import settings
from . import views

app_name = 'testcase_manage'
urlpatterns = [
    path('index/',views.testcase_index,name='testcaseIndex'),  #/testcase/index
    path('queryModulars/',views.queryModulars,name='queryModulars')
] 
