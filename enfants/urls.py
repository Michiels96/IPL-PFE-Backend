from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('enfants', views.EnfantsView, basename='enfant')
router.register('logged_enfant', views.logged_enfant, basename='logged_enfant')
router.register('non_logged_enfant', views.non_logged_enfant, basename='non_logged_enfant')
router.register('info_supplementaire', views.info_supplementaireview, basename='info_supplementaire')
router.register('personne_contact', views.personne_contactview, basename='personne_contact')
router.register('handicaps', views.HandicapsView, basename='handicap')
router.register('handicaps_enfants', views.HandicapsEnfantsView, basename='handicap_enfant')

urlpatterns = [
    path('', include(router.urls)),
] 