from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),        # '' = main url
    path('about', views.about)
]
