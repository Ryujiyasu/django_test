# Generated by Django 3.0.8 on 2020-07-22 04:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_auto_20200722_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 4, 32, 16, 993500, tzinfo=utc), verbose_name='入室日時'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='exit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='退室日時'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 4, 32, 16, 993770, tzinfo=utc), verbose_name='更新時間'),
        ),
    ]
