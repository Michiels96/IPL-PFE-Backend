from django.db import models

class Handicap(models.Model):
    handicap_id = models.AutoField(primary_key=True)
    nom_handicap = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class Enfant(models.Model):
    enfant_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True)
    connecte = models.BooleanField(default=False)

class InfoSupplementaire(models.Model):
    enfant = models.OneToOneField(Enfant, related_name='info_enfant', on_delete=models.CASCADE, primary_key=True)
    date_naissance = models.DateTimeField()
    langue = models.CharField(max_length=255, null=True)
    scolarite = models.CharField(choices=[('EO','Enseignement ordinaire'),('ES','Enseignement spécialisé'),('EI','Enseignement en intégration')], null=True, max_length=50)
    niveau_scolaire = models.CharField(max_length=255)
    type_enseignement = models.CharField(max_length=255, null=True)
    dominance = models.CharField(choices=[('D','Droitier'),('G','Gaucher'),('AB','Ambidextre'),('AD','Adominant')], null=True, max_length=10)
    besoin_particulier = models.CharField(choices=[('DV','présente difficultés visuelles'),('VP','ne voit pas'),('DA','présente des difficultés auditives'),('EP','n’entend pas'),('DCD','présente des difficultés pour contrôler avec précision les mouvements de ses bras et mains à droite'),('DCG','présente des difficultés pour contrôler avec précision les mouvements de ses bras et mains à gauche'),('DCB','présente des difficultés pour contrôler avec précision les mouvements de ses bras et mains bilatéral'),('MD','ne peut pas mouvoir ses bras et mains à droite'),('MG','ne peut pas mouvoir ses bras et mains à gauche'),('MB','ne peut pas mouvoir ses bras et mains bilateral'),('DO','présente des difficultés pour s’exprimer oralement'),('PP','ne peut pas parler'),('DCA','présente des difficultés pour comprendre les consignes verbales de l’adulte'),('DEI','présente des difficultés pour comprendre les étapes et/ou les images du jeu'),('DOE','présente des difficultés pour s’orienter dans l’espace du jeu'),('AU','Autre')], null=True, max_length=100)
    autre_besoin_particulier = models.CharField(max_length=255, null=True)

class PersonneContact(models.Model):
    personne_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=250, null=True)
    relation = models.CharField(choices=[('P','Père'),('M','Mère'),('T','Tuteur'),('F','Frère'),('S','Soeur'),('A','Autre')], max_length=20)
    autre_relation = models.CharField(max_length=50,null=True)
    enfant = models.ForeignKey(Enfant, related_name='enfant', on_delete=models.CASCADE)

class HandicapEnfant(models.Model):
    handicap_enfant_id = models.AutoField(primary_key=True)
    enfant = models.ForeignKey(Enfant, related_name='enfant_h' ,on_delete=models.CASCADE)
    handicap = models.ForeignKey(Handicap, related_name='handicap_h',on_delete=models.CASCADE, null=True)
