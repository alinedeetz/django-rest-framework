from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Product(models.Model):
    product = models.CharField(max_length=50)
    price = models.IntegerField()
    history = HistoricalRecords()

class Client(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(default='default@default.com')
    phone = models.CharField(max_length=15, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

# Client.objects.create(name='Anything', adress='This is an andress', age='20')
