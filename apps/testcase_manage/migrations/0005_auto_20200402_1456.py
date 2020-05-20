# Generated by Django 2.0 on 2020-04-02 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_manage', '0004_auto_20200402_1456'),
        ('testcase_manage', '0004_auto_20200402_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='product_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_manage.Product', verbose_name='所属项目'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='body',
            field=models.TextField(blank=True, default='---\ndata: {}\n    ', help_text='单接口的请求体列表,流程测试不填这项！', verbose_name='请求体列表'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='case_file',
            field=models.FileField(blank=True, help_text='流程测试,请上传流程测试脚本！', upload_to='testCase', verbose_name='用例测试脚本'),
        ),
        migrations.AlterUniqueTogether(
            name='testcase',
            unique_together={('casename', 'modular_name')},
        ),
    ]