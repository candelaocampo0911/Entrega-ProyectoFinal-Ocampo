# Generated by Django 4.1.5 on 2023-01-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_de_articulo', models.CharField(max_length=256)),
                ('marca', models.CharField(max_length=256)),
                ('peso', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=256)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Medio_pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medio_de_pago', models.CharField(max_length=256)),
            ],
        ),
    ]
