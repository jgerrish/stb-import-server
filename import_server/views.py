from django.shortcuts import render
from import_server.models import Bill
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer


class BillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bills to be viewed or edited.
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
