# Generated by Django 3.2.5 on 2021-07-25 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0010_alter_organization_owner_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='expert_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='کارشناس ایجاد کننده'),
        ),
    ]