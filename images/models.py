from django.db import models

class Categorie(models.Model):
    categorie_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=100)

def upload_path(instance, filename):
    return '/'.join([str(instance.categorie.libelle),filename])

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(blank=True, upload_to=upload_path)
    description =  models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, related_name='categorie',on_delete=models.PROTECT)
