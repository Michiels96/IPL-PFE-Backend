from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('enfants', views.EnfantsView, basename='enfant')
router.register('handicaps', views.HandicapsView, basename='handicap')
router.register('handicaps_enfants', views.HandicapsEnfantsView, basename='handicap_enfant')

urlpatterns = [
    path('', include(router.urls)),
] 