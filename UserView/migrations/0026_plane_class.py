# Generated by Django 4.2.3 on 2023-09-09 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserView', '0025_alter_packages_location_alter_packages_plane'),
    ]

    operations = [
        migrations.AddField(
            model_name='plane',
            name='Class',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
