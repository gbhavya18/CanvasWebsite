# Generated by Django 2.1.4 on 2018-12-22 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='author',
            new_name='user',
        ),
    ]
