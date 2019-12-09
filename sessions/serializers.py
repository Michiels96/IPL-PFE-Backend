from rest_framework import serializers
from .models import Session, Question, Note
from enfants.models import Enfant
from enfants.serializers import EnfantSerializer


class NoteSerializer(serializers.ModelSerializer):
    #prof = serializers.CharField(source='professeur.email', read_only=True)
    class Meta:
        model = Note
        fields = ('note_id', 'professionnel_id','question_id', 'note_aime', 'note_aide', 'note_satisfaction') 

class QuestionSerializer(serializers.ModelSerializer):
    img_description = serializers.CharField(source='image_correspondante.description', read_only=True)
    img_categorie = serializers.CharField(source='image_correspondante.categorie', read_only=True)
    note = NoteSerializer(read_only=True)
    class Meta:
        model = Question
        fields = ('question_id', 'session', 'image_correspondante', 'img_description', 'img_categorie', 'habitude', 'aime', 'aide', 'content','note')


class SessionSerializer(serializers.ModelSerializer):
    #enfant_session = serializers.CharField(source='session_enfant', read_only=True)
    class Meta:
        model = Session
        fields = ('session_id', 'enfant', 'date')


class FullSessionSerializer(serializers.ModelSerializer):
    question_session = QuestionSerializer(many=True, read_only=True)
    enfant = EnfantSerializer( read_only=True)
    class Meta: 
        model = Session
        fields = ('session_id', 'enfant', 'date','question_session')


class EnfantFullSessionSerializer(serializers.ModelSerializer):
    session_enfant = FullSessionSerializer(many=True, read_only=True)
    class Meta:
        model = Enfant
        fields = ('enfant_id', 'nom', 'prenom', 'age', 'connecte','session_enfant')
    

