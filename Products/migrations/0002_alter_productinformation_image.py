# Generated by Django 4.1 on 2022-10-27 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinformation',
            name='image',
            field=models.ImageField(null=True, upload_to='prod-images/'),
        ),
    ]
