# Generated by Django 3.2.5 on 2021-07-24 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20210724_1205'),
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuoteItems',
            new_name='QuoteItem',
        ),
    ]
