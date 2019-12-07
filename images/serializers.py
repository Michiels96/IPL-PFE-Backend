from rest_framework import serializers
from .models import Image, Categorie

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('categorie_id', 'libelle')

class ImageSerializer(serializers.ModelSerializer):
    categorie_image = serializers.CharField(source='categorie.libelle', read_only=True)
    class Meta:
        model = Image
        fields = ('image_id', 'description', 'categorie', 'categorie_image') 
