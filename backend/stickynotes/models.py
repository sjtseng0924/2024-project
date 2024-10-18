from djongo import models
from django.utils import timezone

class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)  # 新增按讚數變數，預設為 0

    def __str__(self):
        return f"[{self.timestamp}] {self.content} (ID: {self.note_id}, Likes: {self.likes})"