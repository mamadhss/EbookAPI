from rest_framework import serializers
from .models import UserAccount

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('username','email','password')
        extra_kwargs = {
            'password':{'write_only':True,'min_length':5,'style':{'input_type':'password'}},
            'username':{'min_length':3}

        }

    def create(self,validate_data):
        """ create new user with encrypted password and return it"""
        return UserAccount.objects.create_user(**validate_data)   





