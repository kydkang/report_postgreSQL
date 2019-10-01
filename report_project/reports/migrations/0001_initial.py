# Generated by Django 2.2.6 on 2019-10-01 20:59

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dmeva_code', models.CharField(max_length=20)),
                ('dmeva_fecha', models.DateField()),
                ('grafico', models.ImageField(blank=True, upload_to='grafico/', verbose_name='Superficie Grafico')),
                ('mapa', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, srid=4326, verbose_name='Mapa de Ubicación')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_code', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Localización Código')),
                ('province', models.CharField(max_length=50)),
                ('canton', models.CharField(max_length=50)),
                ('parroquia', models.CharField(max_length=50)),
                ('parroquia_mapa', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, srid=4326, verbose_name='Parroquia Mapa')),
            ],
        ),
        migrations.CreateModel(
            name='SatImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuente', models.CharField(max_length=50)),
                ('banda', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('image', models.ImageField(upload_to='satimages', verbose_name='Imagen')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Event', verbose_name='Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informe_code', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('fecha', models.DateField()),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reports.Event')),
                ('satimage1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='informe1', to='reports.SatImage', verbose_name='Imagen Satelital 1')),
                ('satimage2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='informe2', to='reports.SatImage', verbose_name='Imagen Satelital 2')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superficie', models.DecimalField(decimal_places=2, max_digits=8)),
                ('hectarea', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Hectáreas')),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Porcentaje')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Event', verbose_name='Evento')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Location', verbose_name='Localización')),
            ],
        ),
    ]
