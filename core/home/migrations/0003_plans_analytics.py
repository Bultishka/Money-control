# Generated by Django 4.2.17 on 2025-01-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_transaction_analytics'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='analytics',
            field=models.BooleanField(default=True),
        ),
    ]
