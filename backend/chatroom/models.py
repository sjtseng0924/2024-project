from djongo import models
from django.utils import timezone

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"

class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sender_name}: {self.content}"

class UserSession(models.Model):
    uuid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    joined_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
