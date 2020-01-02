from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
]