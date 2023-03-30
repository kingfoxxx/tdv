from django.urls import path

from .views import HeroView, HeroImageView, HomePageView

app_name = 'hero'

urlpatterns = [
    path('hero/', HeroView.as_view(), name='hero_view'),
    path('hero-image/', HeroImageView.as_view(), name='hero-image'),
    path('home/', HomePageView.as_view(), name='home_page')
]
