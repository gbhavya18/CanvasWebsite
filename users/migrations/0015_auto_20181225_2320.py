# Generated by Django 2.1.4 on 2018-12-25 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20181225_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
