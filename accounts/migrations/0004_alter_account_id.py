# Generated by Django 5.0.4 on 2024-05-02 01:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1b548ed0-3663-4f4f-85c6-0f3fafd9d9fb'), editable=False, primary_key=True, serialize=False),
        ),
    ]
