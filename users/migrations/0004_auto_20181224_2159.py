# Generated by Django 2.1.4 on 2018-12-24 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Course'),
        ),
    ]
