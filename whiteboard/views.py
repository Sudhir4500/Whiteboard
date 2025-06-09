from django.shortcuts import render

def whiteboard_room(request, room_name):
    return render(request, "whiteboard/room.html", {"room_name": room_name})
