from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', ObtainAuthToken.as_view()),
] 