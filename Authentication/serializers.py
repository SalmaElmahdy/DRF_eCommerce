from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255,min_length=3)
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    
    class Meta:
        model=User
        fields=['email','username','password']
        
    def validate(self,attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')
        
        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alpanumeric characters')
        return attrs
    
    def create(self, validated_data):
        password=validated_data.pop("password")
        # ISSUE::
        # when create user should set password with set_password()
        # as it hashed password if we do not use it when create user leads to :
        # when login the user with auth.authenticate() will always failed to autheticate the user
        user=super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
    
    

class EmailVerificationSerializer(serializers.ModelSerializer):
    token=serializers.CharField(max_length=555)
    class Meta:
        model=User
        fields=['token']
        

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255,min_length=3)
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    username=serializers.CharField(max_length=68,min_length=6,read_only=True)
    tokens=serializers.CharField(read_only=True)
    
    class Meta:
        model=User
        fields=['email','password','username','tokens']
        
    def validate(self, attrs):
        email=attrs.get('email','')
        password=attrs.get('password','')
        user=auth.authenticate(email=email,password=password)
        if not user:
            raise AuthenticationFailed('Inalid Credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
        
        return {
            'email':user.email,
            'username':user.username,
            'tokens':user.tokens()
        }
