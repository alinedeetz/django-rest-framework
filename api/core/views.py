from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Client, Product
from .serializers import ClientSerializer, ProductSerializer, ClientHistorySerializer
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

class HistoryViewSet(viewsets.ModelViewSet):
    # queryset = Client.history.filter()
    serializer_class = ClientHistorySerializer

    def get_queryset(self):
        id = self.request.query_params.get('id')
        # print('UID = {}'.format(id))
        if id is None:
            return Client.history.all()
        else:
            return Client.history.filter(id=id)



