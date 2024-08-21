from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = User
        fields = ['id','username','password']
        # write_only tell Django that we want to accept a password when creating a new user but
        # we dont want to return the password when we are giving information about user (by 
        # specifying wrtie_only).  
        extra_kwargs = {"password" : {"write_only" : True}}
        
    def create(self, validated_data) :
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Note
        fields = ['id','title','content','created_at','author']
        extra_kwargs = {'author' : {"read_only" : True}}