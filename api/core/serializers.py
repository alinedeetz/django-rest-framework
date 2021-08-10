from rest_framework import routers, serializers, viewsets
from .models import Client, Product

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'adress', 'age', 'email')

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Client.history.model
        fields = '__all__'

class DateSerializer(serializers.ModelSerializer):
    pass

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product.history.model 
        fields = '__all__'


