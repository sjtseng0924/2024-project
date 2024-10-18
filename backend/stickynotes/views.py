import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Note
from django.views.decorators.csrf import csrf_exempt

# Send messages
@csrf_exempt
def add_note(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            content = data.get('note_content')
            Note.objects.create(content=content, likes=0)  # 初始化 likes 為 0
            return JsonResponse({"status": "Note added successfully"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"status": "Invalid JSON"}, status=400)

@csrf_exempt
def get_one_note(request, note_id):
    if request.method == 'GET':
        try:
            notes = Note.objects.filter(note_id=note_id)
            if notes:
                return JsonResponse({"notes": [{"content": note.content, "time": note.timestamp, "likes": note.likes, "note_id": note.note_id} for note in notes]})
            else:
                return JsonResponse({"status": "Note not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"status": "Invalid JSON"}, status=400)

@csrf_exempt
def get_all_note(request):
    if request.method == 'GET':
        try:
            notes = Note.objects.all()
            print(notes)
            return JsonResponse({"notes": [{"content": note.content, "time": note.timestamp, "likes": note.likes, "note_id": note.note_id} for note in notes]})
        except json.JSONDecodeError:
            return JsonResponse({"status": "Invalid JSON"}, status=400)
@csrf_exempt
def update_likes(request, note_id):
    if request.method == 'POST':
        try:
            note = Note.objects.get(note_id=note_id)
            data = json.loads(request.body)
            new_likes = data.get('likes', None)

            if new_likes is not None:
                note.likes = new_likes
                note.save()
                return JsonResponse({"status": "Likes updated successfully"}, status=200)
            else:
                return JsonResponse({"status": "Missing 'likes' in request"}, status=400)
        except Note.DoesNotExist:
            return JsonResponse({"status": "Note not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"status": "Invalid JSON"}, status=400)
