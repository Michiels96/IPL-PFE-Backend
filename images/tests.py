from django.test import TestCase
from .models import *

class EnfantsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Categorie.objects.create(categorie_id=1, libelle='deplacements')
        Image.objects.create(image_id=1, description='bus', categorie=Categorie.objects.get(categorie_id=1))

    def test_libelle_max_length(self):
        cat = Categorie.objects.get(categorie_id=1)
        max_length_libelle = cat._meta.get_field('libelle').max_length
        self.assertTrue(max_length_libelle <= 100)

    def test_description_max_length(self):
        img = Image.objects.get(image_id=1)
        max_length_description = img._meta.get_field('description').max_length
        self.assertTrue(max_length_description <= 100)
