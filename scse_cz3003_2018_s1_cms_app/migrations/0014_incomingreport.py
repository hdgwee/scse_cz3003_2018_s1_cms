# Generated by Django 2.1.2 on 2018-11-14 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scse_cz3003_2018_s1_cms_app', '0013_emergencyupdates_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomingReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('U', 'Unread'), ('R', 'Read'), ('C', 'Completed')], default='U', max_length=1)),
            ],
        ),
    ]
