# Generated by Django 3.1.7 on 2021-03-13 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20210313_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='responsible',
        ),
        migrations.RemoveField(
            model_name='conference',
            name='responsible',
        ),
        migrations.RemoveField(
            model_name='event',
            name='responsible',
        ),
        migrations.AddField(
            model_name='booking',
            name='assistant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_assistant', to=settings.AUTH_USER_MODEL, verbose_name='Ассистент'),
        ),
        migrations.AddField(
            model_name='booking',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='booking_owner', to='schedule.user', verbose_name='Владелец'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conference',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conference_operator', to=settings.AUTH_USER_MODEL, verbose_name='Оператор'),
        ),
        migrations.AddField(
            model_name='conference',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='conference_owner', to='schedule.user', verbose_name='Владелец'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='schedule.user', verbose_name='Владелец'),
            preserve_default=False,
        ),
    ]
