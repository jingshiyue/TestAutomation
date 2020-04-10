from django.contrib.auth.models import User
from django.db import models
from django.db import models

class BaseModel(models.Model):
    '''模型抽象基类'''
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='创建人')
    class Meta:
        abstract = True



class Notifier(BaseModel):
    """
    邮件抄送人列表
    """
    name = models.CharField(max_length=50, verbose_name='角色名')
    email = models.EmailField(verbose_name='邮箱地址')
    desc = models.TextField(verbose_name='描述', blank=True,help_text='选填')

    def __str__(self):
        return self.name + ': ' + self.email

    class Meta:
        verbose_name = '邮件抄送人'
        verbose_name_plural = '邮件抄送人'
        ordering = ['-update_time']

class Product(BaseModel):
    """
    项目表
    """
    projectType = (
        ('Web', 'Web'),
        ('App', 'App'),
        ('其他', '其他')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='项目名称')
    # version = models.CharField(max_length=50, verbose_name='版本')
    type = models.CharField(max_length=50, verbose_name='项目类型', choices=projectType)
    description = models.TextField(blank=True, verbose_name='描述')
    # notify = models.EmailField(max_length=50, verbose_name='项目关注人群',help_text='[173302591@qq.com]')
    # status = models.BooleanField(default=True, verbose_name='状态')
    notifier = models.ManyToManyField(Notifier,verbose_name='邮件抄送人', related_name='product',null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目管理'
        verbose_name_plural = '项目管理'


# class Role(models.Model):
#     """
#     角色表
#     """
#     id = models.AutoField(primary_key=True)
#     to_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='所属项目', related_name='role')
#     name = models.CharField(max_length=50, verbose_name='角色名')
#     account = models.CharField(max_length=20, verbose_name='用户名', help_text='角色对应的账户')
#     password = models.CharField(max_length=20, verbose_name='密码', help_text='角色对应的密码')
#     desc = models.TextField(verbose_name='描述', blank=True)

#     def __str__(self):
#         return self.to_product.name + ' ' + self.name

#     class Meta:
#         verbose_name = '角色管理'
#         verbose_name_plural = '角色管理'


class Modular(BaseModel):
    """
    模块表
    """
    id = models.AutoField(primary_key=True)
    to_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='所属项目', related_name='modular')
    name = models.CharField(max_length=50, verbose_name='模块名')  #没有blank,默认就是必填字段
    host = models.CharField(max_length=50, verbose_name='HOST', help_text='e.g. http://127.0.0.1:8000')
    # appid = models.CharField(max_length=64, verbose_name="模块ID", default='appid')
    # _authapi = models.CharField(max_length=64, verbose_name='鉴权api', default='/')
    # key = models.CharField(max_length=64, verbose_name="KEY", help_text="秘钥")

    def __str__(self):
        # return self.to_product.name + ' -> ' + self.name
        return self.name

    class Meta:
        verbose_name = '模块管理'
        verbose_name_plural = '模块管理'
