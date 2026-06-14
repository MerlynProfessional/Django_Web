from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('Members/', views.Member, name = 'Members'),
    path('Members/details/<slug:slug>/', views.details, name = 'details_url'),
    path('testing/', views.testing, name = 'testing'),
]