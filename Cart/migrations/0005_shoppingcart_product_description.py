# Generated by Django 4.1 on 2022-10-24 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0004_shoppingcart_product_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='product_description',
            field=models.TextField(null=True),
        ),
    ]
