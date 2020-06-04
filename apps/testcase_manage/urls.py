from django.urls import path,re_path
from django.conf import settings
from . import views

app_name = 'testcase_manage'
urlpatterns = [
    path('index/',views.testcase_index,name='testcaseIndex'),  #/testcase/index
    path('login/',views.login,name='login'), 
    path('detail/',views.detail,name='testcaseDetail'), 
    path('queryModulars/',views.queryModulars,name='queryModulars'),
    path('generateCaseInfo/',views.generateCaseInfo,name='generateCaseInfo'),
    re_path('report/(?P<file>\w+)\.html$',views.getReport,name='report')
#     re_path(r'(?P<fl_name>\w+)\.html$', views.pt_htm),
] 
