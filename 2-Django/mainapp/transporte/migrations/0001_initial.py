# Generated by Django 4.1.2 on 2022-10-18 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreChofer', models.CharField(max_length=255)),
                ('domicilioChofer', models.CharField(max_length=255)),
                ('edadChofer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCiudad', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreRuta', models.CharField(max_length=255)),
                ('distanciaRuta', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaViaje', models.DateField()),
                ('observaciones', models.CharField(max_length=255)),
                ('chofer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transporte.chofer')),
                ('ruta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transporte.ruta')),
            ],
        ),
        migrations.AddField(
            model_name='chofer',
            name='ciudadNacimiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transporte.ciudad'),
        ),
    ]
