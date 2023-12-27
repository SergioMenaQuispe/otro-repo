# Generated by Django 4.2.7 on 2023-12-27 01:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0009_remove_task_shared_remove_task_shared_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='shared',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='shared_with',
            field=models.ManyToManyField(blank=True, related_name='shared_tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]