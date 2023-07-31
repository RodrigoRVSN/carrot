from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class Product(admin.ModelAdmin):
  search_fields = ['name']