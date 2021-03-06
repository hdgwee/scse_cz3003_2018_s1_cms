# Generated by Django 2.1.1 on 2018-09-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublicServiceAnnouncement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('reusable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='publicserviceannouncement',
            name='publish',
            field=models.ManyToManyField(blank=True, to='scse_cz3003_2018_s1_cms_app.User'),
        ),
    ]
