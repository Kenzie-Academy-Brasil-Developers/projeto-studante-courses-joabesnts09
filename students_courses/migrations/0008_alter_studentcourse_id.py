# Generated by Django 5.0.4 on 2024-05-08 14:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_courses', '0007_alter_studentcourse_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8ae27177-a534-42b8-b0f8-7745a9ef251a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
