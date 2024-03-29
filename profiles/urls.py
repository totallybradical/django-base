from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('<int:id>/', views.profile_detail, name='profile_detail'),
]