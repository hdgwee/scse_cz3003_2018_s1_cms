# Generated by Django 2.1.1 on 2018-10-25 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scse_cz3003_2018_s1_cms_app', '0010_dengue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dengue',
            name='lat',
            field=models.DecimalField(decimal_places=20, max_digits=30),
        ),
        migrations.AlterField(
            model_name='dengue',
            name='lng',
            field=models.DecimalField(decimal_places=20, max_digits=30),
        ),
    ]
