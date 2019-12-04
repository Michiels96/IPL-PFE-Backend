from rest_framework import viewsets
from .models import Image, Categorie
from .serializers import ImageSerializer, CategorieSerializer

class CategorieView(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer 