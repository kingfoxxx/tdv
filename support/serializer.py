from rest_framework.serializers import ModelSerializer

from .models import Support, Donation

class SupportSerializer(ModelSerializer):
    class Meta:
        model = Support
        fields = "__all__"

class DonationSerializer(ModelSerializer):
    class Meta:
        model = Donation
        fields = "__all__"
