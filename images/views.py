from rest_framework import viewsets
from .models import Image, Categorie
from .serializers import ImageSerializer, CategorieSerializer

class CategorieView(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('image_id')
    serializer_class = ImageSerializer 

class DeplacementsView(viewsets.ModelViewSet):
    queryset = Image.objects.filter(categorie=1)
    serializer_class = ImageSerializer

class HabitationsView(viewsets.ModelViewSet):
    queryset = Image.objects.filter(categorie=2)
    serializer_class = ImageSerializer

class LoisirsView(viewsets.ModelViewSet):
    queryset = Image.objects.filter(categorie=3)
    serializer_class = ImageSerializer

class NutritionsView(viewsets.ModelViewSet):
    queryset = Image.objects.filter(categorie=4)
    serializer_class = ImageSerializer

class RelationsComView(viewsets.ModelViewSet):
    queryset = Image.objects.filter(categorie=5)
    serializer_class = ImageSerializer

class ResponsabilitesView(viewsets.ModelViewSet):
    queryset = Image.objects.filter(categorie=6)
    serializer_class = ImageSerializer

class SoinsPersonnelsView(viewsets.ModelViewSet):
    queryset = Image.objects.filter(categorie=7)
    serializer_class = ImageSerializer
