from rest_framework import serializers
from .models import Enfants, Handicaps

class HandicapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handicaps
        fields = ('handicap_id', 'nom_handicap', 'description')

class EnfantSerializer(serializers.ModelSerializer):
    handicaps = serializers.CharField(source='handicap.nom_handicap', read_only=True)
    class Meta:
        model = Enfants
        fields = ('enfant_id', 'nom', 'prenom', 'age', 'handicap', 'handicaps')