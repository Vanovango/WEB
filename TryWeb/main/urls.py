from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),        # '' = main url
    path('about', views.about, name='about')
]
