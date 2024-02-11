from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('short/<str:short_url>', views.redirect, name='redirect'),
]