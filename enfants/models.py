from django.db import models

class Handicap(models.Model):
    handicap_id = models.AutoField(primary_key=True)
    nom_handicap = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class Enfant(models.Model):
    enfant_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    connecte = models.BooleanField()

class HandicapEnfant(models.Model):
    handicap_enfant_id = models.AutoField(primary_key=True)
    enfant = models.ForeignKey(Enfant, related_name='enfant_h' ,on_delete=models.PROTECT)
    handicap = models.ForeignKey(Handicap, related_name='handicap_h',on_delete=models.PROTECT, null=True)
