# Generated by Django 2.1 on 2019-06-15 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casepoint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caseideacontent',
            name='contents',
            field=models.CharField(max_length=64, verbose_name='框架内容'),
        ),
    ]
