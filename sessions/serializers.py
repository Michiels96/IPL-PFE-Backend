from rest_framework import serializers
from .models import Session, Question, Note

class QuestionSerializer(serializers.ModelSerializer):
    img_description = serializers.CharField(source='image_correspondante.description', read_only=True)
    img_categorie = serializers.CharField(source='image_correspondante.categorie', read_only=True)
    class Meta:
        model = Question
        fields = ('question_id', 'session', 'image_correspondante', 'img_description', 'img_categorie', 'habitude', 'aime', 'aide', 'content')

class NoteSerializer(serializers.ModelSerializer):
    prof = serializers.CharField(source='professeur.email', read_only=True)
    class Meta:
        model = Note
        fields = ('note_id', 'professionnel_id', 'prof', 'question_id', 'note_aime', 'note_aide', 'note_satisfaction') 

class SessionSerializer(serializers.ModelSerializer):
    enfant_session = serializers.CharField(source='session_enfant', read_only=True)
    class Meta:
        model = Session
        fields = ('session_id', 'enfant', 'enfant_session', 'date')
