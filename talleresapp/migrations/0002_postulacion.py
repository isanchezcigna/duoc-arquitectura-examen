# Generated by Django 4.0.5 on 2022-12-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talleresapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postulacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('rut', models.CharField(max_length=15)),
                ('fecha_nac', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=12)),
                ('descripcion', models.CharField(max_length=200)),
                ('requiere_material', models.BooleanField()),
                ('requiere_lugar', models.BooleanField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('desc_habilidades', models.CharField(max_length=255)),
                ('arch_habilidades', models.FileField(upload_to='')),
                ('estado', models.IntegerField(choices=[(0, 'Generado'), (1, 'Asignado'), (2, 'Aprobado'), (3, 'Rechazado'), (4, 'Falta Info'), (5, 'Anulado')], default=0)),
            ],
            options={
                'verbose_name': 'Postulacion',
                'verbose_name_plural': 'Postulaciones',
                'db_table': 'postulacion',
                'ordering': ['id'],
            },
        ),
    ]