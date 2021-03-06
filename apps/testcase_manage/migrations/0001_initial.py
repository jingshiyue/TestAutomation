# Generated by Django 2.0 on 2020-04-01 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_manage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('casename', models.CharField(max_length=50, verbose_name='用例名')),
                ('method', models.CharField(choices=[('POST', 'POST')], default='POST', max_length=32, verbose_name='请求方式')),
                ('body_type', models.CharField(choices=[('json', 'json')], default='json', max_length=20, verbose_name='请求体类型')),
                ('url', models.URLField(verbose_name='url')),
                ('body', models.TextField(default='---\ndata: {}\n    ', help_text='以yaml格式输入请求信息', verbose_name='请求体列表')),
                ('res_code', models.CharField(default='200', help_text='例如200.201多个响应码以.分割', max_length=128, verbose_name='响应码列表')),
                ('check_list', models.TextField(default='---\n- code: 200\n    ', help_text='以yaml格式输入响应信息', verbose_name='响应体检查')),
                ('desc', models.CharField(max_length=255, verbose_name='用例简要描述')),
                ('level', models.CharField(choices=[('重要', '重要'), ('一般', '一般'), ('轻微', '轻微')], default='一般', max_length=64, verbose_name='用例等级')),
                ('skip', models.BooleanField(default=False, verbose_name='是否跳过该用例')),
                ('modular_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_manage.Modular', verbose_name='所属项目')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '用例管理',
                'verbose_name_plural': '用例管理',
            },
        ),
    ]
