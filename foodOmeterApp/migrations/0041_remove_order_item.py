# Generated by Django 4.2 on 2023-06-02 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodOmeterApp', '0040_alter_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
    ]