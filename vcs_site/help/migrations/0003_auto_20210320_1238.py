# Generated by Django 3.1.7 on 2021-03-20 09:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0002_page_urls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='update_date',
        ),
        migrations.AddField(
            model_name='page',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='section',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='urls',
            field=models.TextField(blank=True, help_text='Перечислите url-адреса страниц на которых будет автоматически отображатся эта страница помощи. Например: "/schedule/event-create/;" или "/schedule/event/*.*/conference-create/; /schedule/conference-approve/*.*/;", где ";" - конец адреса.', null=True, verbose_name='Страницы для автоматического вывода'),
        ),
    ]
