# Generated by Django 4.2 on 2023-05-30 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodOmeterApp', '0015_alter_menu_item_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='forget_password_token',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
