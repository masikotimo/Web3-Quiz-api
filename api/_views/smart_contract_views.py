
from authentication.models import Driver
from rest_framework.response import Response
from rest_framework import status, generics
from api._serializers.smart_contract_serializers import GameSerializer ,SaveGameScoreSerializer
from core.utilities.rest_exceptions import (ValidationError)
from business_logic.smart_contract.provider import save_game_scores,get_all_game_details,wait_for_confirmation



class SaveGameScoreView(generics.GenericAPIView):
    serializer_class = SaveGameScoreSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            team_name = serializer.validated_data['team_name']
            score = serializer.validated_data['score']
            from_address = serializer.validated_data['from_address']
            private_key = serializer.validated_data['private_key']

            try:
                tx_hash = save_game_scores(team_name, score, from_address, private_key)
                return Response({"transaction_hash": tx_hash}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GetAllGameScoresView(generics.GenericAPIView):
    serializer_class = GameSerializer

    def get(self, request):
        try:
            team_names, scores, is_recorded_arr = get_all_game_details()
            games = [
                {"team_name": team_names[i], "score": scores[i], "is_recorded": is_recorded_arr[i]}
                for i in range(len(team_names))
            ]
            serializer = self.get_serializer(games, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)