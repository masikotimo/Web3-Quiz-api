from django.urls import path
from api.views import questions_views as views

urlpatterns = [
    path(r'create/',
         views.CreateQuestionViewSet.as_view({'post': 'create'})),
    path('', views.ViewQuestionsListViewSet.as_view(
        {'get': 'list'}), name="view_organizations"),
    path(r'<str:id>/', views.RetrieveQuestionViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_organization"),
    path(r'<str:id>/update/',
         views.UpdateQuestionViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteQuestionViewSet.as_view({'delete': 'destroy'})),
]
