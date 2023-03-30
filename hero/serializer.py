from rest_framework.serializers import ModelSerializer

from .models import Hero, HeroImages

class HeroSerializer(ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'
        depth = 2

class HeroImagesSerializer(ModelSerializer):
    class Meta:
        model = HeroImages
        fields = "__all__"
        depth = 2
