# Generated by Django 4.2.1 on 2023-05-28 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_created_at_product_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/product_images/'),
        ),
    ]
