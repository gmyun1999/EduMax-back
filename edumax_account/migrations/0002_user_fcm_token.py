# Generated by Django 4.2.11 on 2024-05-02 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edumax_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fcm_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
