import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ChatRoom, Message, UserSession
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create room
@csrf_exempt
def create_room(request, room_name):
    if request.method == 'POST':
        try:
            if room_name:
                ChatRoom.objects.create(name=room_name, created_at=timezone.now())
                return JsonResponse({"status": "Room created"})
            else:
                return JsonResponse({"status": "Room name is required"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"status": "Invalid JSON"}, status=400)
    

# New user
@csrf_exempt
def new_user(request, user_name):
    if request.method == 'POST':
        try:
            exist_users = UserSession.objects.all()
            if any(user.name == user_name for user in exist_users):
                return JsonResponse({"status": "User already exists"}, status=400)
            
            uuid = get_random_string(32)
            UserSession.objects.create(uuid=uuid, name=user_name)
            return JsonResponse({"status": "User created", "uuid": uuid})

        except json.JSONDecodeError:
            return JsonResponse({"status": "Invalid JSON"}, status=400)

# Send messages
@csrf_exempt
def send_message(request, room_name):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            content = data.get('message')
            user_name = data.get('name')
            chatroom = ChatRoom.objects.filter(name=room_name).first()

            if user_name and chatroom:
                Message.objects.create(chatroom=chatroom, sender_name=user_name, content=content)
                return JsonResponse({"status": "Message sent"})
            return JsonResponse({"error": "Invalid user or room"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"status": "Invalid JSON"}, status=400)

# Get all messages
def get_allmessage(request, room_name):
    if request.method == 'GET':
        chatroom = ChatRoom.objects.filter(name=room_name).first()
        if chatroom:
            messages = Message.objects.filter(chatroom=chatroom)
            return JsonResponse({"messages": [{"sender_name": message.sender_name, "content": message.content, "time": message.timestamp} for message in messages]})
        return JsonResponse({"error": "Room not found"}, status=404)

def get_messages(request, room_name, user_name):
    if request.method == 'GET':
        chatroom = ChatRoom.objects.filter(name=room_name).first()
        if chatroom:
            messages = Message.objects.filter(chatroom=chatroom, sender_name=user_name)
            return JsonResponse({"messages": [{"content": message.content, "time": message.timestamp} for message in messages]})
        return JsonResponse({"error": "Room not found"}, status=404)

