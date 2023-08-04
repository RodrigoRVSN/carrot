from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Name', max_length=100)
    price = models.FloatField('Price')
    available = models.BooleanField('Available', default = True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
  