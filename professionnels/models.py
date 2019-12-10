from django.db import models
from django.contrib.auth.models import User

class Professionnel(models.Model):
    professionnel_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=42)
    prenom = models.CharField(max_length=42)
    profession = models.CharField(max_length=42, choices=[('Erg','Ergothérapeute'),('Psy','Psychologue'),('Ed','Educateur'),('Ki','Kinésithérapeute'),('En','Enseignant'),('Au','Autre')],null=True)
    autre_profession = models.CharField(max_length=42,null=True)
    telephone = models.CharField(max_length=12)
    user = models.IntegerField(null=True)

    def __str__(self):
        return self.nom




#On utilise le model User de rest