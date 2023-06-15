from django.urls import path
from user_admin import views



urlpatterns = [
    path('add-post',views.PostCreateView.as_view(),name='add-post'),
    path('post-update/<slug:slug>', views.PostUpdateView.as_view(), name='post-update'),
]