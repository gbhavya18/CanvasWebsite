# Generated by Django 2.1.4 on 2018-12-25 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20181226_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Course'),
        ),
    ]
