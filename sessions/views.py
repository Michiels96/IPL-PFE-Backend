from rest_framework import viewsets
from .models import Session, Question, Note, Mandataire
from enfants.models import Enfant
from .serializers import SessionSerializer, QuestionSerializer, NoteSerializer,FullSessionSerializer,EnfantFullSessionSerializer, MandataireSerializer

class SessionsView(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class QuestionsView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class NotesView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer 

class FullSessionsView(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = FullSessionSerializer

class EnfantFullSessionsView(viewsets.ModelViewSet):
    queryset = Enfant.objects.all()
    serializer_class = EnfantFullSessionSerializer

class MandatairesView(viewsets.ModelViewSet):
    queryset = Mandataire.objects.all()
    serializer_class = MandataireSerializer