# Generated by Django 5.0 on 2023-12-19 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0005_remove_order_cart_item_order_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='description',
        ),
        migrations.RemoveField(
            model_name='order',
            name='dish_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
    ]
