# Generated by Django 2.1 on 2019-06-08 04:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_type', models.CharField(max_length=30, verbose_name='类型')),
                ('balance', models.IntegerField(verbose_name='数量')),
                ('last_balance', models.IntegerField(default=500, verbose_name='目前余额')),
                ('marks', models.CharField(max_length=200, verbose_name='备注')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='时间')),
            ],
            options={
                'verbose_name': '用户账单',
                'verbose_name_plural': '用户账单',
            },
        ),
        migrations.CreateModel(
            name='FavoriteNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite', models.IntegerField(choices=[(-1, 'None'), (0, 'False'), (1, 'True')], default=-1, verbose_name='是否收藏此节点')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '用户和分类关联表',
                'verbose_name_plural': '用户和分类关联表',
            },
        ),
        migrations.CreateModel(
            name='SignedInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(choices=[(False, '未签到'), (True, '已经签到')], verbose_name='是否签到')),
                ('date', models.CharField(max_length=30, verbose_name='签到日期')),
                ('signed_day', models.IntegerField(default=0, verbose_name='连续签到天数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='时间')),
            ],
            options={
                'verbose_name': '用户签到',
                'verbose_name_plural': '用户签到',
            },
        ),
        migrations.CreateModel(
            name='TopicVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(choices=[(-1, 'None'), (0, 'False'), (1, 'True')], default=-1, verbose_name='是否喜欢此贴')),
                ('thanks', models.IntegerField(choices=[(-1, 'None'), (0, 'False'), (1, 'True')], default=-1, verbose_name='是否感谢此贴')),
                ('favorite', models.IntegerField(choices=[(-1, 'None'), (0, 'False'), (1, 'True')], default=-1, verbose_name='是否收藏此贴')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': 'Topic和用户关联表',
                'verbose_name_plural': 'Topic和用户关联表',
            },
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='个人网站')),
                ('company', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='所在公司')),
                ('company_title', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='工作职位')),
                ('bio', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='个人简介')),
                ('balance', models.IntegerField(default=500, verbose_name='财富值，默认500')),
                ('show_balance', models.IntegerField(choices=[(0, '不展示'), (1, '展示')], default=1, verbose_name='是否显示余额')),
                ('list_rich', models.IntegerField(choices=[(0, '不展示'), (1, '展示')], default=1, verbose_name='是否参与财富榜')),
                ('my_home', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='登录后首页跳转')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.CreateModel(
            name='UserTopDu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_du', models.IntegerField(default=0, verbose_name='活跃值')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='时间')),
            ],
            options={
                'verbose_name': '用户活跃值',
                'verbose_name_plural': '用户活跃值',
            },
        ),
    ]
