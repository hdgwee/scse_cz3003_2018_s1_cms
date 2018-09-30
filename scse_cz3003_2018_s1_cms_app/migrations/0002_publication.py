# Generated by Django 2.1.1 on 2018-09-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scse_cz3003_2018_s1_cms_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_service_announcement_id', models.ForeignKey(on_delete=None, to='scse_cz3003_2018_s1_cms_app.PublicServiceAnnouncement')),
                ('social_media_id', models.ForeignKey(on_delete=None, to='scse_cz3003_2018_s1_cms_app.SocialMedia')),
                ('user_id', models.ForeignKey(on_delete=None, to='scse_cz3003_2018_s1_cms_app.User')),
            ],
        ),
    ]
