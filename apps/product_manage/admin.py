from django.contrib import admin

from product_manage.models import Product, Modular,Notifier


class ProductAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ('name',)
    # form = ArticleForm
    list_display = ('name','user','create_time','update_time','description',)
    ordering = ('name','user','create_time','update_time','description',)
    # list_filter = (ArticleListFilter, 'status', 'type', 'category', 'tags')
    # filter_horizontal = ('tags',)
    # exclude = ('created_time', 'last_mod_time')

class ModularAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ('name',)
    list_display = ('name','user','to_product','host','create_time','update_time')
    ordering = ('name','user','to_product','host','create_time','update_time')

class NotifierAdmin(admin.ModelAdmin):
    list_per_page = 30
    search_fields = ('name','email',)
    list_display = ('name','email','create_time','update_time')
    ordering = ('name','email','create_time','update_time')


admin.site.register(Product,ProductAdmin)
admin.site.register(Modular,ModularAdmin)
admin.site.register(Notifier,NotifierAdmin)
