# Generated by Django 4.2.7 on 2024-01-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_Name', models.CharField(max_length=40)),
                ('T_Email', models.CharField(max_length=30)),
            ],
        ),
    ]