from rest_framework.generics import ListCreateAPIView
from .models import Note
from .serializers import NoteSerializer

class NoteListCreateView(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
