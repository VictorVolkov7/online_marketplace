# Generated by Django 3.2.23 on 2024-01-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_phone_number_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='image'),
        ),
    ]
