# Generated by Django 4.2.7 on 2024-02-17 16:12

import django.core.validators
from django.db import migrations, models
import edumax_account.model.model_manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemporaryKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('key', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PwChangeTemporaryQueryParam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('query_param', models.CharField(max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('login_id', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='ID는 알파벳 대소문자나 숫자만을 포함하는 4~16자의 문자열이어야 합니다.', regex='^[a-zA-Z0-9]{4,16}$')])),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('nickname', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='닉네임은 영문, 숫자, 한글로 이루어진 2~10자의 문자열이어야 합니다.', regex='^[a-zA-Z0-9가-힣]{2,10}$')])),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', edumax_account.model.model_manager.UserManager()),
            ],
        ),
    ]