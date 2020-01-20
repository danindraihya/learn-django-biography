from django.contrib import admin
from .models import Biography

class AdminBiography(admin.ModelAdmin):
    readonly_fields = [
        'slug'
    ]

admin.site.register(Biography, AdminBiography)