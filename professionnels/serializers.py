from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Professionnel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs={'password':{'write_only':True,'required':True}}

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)#ca va hasher le password
        return user


class ProfessionnelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professionnel
        fields = ['professionnel_id', 'nom', 'prenom', 'profession', 'autre_profession', 'telephone', 'user']