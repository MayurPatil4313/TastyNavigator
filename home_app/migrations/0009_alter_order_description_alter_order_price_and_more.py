# Generated by Django 5.0 on 2023-12-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0008_alter_order_dish_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
