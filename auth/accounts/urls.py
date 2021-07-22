from os import name
from django.urls import path
from .import views
urlpatterns=[
    path('',views.indexView,name='home'),
    path('login/',views.indexLogin,name='login'),
    path('register/',views.indexRegister,name='register'),

]