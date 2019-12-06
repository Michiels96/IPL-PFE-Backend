from rest_framework import serializers
from .models import Image, Categorie

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('categorie_id', 'libelle')

class ImageSerializer(serializers.ModelSerializer):
    categories = serializers.CharField(source='categories.libelle', read_only=True)
    class Meta:
        model = Image
        fields = ('image_id','image' ,'description', 'categorie', 'categories') 