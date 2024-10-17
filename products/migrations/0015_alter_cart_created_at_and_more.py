# Generated by Django 5.0.2 on 2024-10-16 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_cart_created_at_alter_product_images_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.CharField(default='1403/07/26', max_length=1000, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='product_attributes',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='products.product', verbose_name='محصول'),
        ),
    ]
