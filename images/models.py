from django.db import models

class Categorie(models.Model):
    categorie_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=100)

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    description =  models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, related_name='categorie',on_delete=models.PROTECT)
