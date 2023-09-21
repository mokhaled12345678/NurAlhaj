# Generated by Django 4.2.3 on 2023-08-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploaded-images/packages')),
                ('location', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('last_price', models.FloatField()),
            ],
        ),
    ]