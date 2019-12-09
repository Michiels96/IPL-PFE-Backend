from django.urls import path, include
from . import views
from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('images', views.ImageView, basename='image')
router.register('categories', views.CategorieView, basename='categorie')
router.register('deplacements', views.DeplacementsView, basename='deplacement')
router.register('habitation', views.HabitationsView, basename='habitation')
router.register('loisirs', views.LoisirsView, basename='loisir')
router.register('nutrition', views.NutritionsView, basename='nutrition')
router.register('relationscom', views.RelationsComView, basename='relationcom')
router.register('responsabilites', views.ResponsabilitesView, basename='responsabilite')
router.register('soinspersonnels', views.SoinsPersonnelsView, basename='soinspersonnel')

urlpatterns = [
    path('', include(router.urls))
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)