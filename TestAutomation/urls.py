from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('testcase/',include('testcase_manage.urls',namespace='testcase_manage'))
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.SCRIPTS_URL,document_root=settings.SCRIPTS_ROOT)
