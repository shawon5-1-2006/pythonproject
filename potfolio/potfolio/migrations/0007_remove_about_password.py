# Generated by Django 4.2.7 on 2024-01-27 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('potfolio', '0006_about_password_alter_about_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='password',
        ),
    ]
