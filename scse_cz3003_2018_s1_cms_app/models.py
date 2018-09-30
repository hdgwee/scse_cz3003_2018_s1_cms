from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class PublicServiceAnnouncement(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    reusable = models.BooleanField(default=False)


class SocialMedia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)


class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=None)
    public_service_announcement_id = models.ForeignKey(PublicServiceAnnouncement, on_delete=None)
    social_media_id = models.ForeignKey(SocialMedia, on_delete=None)
