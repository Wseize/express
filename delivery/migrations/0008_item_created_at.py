# Generated by Django 5.0.6 on 2024-07-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_item_percentage_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]