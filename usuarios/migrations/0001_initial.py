# Generated by Django 5.1.1 on 2024-09-19 17:37

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_aluno', models.CharField(max_length=200)),
                ('item', models.CharField(max_length=200, verbose_name=django.contrib.auth.models.User)),
            ],
        ),
    ]
