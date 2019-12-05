from rest_framework import serializers
from .models import Enfant, Handicap, HandicapEnfant

class HandicapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handicap
        fields = ('handicap_id', 'nom_handicap', 'description')

class EnfantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfant
        fields = ('enfant_id', 'nom', 'prenom', 'age') 
    
class HandicapEnfantSerializer(serializers.ModelSerializer):
    enfant_h = serializers.CharField(source='enfant_h.nom', read_only=True)
    handicap_h = serializers.CharField(source='handicap_h.nom_handicap', read_only=True)
    class Meta:
        model = HandicapEnfant
        fields = ('handicap_enfant_id', 'enfant', 'enfant_h', 'handicap', 'handicap_h')

