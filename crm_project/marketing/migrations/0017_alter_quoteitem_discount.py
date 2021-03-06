# Generated by Django 3.2.5 on 2021-08-02 14:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0016_quote_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteitem',
            name='discount',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(limit_value=0, message="discount can't be negative"), django.core.validators.MaxValueValidator(limit_value=100, message="discount can't be more than 100")], verbose_name='درصد تخفیف'),
        ),
    ]
