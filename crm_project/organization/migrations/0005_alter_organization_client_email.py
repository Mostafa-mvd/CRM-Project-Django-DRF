# Generated by Django 3.2.5 on 2021-07-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20210724_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='client_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='ایمیل'),
        ),
    ]
