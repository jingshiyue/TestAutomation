from django.db import models
from product_manage.models import BaseModel
from product_manage.models import Product,Modular
# class API(models.Model):
#     id = models.AutoField(primary_key=True)
#     modular_name = models.ForeignKey('product_manage.Modular', on_delete=models.SET_NULL, null=True,
#                                      verbose_name='所属项目')
#     api_path = models.CharField(max_length=128, verbose_name='接口路径', help_text='e.g. /login')
#     desc = models.CharField(max_length=128, verbose_name='接口描述')

#     def __str__(self):
#         return self.modular_name.name + " " + self.api_path

#     class Meta:
#         verbose_name = '接口管理'
#         verbose_name_plural = '接口管理'
import logging
logger = logging.getLogger(__name__)

class TestCase(BaseModel):
    '''
        用例模块: 分为单接口、流程
    '''
    HTTP_METHODS = (
        ('POST', 'POST'),
        ('GET', 'GET'),
    )
    BODY_TYPES = (
        ('json', 'json'),
    )
    LEVELS = (
        ("重要", "重要"),
        ("一般", "一般"),
        ("轻微", "轻微"),
    )
    DEFAULT_RESPONSE_HEAD = """
    "headers":"${get_headers({'sign':'sign'})}"
    """
    DEFAULT_REQUEST_TEXT = """
    {...}
    """
    DEFAULT_RESPONSE_TEXT = """
    {"status":0,"msg":"Success"}
    """
    CASE_TYPE = (
        ("单接口", "单接口"),
        ("单接口", "流程"),
    )


    id = models.AutoField(primary_key=True)
    casename = models.CharField('用例名',max_length=50,help_text='必填')
    modular_name = models.ForeignKey('product_manage.Modular', on_delete=models.SET_NULL, null=True,
                                     verbose_name='所属项目 -> 模块',related_name="testcase")
    product_name = models.ForeignKey('product_manage.Product', on_delete=models.SET_NULL, null=True,
                                     verbose_name='所属项目') 
    case_type = models.CharField('用例类型',choices=CASE_TYPE,max_length=64,default='单接口')
    method = models.CharField(max_length=32, verbose_name='请求方式', choices=HTTP_METHODS, default='POST')
    api = models.CharField('接口路径',max_length=100,help_text='必填: e.g. /api/v1/face/boarding/push-plan')
    header = models.TextField('请求头列表', default=DEFAULT_RESPONSE_HEAD,
                            help_text='请求头,格式必须是标准的json格式!')
    certificate = models.TextField('证书',blank=True,help_text='证书字符,选填')
    body_type = models.CharField('请求体类型', max_length=20, choices=BODY_TYPES, default="json")
    body = models.TextField('请求体列表', default=DEFAULT_REQUEST_TEXT,blank=True,
                            help_text='单接口的请求体列表,  流程测试不填这项: 格式必须是标准的json格式！')
    # case_file = models.FileField('用例测试脚本',upload_to='TestCase.modular_name',blank=True,help_text='流程测试,请上传流程测试脚本！')
    file_path = models.CharField("启动脚本路径", max_length=128, help_text="流程测试时必填: e.g xx/xx/xx",blank=True)
    check_list = models.TextField('响应体检查', default=DEFAULT_RESPONSE_TEXT,
                                  help_text='响应信息,json格式')
    desc = models.TextField(verbose_name='简要描述',blank=True,help_text='选填')
    level = models.CharField(max_length=64, verbose_name="用例等级", choices=LEVELS, default="一般")
    skip = models.BooleanField("是否跳过该用例", default=False)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    def __str__(self):
        return self.casename


    class Meta:
        unique_together = ('casename', 'modular_name',)
        verbose_name = '用例管理'
        verbose_name_plural = '用例管理'

