# Generated by Django 5.0.4 on 2024-05-02 13:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b35e1a71-c4f6-4052-8af9-a17a9f9ab677'), editable=False, primary_key=True, serialize=False),
        ),
    ]
