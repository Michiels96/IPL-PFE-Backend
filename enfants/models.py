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

class HandicapEnfant(models.Model):
    handicap_enfant_id = models.AutoField(primary_key=True)
    enfant = models.ForeignKey(Enfant, on_delete=models.PROTECT)
    handicap = models.ForeignKey(Handicap, on_delete=models.PROTECT)