from django.urls import path, include
from . import views
from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('images', views.ImageView, basename='image')
router.register('categories', views.CategorieView, basename='categorie')


urlpatterns = [
    path('', include(router.urls))
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)