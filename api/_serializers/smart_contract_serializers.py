from rest_framework import serializers
from core.utilities.rest_exceptions import (ValidationError)


class GameSerializer(serializers.Serializer):
    team_name = serializers.CharField(max_length=255)
    score = serializers.IntegerField()
    is_recorded = serializers.BooleanField()



class SaveGameScoreSerializer(serializers.Serializer):
    team_name = serializers.CharField(max_length=100)
    score = serializers.IntegerField()
    from_address = serializers.CharField(max_length=42)  # Ethereum addresses are 42 characters long
    private_key = serializers.CharField(max_length=64) 