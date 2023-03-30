from rest_framework.serializers import ModelSerializer

from .models import Genre, Track

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        depth = 2

class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
        depth = 2
