# Generated by Django 2.1.4 on 2018-12-25 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20181225_2104'),
        ('dashboard', '0008_course_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='user',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]