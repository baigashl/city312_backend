# Generated by Django 4.1.2 on 2022-10-15 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_partner_customuser_following'),
        ('discount', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='partner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.partner'),
        ),
    ]
