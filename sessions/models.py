from django.db import models
from django.contrib.auth.models import User
from enfants.models import Enfant

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    enfant = models.ForeignKey(Enfant, related_name='session_enfant', on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    session = models.ForeignKey(Session,related_name='question_session' ,on_delete=models.PROTECT)
    image_correspondante = models.ForeignKey('images.Image', related_name='image_correspondante', on_delete=models.PROTECT,null=True)#a modifier !
    habitude = models.CharField(choices=[('O','Oui'),('N','Non'),('V','Voudrais')], null=True, max_length=9)
    aime = models.CharField(choices=[('O','Oui'),('N','Non')],null=True, max_length=3)
    aide = models.CharField(choices=[('O','Oui'),('N','Non')],null=True, max_length=3)
    content = models.CharField(choices=[('O','Oui'),('N','Non')],null=True, max_length=3)

class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    professionnel_id =  models.ForeignKey(User, related_name='professeur', on_delete=models.PROTECT)
    question_id = models.OneToOneField(Question, on_delete=models.PROTECT) 
    note_aime = models.CharField(max_length=255, null=True)
    note_aide = models.CharField(max_length=255, null=True)
    note_satisfaction = models.CharField(max_length=255, null=True)

    
