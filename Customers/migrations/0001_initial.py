# Generated by Django 4.1 on 2022-10-15 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('full_name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
