# Generated by Django 3.2.5 on 2021-07-26 11:08

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0004_rename_client_quote_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='created_time',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد پیش فاکتور'),
        ),
    ]
