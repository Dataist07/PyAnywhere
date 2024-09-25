from django.urls import path
from . import views

urlpatterns = [path('supermarket/', views.supermarket_list),
               path('<str:supermarket>/<str:nom_drive>/product/', views.product_supermarket_list),
                path('<str:nom_drive>/product/', views.product_list)
               ]