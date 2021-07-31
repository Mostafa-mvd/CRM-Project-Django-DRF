# Generated by Django 3.2.5 on 2021-07-30 16:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_companyproduct_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyproduct',
            name='pdf_catalog',
            field=models.FileField(blank=True, upload_to='media/catalogs/pdfs', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='پی دی اف کاتالوگ'),
        ),
    ]
