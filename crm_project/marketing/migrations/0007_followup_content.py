# Generated by Django 3.2.5 on 2021-07-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0006_followup'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup',
            name='content',
            field=models.TextField(default=None, max_length=400, verbose_name='متن پیگیری'),
        ),
    ]
