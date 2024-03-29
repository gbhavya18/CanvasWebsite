# Generated by Django 2.1.4 on 2019-01-11 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0040_auto_20190111_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradeassignments',
            name='assignment',
        ),
        migrations.AddField(
            model_name='gradeassignments',
            name='assignment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Assignment'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='gradeassignments',
            name='course',
        ),
        migrations.AddField(
            model_name='gradeassignments',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Course'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='gradeassignments',
            name='user',
        ),
        migrations.AddField(
            model_name='gradeassignments',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
