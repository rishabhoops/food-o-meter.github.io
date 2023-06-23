# Generated by Django 4.2 on 2023-06-01 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodOmeterApp', '0035_remove_cartitems_cart_remove_cartitems_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='foodOmeterApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('t_price', models.IntegerField(blank=True, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='foodOmeterApp.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodOmeterApp.menu')),
            ],
        ),
    ]
