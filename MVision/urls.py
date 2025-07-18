

from django.urls import path
from .import views


# localhost:8000/MVision
# localhost:8000/MVision/order
urlpatterns = [
    
    path('', views.all_vision, name='all_vision'),
    
]