from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:poke_id>/', views.index_params),
    
]