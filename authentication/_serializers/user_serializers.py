from django.db import IntegrityError
from api.models import   PhoneNumber, UserPhoneNumber
from api._serializers.userphonenumber_serializers import UserPhoneNumberSerializer
from django.db.models import fields
from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response
from authentication.models import Driver, Passenger, User
from api._serializers.phonenumber_serializers import CreatePhoneNumberSerializer, PhoneNumberSerializer

from core.mixins.serializer_mixins import ModelSerializer


class RegisterUserSerializer(ModelSerializer):
    password = serializers.CharField(
        max_length=254,
        min_length=6,
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)

        # EmailAddress.objects.create(
        #     user=user, email=user.email, verified=True, primary=True)
        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
            'date_joined',
            'is_driver',
            'is_passenger',
            'is_verified',
            "last_login"
        ]
        extra_kwargs = {
            'is_verified': {'write_only': True},
            'is_admin': {'write_only': True},
            'is_passenger': {'write_only': True},
            'is_driver': {'write_only': True},
        }
        depth = 3


class UpdateUserSerializer(serializers.ModelSerializer):
    phone_numbers = CreatePhoneNumberSerializer(many=True, required=False)

    class Meta:
        model = User
        exclude = [
            'password',
            'is_superuser',
            'email',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
            'date_joined',
            'is_driver',
            'is_passenger',
            'is_verified',
            'last_login',
        ]
        extra_kwargs = {
            'is_verified': {'write_only': True},
            'is_admin': {'write_only': True},
            'is_passenger': {'write_only': True},
            'is_driver': {'write_only': True},
        }
        depth = 3

    def update(self, instance, validated_data):
        phone_numbers_data = validated_data.pop('phone_numbers', [])
        
        # Update fields of the User model
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        # Update phone numbers
        for phone_number_data in phone_numbers_data:
            try:
                user_instance = User.objects.get(Id=instance.Id)
                phone_number_instance = PhoneNumber.objects.create(number=phone_number_data.get('phone_number', ""))
                primary = phone_number_data.get('primary', False)

                UserPhoneNumber.objects.create(
                    user=user_instance, phone_number=phone_number_instance, primary=primary
                )
            except IntegrityError:
                raise ValidationError({'detail': 'This Number has already been used in the system !'})

        return instance



class UserProfileSerializer(ModelSerializer):
    phone_numbers = UserPhoneNumberSerializer(many=True)  # Use the related name 'phone_numbers'

    class Meta:
        model = User
        exclude = [
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
            'is_verified',
            "last_login"

        ]

        depth = 3

    