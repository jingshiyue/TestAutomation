# Generated by Django 2.0 on 2020-04-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcase_manage', '0006_auto_20200403_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='header',
            field=models.TextField(default='\n    "headers":"${get_headers({\'sign\':\'sign\'})}"\n    ', help_text='请求头,格式必须是标准的json格式!', verbose_name='请求头列表'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='body',
            field=models.TextField(blank=True, default='\n    {...}\n    ', help_text='单接口的请求体列表,  流程测试不填这项: 格式必须是标准的json格式！', verbose_name='请求体列表'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='check_list',
            field=models.TextField(default='\n    {"status":0,"msg":"Success"}\n    ', help_text='响应信息,json格式', verbose_name='响应体检查'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='desc',
            field=models.TextField(blank=True, help_text='选填', verbose_name='简要描述'),
        ),
    ]