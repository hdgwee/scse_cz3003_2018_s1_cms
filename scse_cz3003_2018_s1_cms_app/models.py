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


#Start of incident report models
class CrisisLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)


class Source(models.Model):
    # source will refer to the phone operator
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)


class IncidentReport(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    mobile_number = models.IntegerField()
    description = models.CharField(max_length=128)
    date_time = models.DateTimeField()
    postal_code = models.CharField(max_length=128)
    unit_number = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    # to consider changing to cascade
    crisis_level = models.ForeignKey(CrisisLevel, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    validated = models.CharField(default='unseen', max_length=128)

class StatusReport(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    incident_report = models.ManyToManyField(IncidentReport)
