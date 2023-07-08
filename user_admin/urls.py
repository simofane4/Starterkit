from django.urls import path
from user_admin import views



urlpatterns = [
    path('add-post',views.PostCreateView.as_view(),name='add-post'),
    path('post-update/<slug:slug>', views.PostUpdateView.as_view(), name='post-update'),
    path('add-product',views.ProductCreateView.as_view(),name='add-product'),
    path('update-product/<int:pk>',views.ProductUpdateView.as_view(),name='update-product'),
    path('add-tva',views.creat_tva,name='add-tva'),
    path('add-category',views.creat_category,name='add-category'),
    
]