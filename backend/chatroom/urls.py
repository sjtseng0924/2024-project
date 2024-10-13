from django.urls import path
from . import views

urlpatterns = [
    path('join/<str:room_name>/', views.join_room, name='join_room'),
    path('send/<str:room_name>/', views.send_message, name='send_message'),
    path('room/<str:room_name>/', views.chatroom_view, name='chatroom'),
]
