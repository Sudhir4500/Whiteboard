from django.urls import path
from . import views  # Adjust if views are in a different file

urlpatterns = [
    path("whiteboard/<str:room_name>/", views.whiteboard_room, name="whiteboard_room"),
]
