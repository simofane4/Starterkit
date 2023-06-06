from django.urls import path
from user_admin import views



urlpatterns = [
    path('add-post',views.PostCreateView.as_view(),name='add-post')
]