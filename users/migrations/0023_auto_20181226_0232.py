# Generated by Django 2.1.4 on 2018-12-25 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_course_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
