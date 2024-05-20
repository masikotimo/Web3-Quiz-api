from api.models import Question
from api._serializers.question_serializers import QuestionSerializer
from core.mixins import view_mixins
from core.utilities.rest_exceptions import (PermissionDenied)


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
    # #filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get(self, request):
        if 'Questions' in cache:
            # get results from cache
            Questions = cache.get('Questions')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [Question.to_json() for Question in queryset]
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
