from rest_framework import serializers
from .models import Taxonomy, PostAuthor, PostData
from django.contrib.auth.models import User
from .views import *
from .models import CustomUser

class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = '__all__'

class PostAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAuthor
        fields = '__all__'

class PostDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostData
        fields = '__all__'

# serializers.py

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
              
        



# custom user serializer

# accounts/serializers.py



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user           
