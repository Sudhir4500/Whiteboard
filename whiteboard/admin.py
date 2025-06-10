# whiteboard/admin.py
from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'expires_at', 'is_expired']
    readonly_fields = ['uuid', 'created_at']
