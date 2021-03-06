# Generated by Django 2.1.2 on 2018-11-13 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scse_cz3003_2018_s1_cms_app', '0011_auto_20181025_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyUpdates',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField()),
                ('incident_report', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scse_cz3003_2018_s1_cms_app.IncidentReport')),
            ],
        ),
    ]
