from django.db import models

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.FloatField('Price')
    available = models.BooleanField('Available', default = True)

    def __str__(self) -> str:
        return self.name
    
