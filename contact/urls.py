from django.urls import path

from .views import ContactView, ContactTextView

app_name = 'contact'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact_text/', ContactTextView.as_view(), name="contact_text")
]
