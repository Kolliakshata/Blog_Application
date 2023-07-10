
from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.home, name='login'), 
    path('register/', views.home, name='register'),
    path('detail/', views.home, name='detail'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
