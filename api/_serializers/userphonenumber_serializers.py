from api.models import UserPhoneNumber
from core.modules.rest_framework_modules import serializers
from core.mixins.serializer_mixins import ModelSerializer


class UserPhoneNumberSerializer(ModelSerializer):
    phone_number = serializers.CharField(max_length=16)

    class Meta:
        model = UserPhoneNumber
        fields = ['id', 'phone_number', 'primary']
        lookup_field = 'id'
        depth = 1
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
