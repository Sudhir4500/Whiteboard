from django.core.management.base import BaseCommand
from whiteboard.models import Room
from django.utils import timezone

class Command(BaseCommand):
    help = 'Delete expired rooms'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        expired_rooms = Room.objects.filter(expires_at__lt=now)
        count = expired_rooms.count()
        expired_rooms.delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {count} expired rooms.'))