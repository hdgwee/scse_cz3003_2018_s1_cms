# Generated by Django 2.1.1 on 2018-10-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scse_cz3003_2018_s1_cms_app', '0009_auto_20181025_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dengue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField()),
                ('lat', models.DecimalField(decimal_places=12, max_digits=20)),
                ('lng', models.DecimalField(decimal_places=12, max_digits=20)),
            ],
        ),
    ]
