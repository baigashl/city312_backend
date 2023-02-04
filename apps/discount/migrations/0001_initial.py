# Generated by Django 4.1.2 on 2023-01-30 07:54

import apps.discount.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_type', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('price_before', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=500)),
                ('promotion_condition', models.CharField(max_length=500)),
                ('percentage', models.IntegerField(default=0)),
                ('cashback', models.IntegerField(default=0)),
                ('referral_link', models.CharField(max_length=255)),
                ('start_of_action', models.CharField(max_length=255)),
                ('end_of_action', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DiscountImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to=apps.discount.models.upload_image)),
            ],
        ),
        migrations.CreateModel(
            name='DiscountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.ManyToManyField(blank=True, null=True, to='discount.discount')),
            ],
        ),
    ]