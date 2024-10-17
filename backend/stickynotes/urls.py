from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_note, name='add_note'),
    path('add', views.add_note, name='add_note'),
    path('get/', views.get_all_note, name='get_all_note'),
    path('get', views.get_all_note, name='get_all_note'),
    path('get/<int:note_id>/', views.get_one_note, name='get_one_note'),
    path('get/<int:note_id>', views.get_one_note, name='get_one_note'),
]