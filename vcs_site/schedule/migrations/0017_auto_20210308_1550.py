# Generated by Django 3.1.6 on 2021-03-08 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0016_auto_20210308_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Файл'),
        ),
    ]
