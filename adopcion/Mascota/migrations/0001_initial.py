# Generated by Django 5.2 on 2025-06-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('especie', models.CharField(max_length=50)),
                ('edad', models.CharField(max_length=50)),
                ('estado', models.TextField()),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
