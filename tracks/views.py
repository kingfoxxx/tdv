from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.db.models import Q

from .serializer import GenreSerializer, TrackSerializer
from .models import Genre, Track

class GenreView(ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.filter(is_active=True).order_by('-created_timestamp')


class TrackView(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        queryset = Track.objects.filter(is_active=True).order_by('-created_timestamp')

        genreId = self.request.query_params.get('genreId', None)

        try:
            genreId = int(genreId)
        except ValueError:
            return Track.objects.none()

        if genreId is not None and genreId == 0:
            queryset = queryset
        elif genreId is not None and genreId != 0:
            queryset = queryset.filter(genre__id=genreId)
        else:
            queryset = queryset.objects.none()

        return queryset

# class TrackSearchView(APIView):
#     def get(self, request):
#         search_param = request.GET.get('search_param', '')
#         query = Q(title__icontains=search_param) & Q(is_active=True)
#         my_objects = Track.objects.filter(query).order_by('-created_timestamp')
#         serializer = TrackSerializer(my_objects, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class TrackSearchView(ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):

        try:
            search_param = self.request.query_params.get('search_param', None)
        except ValueError:
            return Track.objects.none()
        if search_param is not None:
            query = Q(title__icontains=search_param) & Q(is_active=True)
            queryset = Track.objects.filter(query)

        return queryset
