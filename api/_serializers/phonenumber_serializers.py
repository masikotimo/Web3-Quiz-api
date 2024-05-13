from api.models import PhoneNumber
from core.mixins.serializer_mixins import ModelSerializer

from core.modules.rest_framework_modules import serializers


class CreatePhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=16)
    primary = serializers.BooleanField(default=False)


class PhoneNumberSerializer(ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['id', 'number']
        lookup_field = 'id'
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
