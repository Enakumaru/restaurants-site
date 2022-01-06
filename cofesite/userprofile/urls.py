from django.urls import path
from .views import profile,edit_userSetting,profileView,tet,edit_Customer,orderHistory
app_name='profile'
urlpatterns = [
    #path('profile/',profile,name='profile'),
    #path('home/', intiprofile, name='home'),
    path('edit/settings',edit_userSetting.as_view(),name='userEdit'),
    path('edit/<int:pk>',edit_Customer.as_view(),name='edit_Customer'),
    path('<int:pk>',profileView.as_view(),name='profileview'),
    path('orderHistory/<int:pk>',orderHistory.as_view(),name='orderhistory'),
    
    path('', tet.as_view(), name='test2'),
    
]
