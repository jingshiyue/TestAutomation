from django.urls import path,re_path
from django.conf import settings
from . import views

app_name = 'testcase_manage'
urlpatterns = [
    path('index/',views.testcase_index,name='testcaseIndex'),  #/index
    path('login/',views.login,name='login'), 
    path('detail/',views.detail,name='testcaseDetail'), 
    path('queryProjs/',views.queryProjs,name='queryProjs'),
    path('queryModulars/',views.queryModulars,name='queryModulars'),
    path('generateCaseInfo/',views.generateCaseInfo,name='generateCaseInfo'),
    re_path('report/(?P<file>\w+)\.html$',views.getReport,name='report'),
    re_path('casesManage/model.html',views.getModelHmtl,name='getModelHmtl')
] 
