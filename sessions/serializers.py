from rest_framework import serializers
from .models import Session, Question, Note

class QuestionSerializer(serializers.ModelSerializer):
    img_description = serializers.CharField(source='image.description', read_only=True)
    img_categorie = serializers.CharField(source='image.categorie', read_only=True)
    class Meta:
        model = Question
        fields = ('question_id', 'session', 'image', 'img_description', 'img_categorie', 'habitude', 'aime', 'aide', 'content')

class NoteSerializer(serializers.ModelSerializer):
    #prof = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Note
        fields = ('note_id', 'professionnel_id', 'prof','question_id', 'note_aime', 'note_aide', 'note_satisfaction') 

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('session_id', 'enfant', 'date')
