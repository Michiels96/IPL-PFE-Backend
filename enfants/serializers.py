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
    class Meta:
        model = HandicapEnfant
        fields = ('handicap_enfant_id', 'enfant', 'handicap') 