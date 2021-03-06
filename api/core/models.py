from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Product(models.Model):
    product = models.CharField(max_length=50)
    cost = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    history = HistoricalRecords()

class Client(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    adress = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(default='default@default.com')
    phone = models.CharField(max_length=15, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


# Client.objects.create(name='Anything', adress='This is an andress', age='20')
