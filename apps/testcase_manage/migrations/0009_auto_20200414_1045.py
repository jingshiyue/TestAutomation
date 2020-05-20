# Generated by Django 2.0 on 2020-04-14 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testcase_manage', '0008_testcase_certificate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcase',
            old_name='url',
            new_name='api',
        ),
        migrations.AlterField(
            model_name='testcase',
            name='file_path',
            field=models.CharField(blank=True, help_text='流程测试时必填: e.g xx/xx/xx', max_length=128, verbose_name='启动脚本路径'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='modular_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='testcase', to='product_manage.Modular', verbose_name='所属项目 -> 模块'),
        ),
    ]
