from rest_framework import serializers
from .models import Enfant, Handicap, HandicapEnfant

class HandicapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handicap
        fields = ('handicap_id', 'nom_handicap', 'description')

class EnfantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfant
        fields = ('enfant_id', 'nom', 'prenom', 'age', 'connecte') 
    
class HandicapEnfantSerializer(serializers.ModelSerializer):
    prenom_enfant = serializers.CharField(source='enfant.prenom', read_only=True)
    nom_enfant = serializers.CharField(source='enfant.nom', read_only=True)
    nom_handicap = serializers.CharField(source='handicap.nom_handicap', read_only=True)
    class Meta:
        model = HandicapEnfant
        fields = ('handicap_enfant_id', 'enfant', 'prenom_enfant', 'nom_enfant', 'handicap', 'nom_handicap')

