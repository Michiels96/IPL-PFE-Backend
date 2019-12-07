from django.urls import path, include
from . import views
from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('images', views.ImageView, basename='image')
router.register('categories', views.CategorieView, basename='categorie')
#router.register('repertoire/deplacements', views.DeplacementsView)
# router.register('repertoire/habitation', views.HabitationsView, basename='habitation')
# router.register('repertoire/loisirs', views.LoisirsView, basename='loisir')
# router.register('repertoire/nutrition', views.NutritionsView, basename='nutrition')
# router.register('repertoire/relationscom', views.RelationsComView, basename='relationcom')
# router.register('repertoire/responsabilites', views.ResponsabilitesView, basename='responsabilite')
# router.register('repertoire/soinspersonnnels', views.SoinsPersonnelsView, basename='soinspersonnel')


urlpatterns = [
    path('', include(router.urls))
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)