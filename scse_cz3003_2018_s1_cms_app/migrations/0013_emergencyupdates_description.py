# Generated by Django 2.1.2 on 2018-11-13 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scse_cz3003_2018_s1_cms_app', '0012_emergencyupdates'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencyupdates',
            name='description',
            field=models.CharField(default='Nil', max_length=128),
        ),
    ]