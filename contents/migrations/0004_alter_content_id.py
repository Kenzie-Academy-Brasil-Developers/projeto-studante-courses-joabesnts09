# Generated by Django 5.0.4 on 2024-05-02 01:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_alter_content_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5e1ed4d1-7ceb-45d9-9262-03ae349107c0'), editable=False, primary_key=True, serialize=False),
        ),
    ]
