from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('sessions', views.SessionsView, basename='session')
router.register('questions', views.QuestionsView, basename='question')
router.register('notes', views.NotesView, basename='note')

urlpatterns = [
    path('', include(router.urls))
] 