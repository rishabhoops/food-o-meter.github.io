# Generated by Django 4.2 on 2023-06-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodOmeterApp', '0042_order_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='instamojo_response',
            field=models.TextField(blank=True, null=True),
        ),
    ]
