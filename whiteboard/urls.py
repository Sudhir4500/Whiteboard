# whiteboard/urls.py
from django.urls import path
from . import views

app_name = "whiteboard"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("new/", views.create_temp_room, name="create_temp_room"),
    path("<str:room_name>/", views.join_room, name="room"),
    path("save_snapshot/<str:room_name>/", views.save_snapshot, name="save_snapshot"),
    path("get_latest_snapshot/<str:room_name>/", views.get_latest_snapshot, name="get_latest_snapshot"),
]