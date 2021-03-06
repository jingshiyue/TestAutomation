# Generated by Django 2.0 on 2020-04-01 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='角色名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱地址')),
                ('desc', models.TextField(blank=True, verbose_name='描述')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '邮件抄送人',
                'verbose_name_plural': '邮件抄送人',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='notifier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='product_manage.Notifier', verbose_name='邮件抄送人'),
        ),
    ]
