from django.db import models

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    enfant = models.ForeignKey('enfants.HandicapEnfant', on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    image = models.ForeignKey('images.Image', related_name='image', on_delete=models.PROTECT)
    habitude = models.CharField(choices=[('O','Oui'),('N','Non'),('V','Voudrais')], null=True, max_length=9)
    aime = models.CharField(choices=[('O','Oui'),('N','Non')],null=True, max_length=3)
    aide = models.CharField(choices=[('O','Oui'),('N','Non')],null=True, max_length=3)
    content = models.CharField(choices=[('O','Oui'),('N','Non')],null=True, max_length=3)


class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    professionnel_id =  models.ForeignKey('professionnels.Professionnel', related_name='professionnel', on_delete=models.PROTECT)
    question_id = models.ForeignKey(Question, on_delete=models.PROTECT) 
    note_aime = models.CharField(max_length=255, null=True)
    note_aide = models.CharField(max_length=255, null=True)
    note_statisfaction = models.CharField(max_length=255, null=True)
