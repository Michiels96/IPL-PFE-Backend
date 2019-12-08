from rest_framework import serializers
from .models import Session, Question, Note


class NoteSerializer(serializers.ModelSerializer):
    #prof = serializers.CharField(source='user.email', read_only=True)
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
    class Meta:
        model = Session
        fields = ('session_id', 'enfant', 'date')


class FullSessionSerializer(serializers.ModelSerializer):
    question_session = QuestionSerializer(many=True, read_only=True)
    class Meta: 
        model = Session
        fields = ('session_id', 'enfant', 'date','question_session')
