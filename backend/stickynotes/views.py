import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Note
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Send messages
@csrf_exempt
def add_note(request):
    if request.method == 'POST':
        try:
            print(request.body)
            data = json.loads(request.body)
            content = data.get('note_content')
            Note.objects.create(content=content)
            return JsonResponse({"status": "Note added successfully"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"status": "Invalid JSON"}, status=400)

@csrf_exempt
def get_one_note(request, note_id):
    if request.method == 'GET':
        try:
            notes = Note.objects.filter(note_id=note_id)
            return JsonResponse({"notes": [{"content": note.content, "time": note.timestamp, "note_id": note.note_id} for note in notes]})
        except json.JSONDecodeError:
            return JsonResponse({"status": "Invalid JSON"}, status=400)

@csrf_exempt
def get_all_note(request):
    if request.method == 'GET':
        try:
            notes = Note.objects.all()
            return JsonResponse({"notes": [{"content": note.content, "time": note.timestamp, "note_id": note.note_id} for note in notes]})
        except json.JSONDecodeError:
            return JsonResponse({"status": "Invalid JSON"}, status=400)

