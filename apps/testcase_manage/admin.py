from django.contrib import admin

from testcase_manage.models import TestCase

class TestCaseAdmin(admin.ModelAdmin):
    list_per_page = 50
    search_fields = ('casename','api',)
    list_display = ('casename','modular_name','api','user','create_time','update_time')
    # ordering = ('create_time','update_time')
    list_filter = ('product_name','modular_name',)

admin.site.register(TestCase,TestCaseAdmin)
