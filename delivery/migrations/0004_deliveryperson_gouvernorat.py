# Generated by Django 5.0.6 on 2024-07-05 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_gouvernorat_store_gouvernorat'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryperson',
            name='gouvernorat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.gouvernorat'),
        ),
    ]