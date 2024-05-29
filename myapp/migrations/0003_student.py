# Generated by Django 5.0.6 on 2024-05-29 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_region_name_alter_district_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sinf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.sinf')),
            ],
        ),
    ]
