from django.urls import path
from . import views

# url list
urlpatterns = [
    path('', views.rolls, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('order/', views.order, name='order')
]