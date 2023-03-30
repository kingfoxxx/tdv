from rest_framework.serializers import ModelSerializer

from .models import Contacts, ContactText

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"

class ContactTextSerializer(ModelSerializer):
    class Meta:
        model = ContactText
        fields = "__all__"
        depth = 2
