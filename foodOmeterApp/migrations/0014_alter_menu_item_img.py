# Generated by Django 4.2 on 2023-05-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodOmeterApp', '0013_alter_menu_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='item_img',
            field=models.ImageField(upload_to='item_image/'),
        ),
    ]
