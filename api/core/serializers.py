from rest_framework import routers, serializers, viewsets
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'adress', 'age', 'email', 'date')

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Client.history.model
        fields = '__all__'

class DateSerializer(serializers.ModelSerializer):
    pass


