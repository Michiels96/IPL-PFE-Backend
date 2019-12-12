from django.test import TestCase
from .models import Enfant, Handicap, HandicapEnfant

class EnfantsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Enfant.objects.create(enfant_id=1, nom='Jean', prenom='Pierre', age=12, connecte='False')
        Handicap.objects.create(handicap_id=1, nom_handicap='aveugle', description='ne voit pas')
        HandicapEnfant.objects.create(handicap_enfant_id=1, enfant=Enfant.objects.get(enfant_id=1), handicap=Handicap.objects.get(handicap_id=1))

    def test_nom_max_length(self):
        enfant = Enfant.objects.get(enfant_id=1)
        max_length_nom = enfant._meta.get_field('nom').max_length
        self.assertTrue(max_length_nom <= 50)

    def test_prenom_max_length(self):
        enfant = Enfant.objects.get(enfant_id=1)
        max_length_prenom = enfant._meta.get_field('prenom').max_length
        self.assertTrue(max_length_prenom <= 50)

    def test_age(self):
        enfant = Enfant.objects.get(enfant_id=1)
        age = enfant.age
        self.assertTrue(age > 0 and age <= 18)

    def test_connecte(self):
        enfant = Enfant.objects.get(enfant_id=1)
        self.assertEquals(enfant.connecte, False)

    def test_nom_handicap_max_length(self):
        handicap = Handicap.objects.get(handicap_id=1)
        max_length_nom_handicap = handicap._meta.get_field('nom_handicap').max_length
        self.assertTrue(max_length_nom_handicap <= 255)

    def test_description_max_length(self):
        handicap = Handicap.objects.get(handicap_id=1)
        max_length_description = handicap._meta.get_field('description').max_length
        self.assertTrue(max_length_description <= 255)