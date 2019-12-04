from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('images', views.ImageView, basename='image')
router.register('categories', views.CategorieView, basename='categorie')

urlpatterns = [
    path('', include(router.urls))
] 