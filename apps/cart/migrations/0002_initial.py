# Generated by Django 4.1.2 on 2023-01-18 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='discount',
            field=models.ManyToManyField(blank=True, null=True, to='discount.discount'),
        ),
    ]
