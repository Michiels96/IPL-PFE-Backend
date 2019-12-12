from rest_framework import serializers
from .models import Session, Question, Note, Mandataire
from enfants.models import Enfant
from enfants.serializers import EnfantSerializer

class MandataireSerializer(serializers.ModelSerializer):
    date_demande = serializers.DateField(format='%d/%m/%Y')
    class Meta:
        model = Mandataire
        fields = ('mandataire_id', 'mandataire', 'autre_mandataire', 'nom', 'prenom', 'spécialité', 'téléphone', 'email', 'date_demande', 'objet')

class NoteSerializer(serializers.ModelSerializer):
    #prof = UserSerializer(read_only=True)
    class Meta:
        model = Note
        fields = ('note_id', 'professionnel_id', 'question_id', 'note_aime', 'note_aide', 'note_satisfaction') 

class QuestionSerializer(serializers.ModelSerializer):
    img_description = serializers.CharField(source='image_correspondante.description', read_only=True)
    img_categorie = serializers.CharField(source='image_correspondante.categorie', read_only=True)
    note = NoteSerializer(read_only=True)
    class Meta:
        model = Question
        fields = ('question_id', 'session', 'image_correspondante', 'img_description', 'img_categorie', 'habitude', 'aime', 'aide', 'content','note')


class SessionSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')
    class Meta:
        model = Session
        fields = ('session_id', 'enfant', 'date')


class FullSessionSerializer(serializers.ModelSerializer):
    question_session = QuestionSerializer(many=True, read_only=True)
    enfant = EnfantSerializer( read_only=True)
    date = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')
    class Meta: 
        model = Session
        fields = ('session_id', 'enfant', 'date','question_session')


class EnfantFullSessionSerializer(serializers.ModelSerializer):
    session_enfant = FullSessionSerializer(many=True, read_only=True)
    class Meta:
        model = Enfant
        fields = ('enfant_id', 'nom', 'prenom', 'age', 'connecte','session_enfant')