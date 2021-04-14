from django.urls import path
from .views import *
urlpatterns = [
    path('all/', views.all_animals, name='all-animals')
]
