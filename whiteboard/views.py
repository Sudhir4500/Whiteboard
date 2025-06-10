# whiteboard/views.py
import json
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
import uuid
from .models import Room, Snapshot

def homepage(request):
    if request.method == "POST":
        room_name = request.POST.get("room_name", "").strip()
        if not room_name:
            return render(request, "whiteboard/homepage.html", {"error": "Please enter a room name."})
        if len(room_name) > 100:
            return render(request, "whiteboard/homepage.html", {"error": "Room name too long (max 100 characters)."})
        return redirect(reverse("whiteboard:room", args=[room_name]))
    return render(request, "whiteboard/homepage.html")

def create_temp_room(request):
    unique_name = str(uuid.uuid4())[:8]
    expires_at = timezone.now() + timedelta(hours=24)
    try:
        room = Room.objects.create(name=unique_name, expires_at=expires_at)
        return redirect('whiteboard:room', room_name=room.name)
    except Exception as e:
        return render(request, "whiteboard/homepage.html", {"error": "Failed to create room."})

def join_room(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    if room.is_expired():
        return render(request, "whiteboard/expired.html", {"room_name": room.name})
    return render(request, "whiteboard/room.html", {"room_name": room.name})

@csrf_exempt
def save_snapshot(request, room_name):
    if request.method != "POST":
        return JsonResponse({"error": "POST method required"}, status=405)
    
    try:
        room = Room.objects.get(name=room_name)
    except Room.DoesNotExist:
        return JsonResponse({"error": "Room not found"}, status=404)

    try:
        data = json.loads(request.body)
        image_data = data.get("image_data")
        if not image_data:
            return JsonResponse({"error": "No image data provided"}, status=400)
        
        Snapshot.objects.create(room=room, image_data=image_data)
        return JsonResponse({"status": "snapshot saved"})
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)
    except Exception as e:
        return JsonResponse({"error": "Server error"}, status=500)

def get_latest_snapshot(request, room_name):
    try:
        room = Room.objects.get(name=room_name)
        snapshot = room.snapshots.order_by('-created_at').first()
        return JsonResponse({"image_data": snapshot.image_data if snapshot else None})
    except Room.DoesNotExist:
        return JsonResponse({"error": "Room not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": "Server error"}, status=500)