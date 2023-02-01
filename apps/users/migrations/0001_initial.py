import apps.users.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
            name='Admin',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('date_of_birth', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.myuser',),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('activity_type', models.CharField(max_length=255)),
                ('brand_name', models.CharField(max_length=255)),
                ('organization_form', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('inn', models.CharField(max_length=255)),
                ('isVip', models.BooleanField(default=False)),
                ('transaction_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('logo', models.ImageField(default='default.png', upload_to=apps.users.models.upload_logo)),
                ('banner', models.ImageField(default='default.png', upload_to=apps.users.models.upload_banner)),
                ('phone1', models.CharField(max_length=255)),
                ('phone2', models.CharField(blank=True, max_length=255, null=True)),
                ('phone3', models.CharField(blank=True, max_length=255, null=True)),
                ('phone4', models.CharField(blank=True, max_length=255, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube', models.CharField(blank=True, max_length=255, null=True)),
                ('telegram', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('schedule', models.CharField(max_length=255)),
                ('start', models.CharField(max_length=255)),
                ('end', models.CharField(max_length=255)),
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
                ('discount_card_number', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(default='user_default.png', upload_to='user_image')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.myuser',),
        ),
    ]
