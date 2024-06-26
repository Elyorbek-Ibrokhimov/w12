# Generated by Django 5.0.6 on 2024-05-29 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maktab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(default='maktab', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sinf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(default='sinf', max_length=100)),
                ('maktab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maktablar', to='students.maktab')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(default='student', max_length=100)),
                ('sinf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='students.sinf')),
            ],
        ),
    ]
