from django.test import TestCase
from datetime import datetime, timedelta
from .models import *

class SessionsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Session.objects.create(session_id=1, enfant=Enfant.objects.create(enfant_id=1, nom='bla', prenom='blabla', age=12, connecte='False'), date="2019-12-09 22:00:00")
        Question.objects.create(question_id=1, session=Session.objects.get(session_id=1), habitude='Oui', aime='Oui', aide='Oui', content='Oui')
        Note.objects.create(note_id=1, professionnel_id=User.objects.create(), question_id=Question.objects.get(question_id=1), note_aime='Oui', note_aide='Oui', note_satisfaction='Oui')

    def test_date(self):
        date_futur = Session(date = datetime.now() + timedelta(days=1))
        self.assertEqual(date_futur.date_actuelle(), True)

    def test_choix_habitude(self):
        question = Question.objects.get(question_id=1)
        self.assertEquals(question.habitude, 'Oui') # A check

    def test_choix_aime(self):
        question = Question.objects.get(question_id=1)
        self.assertEquals(question.aime, 'Oui')

    def test_choix_aide(self):
        question = Question.objects.get(question_id=1)
        self.assertEquals(question.aide, 'Oui')

    def test_choix_content(self):
        question = Question.objects.get(question_id=1)
        self.assertEquals(question.content, 'Oui')

    def test_note_aime_max_length(self):
        note = Note.objects.get(note_id=1)
        max_length_note_aime = note._meta.get_field('note_aime').max_length
        self.assertTrue(max_length_note_aime <= 255)

    def test_note_aide_max_length(self):
        note = Note.objects.get(note_id=1)
        max_length_note_aide = note._meta.get_field('note_aide').max_length
        self.assertTrue(max_length_note_aide <= 255)

    def test_note_satisfaction_max_length(self):
        note = Note.objects.get(note_id=1)
        max_length_note_satisfaction = note._meta.get_field('note_satisfaction').max_length
        self.assertTrue(max_length_note_satisfaction <= 255)