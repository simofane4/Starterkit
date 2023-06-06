from django.urls import path
from blog import views



urlpatterns=[
    # About us 
    path('about/', views.AboutView.as_view(),name='about'),
    
    path('blog/', views.BlogView.as_view(),name='blog'),
    path('contact/', views.ContactView.as_view(),name='contact'),
    path('post-detail/<slug:slug>/', views.postdetail,name="post-detail"),
    path('detail/<slug:slug>/Favourites', views.Favorites, name='Favorites'),
    #path('detail/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    
    
    ]