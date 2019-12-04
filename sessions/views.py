from rest_framework import viewsets
from .models import Session, Question, Note
from .serializers import SessionSerializer, QuestionSerializer, NoteSerializer

class SessionsView(viewsets.ModelViewSet):
    queryset = Sessions.objects.all()
    serializer_class = SessionSerializer

class QuestionsView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class NotesView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer 