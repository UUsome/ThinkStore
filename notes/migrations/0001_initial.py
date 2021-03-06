# Generated by Django 2.1 on 2019-06-10 16:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes_sn', models.CharField(max_length=20, unique=True, verbose_name='Note唯一sn')),
                ('content', models.TextField(blank=True, max_length=200000, null=True, verbose_name='Note正文')),
                ('notes_type', models.IntegerField(choices=[(0, 'Default'), (1, 'Markdown')], help_text='Note正文类型', verbose_name='Note正文类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Note作者')),
            ],
            options={
                'verbose_name': 'Notes',
                'verbose_name_plural': 'Notes',
            },
        ),
        migrations.CreateModel(
            name='NotesFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', help_text='文件夹标题', max_length=30, verbose_name='文件夹标题')),
                ('url', models.CharField(default='', help_text='文件夹URL', max_length=30, unique=True, verbose_name='文件夹URL')),
                ('desc', models.TextField(blank=True, help_text='文件夹名称描述', null=True, verbose_name='文件夹名称描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': 'Notes 目录',
                'verbose_name_plural': 'Notes 目录',
            },
        ),
        migrations.AddField(
            model_name='notes',
            name='folder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='notes.NotesFolder', verbose_name='所在目录'),
        ),
    ]
