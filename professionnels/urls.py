from django.urls import path, include
from . import views
from .views import CustomObtainAuthToken
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register('professionnels', views.ProfessionnelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('login/', ObtainAuthToken.as_view()),
    path('login/', CustomObtainAuthToken.as_view()),
] 