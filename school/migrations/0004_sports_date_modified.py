# Generated by Django 5.1.2 on 2025-03-06 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_school_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sports',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
