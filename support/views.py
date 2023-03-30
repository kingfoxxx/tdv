from django.conf import settings

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import SupportSerializer, DonationSerializer
from .models import Support, Donation


class SupportView(ListAPIView):
    serializer_class = SupportSerializer
    queryset = Support.objects.all()

class DonationView(APIView):
    def post(self, request):
        amount = request.query_params.get('amount', None)
        email = request.query_params.get('email', None)
        firstname = request.query_params.get('firstname', None)
        lastname = request.query_params.get('lastname', None)
        reference = request.query_params.get('reference', None)
        transaction_id = request.query_params.get('transaction_id', None)
        transaction_message = request.query_params.get('transaction_message', None)
        print(f'request {request}')
        if amount and email and firstname and lastname and reference and transaction_id and transaction_message:
            donation = Donation.objects.create(
                amount=amount, email=email, first_name=firstname, last_name=lastname, reference=reference,
                transanction_id=transaction_id, transanction_message=transaction_message
            )
            return Response({'msg', 'The transaction is a success nad have been saved successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'There was an error and the transaction was not saved successfully'}, status=status.HTTP_400_BAD_REQUEST)
