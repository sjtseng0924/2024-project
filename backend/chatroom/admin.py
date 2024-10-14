from django.contrib import admin
from .models import ChatRoom, Message, UserSession
# Register your models here.

admin.site.register(ChatRoom)
admin.site.register(Message)
admin.site.register(UserSession)