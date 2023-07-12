from django.urls import path
from ecommerce import views

urlpatterns=[
    # About us 
    path('shop', views.ProductListView.as_view(),name='shop'),
    path('product/<int:pk>', views.ProductDetailView.as_view(),name='product-detail'),
    
   
    
    
    ] 