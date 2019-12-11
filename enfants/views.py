from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Enfant, Handicap, HandicapEnfant,PersonneContact,InfoSupplementaire
from .serializers import EnfantSerializer, HandicapSerializer, HandicapEnfantSerializer,InfoSupplementaireSerializer,PersonneContactSerializer
from rest_framework.response import Response

class EnfantsView(viewsets.ModelViewSet):
    queryset = Enfant.objects.all()
    serializer_class = EnfantSerializer

class logged_enfant(viewsets.ModelViewSet):
    queryset = Enfant.objects.all().filter(connecte="True")
    serializer_class = EnfantSerializer

class non_logged_enfant(viewsets.ModelViewSet):
    queryset = Enfant.objects.all().filter(connecte="False")
    serializer_class = EnfantSerializer

class HandicapsView(viewsets.ModelViewSet):
    queryset = Handicap.objects.all()
    serializer_class = HandicapSerializer

class info_supplementaireview(viewsets.ModelViewSet):
    queryset = InfoSupplementaire.objects.all()
    serializer_class = InfoSupplementaireSerializer

class personne_contactview(viewsets.ModelViewSet):
    queryset = PersonneContact.objects.all()
    serializer_class = PersonneContactSerializer

class HandicapsEnfantsView(viewsets.ModelViewSet):
    queryset = HandicapEnfant.objects.all()
    serializer_class = HandicapEnfantSerializer
