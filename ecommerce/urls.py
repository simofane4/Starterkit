from django.urls import path
from ecommerce import views

urlpatterns=[
    # About us 
    path('shop', views.ProductListView.as_view(),name='shop'),
    
   
    
    
    ] 