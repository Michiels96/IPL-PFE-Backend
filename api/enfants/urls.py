from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('enfants', views.EnfantsView, basename='enfant')
router.register('handicaps', views.HandicapsView, basename='handicap')

urlpatterns = [
    path('', include(router.urls))
]