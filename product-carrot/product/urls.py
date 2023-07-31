from django.contrib import admin
from django.urls import include, path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products', views.ProductView.as_view()),
    path('', include('users.urls')),
]
