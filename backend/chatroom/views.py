from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ChatRoom, Message, UserSession
from django.utils.crypto import get_random_string

# 加入聊天室
def join_room(request, room_name):
    if request.method == 'POST':
        name = request.POST.get('name')
        if not name:
            return JsonResponse({"error": "Name is required"}, status=400)

        uuid = get_random_string(32)  # 生成唯一的 UUID
        UserSession.objects.create(uuid=uuid, name=name)

        return redirect('chatroom', room_name=room_name)
    
    # 如果是 GET 請求，渲染一個輸入用戶名的頁面
    return render(request, 'chatroom/join_room.html', {'room_name': room_name})

# 發送訊息
def send_message(request, room_name):
    if request.method == 'POST':
        content = request.POST.get('message')
        uuid = request.POST.get('uuid')
        user = UserSession.objects.filter(uuid=uuid).first()
        chatroom = ChatRoom.objects.filter(name=room_name).first()

        if user and chatroom:
            Message.objects.create(chatroom=chatroom, sender_name=user.name, content=content)
            return JsonResponse({"status": "Message sent"})
        return JsonResponse({"error": "Invalid session or room"}, status=400)

# 顯示聊天室頁面
def chatroom_view(request, room_name):
    return render(request, 'chatroom/chatroom.html', {'room_name': room_name})