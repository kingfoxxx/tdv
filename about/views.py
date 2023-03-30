from django.shortcuts import render

from rest_framework.generics import ListAPIView

from .serializer import AboutSerializer
from .models import About

class AboutView(ListAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
