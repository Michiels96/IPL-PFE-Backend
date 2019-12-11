from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

class Handicap(models.Model):
    handicap_id = models.AutoField(primary_key=True)
    nom_handicap = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class PersonneContact(models.Model):
    personne_id = models.AutoField(primary_key=True)
    nom_contact = models.CharField(max_length=50)
    prenom_contact = models.CharField(max_length=50)
    #telephone = PhoneNumberField(null=False, blank=False, unique=True)
    #email = EmailField(max_length=250)
    relation = models.CharField(choices=[('P','Père'),('M','Mère'),('T','Tuteur'),('F','Frère'),('S','Soeur'),('A','Autre')], max_length=20)

# class BesoinParticuler(models.Model):
#     l’enfant présente des difficultés visuelles
#     l’enfant ne voit pas
#     L’enfant présente des difficultés auditives
#     l’enfant n’entend pas
#     L’enfant présente des difficultés pour contrôler avec précision les mouvements de ses bras et mains
#                 à droite   à gauche   bilatéral
#     L’enfant ne peut pas mouvoir ses bras et mains
#              à droite   à gauche   bilatéral
#     L’enfant présente des difficultés pour s’exprimer oralement
#     L’enfant ne peut pas parler
#     L’enfant présente des difficultés pour comprendre les consignes verbales de l’adulte
#     L’enfant présente des difficultés pour comprendre les étapes et/ou les images du jeu
#     L’enfant présente des difficultés pour s’orienter dans l’espace du jeu
#     Autre : texte


class Enfant(models.Model):
    enfant_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True)
    connecte = models.BooleanField(default=False)
    # date_naissance = models.DateField(auto_now=False, auto_now_add=False)
    # langue = models.CharField(max_length=255, null=True)
    # scolarité = models.CharField(choices=[('EO','Enseignement ordinaire'),('ES','Enseignement spécialisé'),('EI','Enseignement en intégration')], null=True, max_length=50)
    # dominance = models.CharField(choices=[('D','Droitier'),('G','Gaucher'),('AB','Ambidextre'),('AD','Adominant')], null=True, max_length=10)
    # personne_contact = models.ForeignKey(PersonneContact, related_name='contact', on_delete=models.PROTECT)

    def __iter__(self):
        return [ self.nom, 
                 self.prenom, 
                 self.age, 
                 self.connecte ]

class HandicapEnfant(models.Model):
    handicap_enfant_id = models.AutoField(primary_key=True)
    enfant = models.ForeignKey(Enfant, related_name='enfant_h' ,on_delete=models.PROTECT)
    handicap = models.ForeignKey(Handicap, related_name='handicap_h',on_delete=models.PROTECT, null=True)
