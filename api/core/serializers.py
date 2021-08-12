from rest_framework import routers, serializers, viewsets
from .models import Client, Product

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'adress', 'age', 'email')

class ClientHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Client.history.model
        fields = '__all__'

class DateSerializer(serializers.ModelSerializer):
    pass

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product.history.model 
        fields = '__all__'


