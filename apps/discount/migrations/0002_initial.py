# Generated by Django 4.1.2 on 2023-01-30 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('discount', '0001_initial'),
        ('activity_type', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='discountimage',
            name='discount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='discount.discount'),
        ),
        migrations.AddField(
            model_name='discount',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='activity_type.category'),
        ),
        migrations.AddField(
            model_name='discount',
            name='partner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.partner'),
        ),
    ]
