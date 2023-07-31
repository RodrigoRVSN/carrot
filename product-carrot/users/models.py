from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import uuid

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Name', max_length=255)
    city = models.CharField('City', max_length=100)
    email = models.EmailField('Email', unique=True)
    phone = models.CharField('Phone', max_length=15)
    password = models.CharField('Password', max_length=128)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, password):
        is_same_password = check_password(password, self.password)
        return is_same_password