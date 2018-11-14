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


# Start of incident report models
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


class IncomingReport(models.Model):
    STATUS_CHOICES = [('U', 'Unread'), ('R', 'Read'), ('C', 'Completed')]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    updated = models.DateTimeField(blank=True, auto_now = True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='U')


class EmergencyUpdates(models.Model):
    id = models.AutoField(primary_key=True)
    incident_report = models.ForeignKey(IncidentReport, on_delete=models.PROTECT)
    description = models.CharField(max_length=128, default='Nil')
    date_time = models.DateTimeField()


class StatusReport(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    incident_report = models.ManyToManyField(IncidentReport)


class PsiType(models.Model):
    id = models.AutoField(primary_key=True)
    human_readable_name = models.CharField(max_length=128)
    machine_readable_name = models.CharField(max_length=128)


class Psi(models.Model):
    id = models.AutoField(primary_key=True)
    national = models.DecimalField(default=0, max_digits=8, decimal_places=6)
    north = models.DecimalField(default=0, max_digits=8, decimal_places=6)
    south = models.DecimalField(default=0, max_digits=8, decimal_places=6)
    east = models.DecimalField(default=0, max_digits=8, decimal_places=6)
    west = models.DecimalField(default=0, max_digits=8, decimal_places=6)
    central = models.DecimalField(default=0, max_digits=8, decimal_places=6)
    type = models.ForeignKey(PsiType, on_delete=models.PROTECT)
    date_time = models.DateTimeField()


class Dengue(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    lat = models.DecimalField(max_digits=30, decimal_places=20)
    lng = models.DecimalField(max_digits=30, decimal_places=20)
