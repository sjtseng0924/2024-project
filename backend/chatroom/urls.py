from django.urls import path
from . import views

urlpatterns = [
    path('create/<str:room_name>/', views.create_room, name='create_room'),
    path('newuser/<str:user_name>/', views.new_user, name='new_user'),
    path('send/<str:room_name>/', views.send_message, name='send_message'),
    path('messages/<str:room_name>/', views.get_allmessage, name='get_allmessage'),
    path('messages/<str:room_name>/<str:user_name>/', views.get_messages, name='get_messages'),
]
