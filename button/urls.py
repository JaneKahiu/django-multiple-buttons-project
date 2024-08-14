from .import views
from django.urls import path

urlpatterns = [
    path('', views.subscription, name='subscription'),
]