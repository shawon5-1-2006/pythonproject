# Generated by Django 4.2.7 on 2024-01-03 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('potfolio', '0003_about_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='name',
            new_name='u_name',
        ),
    ]