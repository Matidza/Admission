# Generated by Django 5.1.2 on 2024-11-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admit', '0007_alter_schoolprofile_province_and_more'),
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
            name='country',
        ),
        migrations.RemoveField(
            model_name='schoolprofile',
            name='zipcode',
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='province',
            field=models.CharField(choices=[('Limpopo', 'Limpopo'), ('Free State', 'Free State'), ('Gauteng', 'Gauteng')], max_length=20),
        ),
    ]