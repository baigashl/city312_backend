# Generated by Django 4.1.2 on 2023-01-12 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_discount_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='discount_card_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
