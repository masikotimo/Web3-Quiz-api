"""
    Client Account Managers
"""
from rest_framework.response import Response
from rest_framework import status

from business_logic.management.passenger_management import PassengerManager
from business_logic.management.user_management import UserManager
from authentication._serializers import user_serializers
from business_logic.utilities.mailing import EmailVerificationLinkSender
from core.utilities.auth import get_authenticated_user
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed, ValidationError

RegisterUserSerializer = user_serializers.RegisterUserSerializer


class AccountCreator():

    def create(self, request):
        """
        A method for registering a quiz Client member
        """
        try:
            validated_data = request['validated_data']
            request = request['request']
            email = validated_data.get('email')
            user_count = UserManager().get_list().filter(email=email).count() or 0
            
            if user_count >= 1:
                # If a user with the same email already exists, raise an error
                raise ValidationError({'detail': 'User with this email already exists.'})
            
            User = get_user_model()
            password = validated_data.pop('password')  # Remove password from validated_data
            
            user = User.objects.create_user(password=password, **validated_data)
            validated_data = {'user': user}
            authenticated_user = get_authenticated_user(request)  # or AnonymousUser
            if authenticated_user.__str__() == 'AnonymousUser':
                authenticated_user = user
            return EmailVerificationLinkSender(request).send()
        except Exception as exception:
            raise exception
