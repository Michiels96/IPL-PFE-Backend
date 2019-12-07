from django.db import models

class Categorie(models.Model):
    categorie_id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=100)

def upload_path(instance, filename):
    pass
    #return '/'.join(['repertoire',str(instance.categorie.libelle),filename])

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, related_name='categorie',on_delete=models.PROTECT)
    #image_url = models.ImageField(blank=True, upload_to=upload_path)
