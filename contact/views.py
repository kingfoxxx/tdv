from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Contacts, ContactText
from .serializer import ContactSerializer, ContactTextSerializer

class ContactView(ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contacts.objects.filter(active=True)

# class ContactTextView(APIView):
#     def get(self, request, format=None):
#         queryset = ContactText.objects.first()
#         serializer = ContactTextSerializer(queryset)
#         return Response(serializer.data)

class ContactTextView(ListAPIView):
    serializer_class = ContactTextSerializer
    queryset = ContactText.objects.all()
