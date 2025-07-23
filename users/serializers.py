from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
import random


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            is_active=False
        )
        user.set_password(validated_data['password'])
        user.confirmation_code = str(random.randint(100000, 999999))
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials or inactive user")


class ConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = CustomUser.objects.get(username=data['username'])
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User not found")

        if user.confirmation_code != data['code']:
            raise serializers.ValidationError("Invalid confirmation code")

        user.is_active = True
        user.confirmation_code = ''
        user.save()
        return user