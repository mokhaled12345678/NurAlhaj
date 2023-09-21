# Generated by Django 4.2.3 on 2023-09-08 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserView', '0022_packages_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Air Plane Name', max_length=50)),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
        migrations.AddField(
            model_name='packages',
            name='plane',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserView.plane'),
        ),
    ]
