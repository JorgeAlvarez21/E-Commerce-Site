# Generated by Django 4.1 on 2022-10-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='product_image',
            field=models.ImageField(null=True, upload_to='prod-images-cart/'),
        ),
    ]
