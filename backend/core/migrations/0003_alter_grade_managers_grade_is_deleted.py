# Generated by Django 5.1.6 on 2025-02-13 14:19

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_student_managers_student_is_deleted'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='grade',
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
