# Generated by Django 5.0.4 on 2024-05-08 14:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_courses', '0008_alter_studentcourse_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a6d553ce-67fb-46b1-8f3c-93476a97ab00'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
