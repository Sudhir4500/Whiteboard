# whiteboard/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import logging
from channels.db import database_sync_to_async

logger = logging.getLogger(__name__)

class WhiteboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'whiteboard_{self.room_name}'

        # Validate room existence
        if not await self.room_exists():
            await self.close(code=4001)
            return

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        logger.info(f"Connected to room: {self.room_group_name}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        logger.info(f"Disconnected from room: {self.room_group_name} (code: {close_code})")

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            event_type = data.get("type")
        except json.JSONDecodeError:
            logger.error("Invalid JSON received")
            return

        if event_type in ["draw_event", "clear_canvas", "full_canvas"]:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "broadcast_event",
                    "payload": data
                }
            )
            logger.debug(f"Broadcasting {event_type}: {data}")
        else:
            logger.warning(f"Unknown event type received: {event_type}")

    async def broadcast_event(self, event):
        await self.send(text_data=json.dumps(event["payload"]))

    @database_sync_to_async
    def room_exists(self):
        from .models import Room  # ✅ moved here
        try:
            room = Room.objects.get(name=self.room_name)
            return not room.is_expired()
        except Room.DoesNotExist:
            return False
