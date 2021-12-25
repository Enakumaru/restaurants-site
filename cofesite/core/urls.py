from django.urls import path
from .views import *
app_name='core'
urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('blog_single/<str:id>/',blog_single,name='blog_single'),
    path('blog/',Blog,name='blog'),
    path('cart/',cart,name='cart'),
    path('checkout/',checkout,name='checkout'),
    path('contact/',Contact,name='contact'),
    path('menu/',menu,name='menu'),
    path('product-single/<str:id>/',product_single,name='product_single'),
    path('services/',services,name='services'),
    path('shop/',shop,name='shop'),
    path('formms/',formms,name='formms'),
    path('updatecart/',updatecart,name='updatecart'),
    path('home/', intiprofile, name='home'),
]
