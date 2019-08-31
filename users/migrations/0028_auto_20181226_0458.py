# Generated by Django 2.1.4 on 2018-12-25 23:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0027_auto_20181226_0331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='user',
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ManyToManyField(related_name='course_user_connect', to=settings.AUTH_USER_MODEL),
        ),
    ]