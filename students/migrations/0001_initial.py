# Generated by Django 4.1.7 on 2023-03-25 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('fn', models.DateField()),
                ('sex', models.CharField(choices=[('N/A', 'N/A'), ('M', 'Masculino'), ('F', 'Femenino')], max_length=3)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Estudent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('fn', models.DateField()),
                ('sex', models.CharField(choices=[('N/A', 'N/A'), ('M', 'Masculino'), ('F', 'Femenino')], max_length=3)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('kinship', models.CharField(choices=[('N/A', 'N/A'), ('MADRE', 'MADRE'), ('PADRE', 'PADRE'), ('MADRASTRA', 'MADRASTRA'), ('PADRASTRO', 'PADRASTRO'), ('REPRESENTANTE LOPNNA', 'REPRESENTANTE LOPNNA')], max_length=30)),
                ('representative', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='students.representative')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
