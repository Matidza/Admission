# Generated by Django 5.1.2 on 2024-11-24 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(max_length=100)),
                ('schooladdress', models.TextField(default='', max_length=100)),
                ('telephone', models.CharField(blank=True, max_length=200)),
                ('address1', models.CharField(blank=True, max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('province', models.CharField(blank=True, max_length=200)),
                ('zipcode', models.CharField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('website', models.TextField(max_length=100)),
                ('image', models.ImageField(default=datetime.datetime.today, upload_to='uploads/schoolprofile/')),
            ],
            options={
                'verbose_name_plural': 'School Profile',
            },
        ),
    ]