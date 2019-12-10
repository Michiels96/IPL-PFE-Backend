from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer,ProfessionnelSerializer
from .models import Professionnel


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ProfessionnelViewSet(viewsets.ModelViewSet):
    queryset = Professionnel.objects.all()
    serializer_class = ProfessionnelSerializer