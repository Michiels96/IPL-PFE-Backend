from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('sessions', views.SessionsView, basename='session')
router.register('full_sessions', views.FullSessionsView, basename='full_session')
router.register('enfant_full_sessions', views.EnfantFullSessionsView, basename='enfant_full_sessions')
router.register('questions', views.QuestionsView, basename='question')
router.register('notes', views.NotesView, basename='note')
router.register('mandataires', views.MandatairesView, basename='mandataire')

urlpatterns = [
    path('', include(router.urls))
] 