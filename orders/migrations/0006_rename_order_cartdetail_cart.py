# Generated by Django 3.2 on 2023-03-10 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20230310_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdetail',
            old_name='order',
            new_name='cart',
        ),
    ]
