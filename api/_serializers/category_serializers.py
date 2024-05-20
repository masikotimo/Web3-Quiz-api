from api.models import Category
from core.mixins.serializer_mixins import ModelSerializer

from core.modules.rest_framework_modules import serializers




class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ["created_by", "lastupdated_by", "created_at",
                   "lastupdated_at","id" ]
        lookup_field = 'id'
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
