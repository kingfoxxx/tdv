from django.urls import path

from .views import GenreView, TrackView, TrackSearchView

app_name='tracks'

urlpatterns = [
    path('genres/', GenreView.as_view(), name='genres'),
    path('tracks/', TrackView.as_view(), name='tracks'),
    path('track_search/', TrackSearchView.as_view(), name='track_search')
]
