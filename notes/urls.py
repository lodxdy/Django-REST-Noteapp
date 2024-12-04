from django.urls import path
from django.http import HttpResponse
from .views import NoteListCreateView

def home(request):
    return HttpResponse("<h1>Welcome to the Django REST App!</h1>")

urlpatterns = [
    path('', home, name='home'),                          # Home view at root
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),  # Notes API
]
