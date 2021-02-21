# Generated by Django 3.1.6 on 2021-02-20 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='conference',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date']},
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.SmallIntegerField(choices=[(1, 'Очень плохо'), (2, 'Плохо'), (3, 'Удовлетворительно'), (4, 'Хорошо'), (5, 'Отлично')], verbose_name='Оценка')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.event', verbose_name='Мероприятие')),
                ('staffer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.staffer', verbose_name='Ответственный сотрудник')),
            ],
        ),
    ]