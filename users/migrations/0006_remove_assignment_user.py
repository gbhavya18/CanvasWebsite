# Generated by Django 2.1.4 on 2018-12-25 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_assignment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='user',
        ),
    ]
