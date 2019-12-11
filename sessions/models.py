from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from enfants.models import Enfant

class Mandataire(models.Model):
    mandataire_id = models.AutoField(primary_key=True) 
    mandataire = models.CharField(choices=[('Prof','Professionnel'),('P','Parents'),('PE', 'Père'),('ME', 'Mère'),('T','Tuteur'),('E','Enfant'),('M','Medecin'),('AP','Autre Professionnel'),('A','Autre')],max_length=20)
    autre_mandataire = models.CharField(max_length=50, null=True)
    nom = models.CharField(max_length=50,null=True)
    prenom = models.CharField(max_length=50,null=True)
    spécialité = models.CharField(max_length=50,null=True)
    téléphone = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    date_demande = models.DateTimeField()
    objet = models.TextField()

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    enfant = models.ForeignKey(Enfant, related_name='session_enfant', on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    mandataire = models.ForeignKey(Mandataire, related_name='image_correspondante', on_delete=models.PROTECT,null=True)

    def __iter__(self):
        return { self.enfant, 
                 self.date, 
                 self.mandataire }


    def date_actuelle(self):
        return (datetime.now() - self.date).days <= 0

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

    
