# Generated by Django 5.1.2 on 2024-11-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admit', '0005_schoolprofile_image1_schoolprofile_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='province',
            field=models.CharField(choices=[('Limpopo', 'Limpopo'), ('Free State', 'Free State'), ('Gauteng', 'Gauteng')], max_length=20),
        ),
    ]