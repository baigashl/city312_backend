# Generated by Django 4.1.2 on 2022-10-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('discount', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='discount',
            field=models.ManyToManyField(blank=True, null=True, to='discount.discount'),
        ),
    ]
