# whiteboard/models.py
from django.db import models
from django.utils import timezone
import uuid
from django.core.validators import MinLengthValidator

class Room(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True, 
        validators=[MinLengthValidator(1)],
        db_index=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def is_expired(self):
        return self.expires_at and timezone.now() > self.expires_at
    
    def __str__(self):
        return f"Room: {self.name}"

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['expires_at']),
        ]

class Snapshot(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='snapshots')
    created_at = models.DateTimeField(auto_now_add=True)
    image_data = models.TextField()  # For base64 string snapshot

    def __str__(self):
        return f"Snapshot for {self.room.name} at {self.created_at}"

    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
        ]