from api.models import Question,Category
from core.mixins.serializer_mixins import ModelSerializer
from .category_serializers import CategorySerializer

from core.modules.rest_framework_modules import serializers




class QuestionSerializer(ModelSerializer):
    category = serializers.CharField(max_length=128)
    class Meta:
        model = Question
        exclude = ["created_by", "lastupdated_by", "created_at",
                   "lastupdated_at","id" ]
        lookup_field = 'id'
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
        depth = 1

    def create(self, validated_data):
        category_name = validated_data.pop('category')
        category_instance, _ = Category.objects.get_or_create(name=category_name)
        question_instance = Question.objects.create(category=category_instance, **validated_data)
        return question_instance


