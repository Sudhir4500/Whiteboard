# whiteboard/management/commands/cleanup_expired.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from whiteboard.models import Room

class Command(BaseCommand):
    help = "Delete expired rooms and their snapshots"

    def handle(self, *args, **kwargs):
        expired_rooms = Room.objects.filter(expires_at__lt=timezone.now())
        count = expired_rooms.count()
        expired_rooms.delete()
        self.stdout.write(f"Deleted {count} expired rooms and their snapshots.")
