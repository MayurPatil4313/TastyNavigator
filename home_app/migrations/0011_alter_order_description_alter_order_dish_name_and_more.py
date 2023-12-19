# Generated by Django 5.0 on 2023-12-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0010_alter_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='dish_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]