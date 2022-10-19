# Generated by Django 4.1.2 on 2022-10-19 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('activity_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=255)),
                ('isPartner', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('brand_name', models.CharField(max_length=255)),
                ('organization_form', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('inn', models.CharField(max_length=255)),
                ('isVip', models.BooleanField(default=False)),
                ('transaction_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('activity_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activity_type.activitytype')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.myuser',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('date_of_birth', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('discount_card_number', models.CharField(blank=True, max_length=1000, null=True)),
                ('contract_offer', models.CharField(max_length=255)),
                ('following', models.ManyToManyField(blank=True, null=True, related_name='following', to='users.partner')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.myuser',),
        ),
    ]
