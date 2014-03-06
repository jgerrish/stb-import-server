from django.contrib.auth.models import User, Group
from import_server.models import Bill
from rest_framework import serializers


class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BIll
        fields = ('url', 'name', 'bill_type')
