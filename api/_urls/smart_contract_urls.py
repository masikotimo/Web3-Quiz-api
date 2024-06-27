from django.urls import path
from api.views import smart_contract_views as views

urlpatterns = [
    path('save-game-score/', views.SaveGameScoreView.as_view(), name='save_game_score'),
    path('get-all-game-scores/', views.GetAllGameScoresView.as_view(), name='get_all_game_scores'),

]
