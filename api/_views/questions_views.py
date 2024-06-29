from api.models import Question
from api._serializers.question_serializers import QuestionSerializer
from core.mixins import view_mixins
from core.utilities.rest_exceptions import PermissionDenied
from django.core.cache import cache
from django.conf import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', 60 * 15)  # 15 minutes

class CreateQuestionViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewQuestionsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    permission_classes = []
    serializer_class = QuestionSerializer
    lookup_field = 'id'
    search_fields = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name=category)
        return queryset

    def get(self, request):
        if 'Questions' in cache:
            # get results from cache
            Questions = cache.get('Questions')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception
        else:
            queryset = self.get_queryset()
            results = [question.to_json() for question in queryset]
            # store data in cache
            cache.set('Questions', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrieveQuestionViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdateQuestionViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeleteQuestionViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception
