# Generated by Django 5.1.2 on 2024-12-12 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_schoolprofile_type_of_school_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolprofile',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='schoolprofile',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='schoolprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='schoolprofile',
            name='zipcode',
        ),
    ]