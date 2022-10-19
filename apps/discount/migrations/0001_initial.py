# Generated by Django 4.1.2 on 2022-10-19 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activity_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contacts', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('inn', models.CharField(max_length=255)),
                ('isVip', models.CharField(max_length=255)),
                ('transaction_quantity', models.CharField(max_length=255)),
                ('isPartner', models.CharField(max_length=255)),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activity_type.category')),
                ('discount_type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='discount.discounttype')),
            ],
        ),
    ]
