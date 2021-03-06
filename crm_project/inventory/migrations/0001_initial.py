# Generated by Django 3.2.5 on 2021-07-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0002_alter_organization_manufacturedـproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام محصول')),
                ('is_taxation', models.BooleanField(default=True, verbose_name='آیا مشمول مالیات است؟')),
                ('image_catalog', models.ImageField(blank=True, upload_to='media/catalog/pictures', verbose_name='عکس کاتالوگ')),
                ('pdf_catalog', models.FileField(blank=True, upload_to='media/catalog/pdfs', verbose_name='پی دی اف کاتالوگ')),
                ('price', models.FloatField(default=0.0, verbose_name='قیمت')),
                ('technical_features', models.TextField(max_length=300, verbose_name='ویژگی های فنی')),
                ('related_with_manufacturedـproducts', models.ManyToManyField(to='organization.OrganizationProduct', verbose_name='قابل استفاده برای تولید محصولات تولیدی')),
            ],
        ),
    ]
