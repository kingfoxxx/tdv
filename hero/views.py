from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import HeroSerializer, HeroImagesSerializer
from .models import Hero, HeroImages

class HomePageView(APIView):
    def get(self, request):
        return Response({"msg":"Welcome to the home page"}, status=status.HTTP_200_OK)

class HeroView(ListAPIView):
    serializer_class = HeroSerializer
    queryset = Hero.objects.filter(is_active=True)

class HeroImageView(ListAPIView):
    serializer_class = HeroImagesSerializer

    def get_queryset(self):
        queryset = HeroImages.objects.all()
        heroId = self.request.query_params.get('heroId')
        print(f'heroId:- {heroId}')
        if heroId is not None:
            queryset = queryset.filter(hero__id=heroId)
        return queryset
