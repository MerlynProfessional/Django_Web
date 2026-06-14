from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('Members/', views.Member, name = 'Members'),
    path('Members/details/<int:id>/', views.details, name = 'Member_details'),
    path('testing/', views.testing, name = 'testing'),
]