# Generated by Django 2.1.1 on 2018-10-01 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scse_cz3003_2018_s1_cms_app', '0003_auto_20180927_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='public_service_announcement_id',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='social_media_id',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]