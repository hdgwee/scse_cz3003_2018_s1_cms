from django.contrib import admin

from .models import User
from .models import PublicServiceAnnouncement
from .models import SocialMedia


@admin.register(PublicServiceAnnouncement)
class PublicServiceAnnouncement(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'reusable']