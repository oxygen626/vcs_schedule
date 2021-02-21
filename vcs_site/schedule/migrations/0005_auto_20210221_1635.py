# Generated by Django 3.1.6 on 2021-02-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20210221_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffer',
            name='subscribe_mail',
            field=models.BooleanField(default=False, verbose_name='Подписка на почтовую рассылку'),
        ),
        migrations.AddField(
            model_name='staffer',
            name='subscribe_telegram',
            field=models.BooleanField(default=False, verbose_name='Подписка на рассылку в телеграм'),
        ),
        migrations.AddField(
            model_name='staffer',
            name='telegram',
            field=models.PositiveIntegerField(default=1, verbose_name='Телеграм чат-id'),
            preserve_default=False,
        ),
    ]
