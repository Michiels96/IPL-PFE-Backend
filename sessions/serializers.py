from rest_framework import serializers
from .models import Session, Question, Note

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_id', 'session', 'image', 'habitude', 'aime', 'aide', 'content')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('note_id', 'professionnel_id', 'question_id', 'note_aime', 'note_aide', 'note_satisfaction') 

class SessionSerializer(serializers.ModelSerializer):
    enfant_prenom = serializers.CharField(source='enfant.prenom', read_only=True)
    class Meta:
        model = Session
        fields = ('session_id', 'enfant_prenom', 'enfants', 'date')
