from rest_framework import viewsets
from .models import Enfants, Handicaps
from .serializers import EnfantSerializer, HandicapSerializer

class EnfantsView(viewsets.ModelViewSet):
    queryset = Enfants.objects.all()
    serializer_class = EnfantSerializer

class HandicapsView(viewsets.ModelViewSet):
    queryset = Handicaps.objects.all()
    serializer_class = HandicapSerializer