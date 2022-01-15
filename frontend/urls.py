from django.contrib import admin
from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('detail', views.detail, name="detail-page"),
    path('pesan', views.pesan, name="pesan-page"),
    path('konfirmasi', views.konfirmasi, name="konfirmasi-page"),
]
