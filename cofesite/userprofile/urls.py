from django.urls import path
from .views import *
app_name='profile'
urlpatterns = [
    path('profile/',profile,name='profile'),
    path('home/', intiprofile, name='home'),
]