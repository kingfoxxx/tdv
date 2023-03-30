from django.urls import path

from .views import SupportView, DonationView

app_name = 'support'

urlpatterns = [
    path('support/', SupportView.as_view()),
    path('donate_transaction/', DonationView.as_view(), name="donate")
]
