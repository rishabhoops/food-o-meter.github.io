# Generated by Django 4.2 on 2023-06-01 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodOmeterApp', '0029_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItems',
        ),
    ]
