# Generated by Django 2.1.2 on 2018-10-06 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrisisLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='IncidentReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mobile_number', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
                ('date_time', models.DateTimeField()),
                ('postal_code', models.CharField(max_length=128)),
                ('unit_number', models.CharField(max_length=128)),
                ('street', models.CharField(max_length=128)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('crisis_level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.CrisisLevel')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='StatusReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField()),
                ('incident_report', models.ManyToManyField(to='reports.IncidentReport')),
            ],
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.Source'),
        ),
    ]
