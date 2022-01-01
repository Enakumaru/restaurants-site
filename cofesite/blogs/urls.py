from django.urls import path
from .views import *
app_name='blog'
urlpatterns = [
    
    
    path('testt/',hello.as_view(),name='testt'),
    path('P-blog/',P_blog.as_view(),name='P-blog'),
    path('P-blog/edit/<str:pk>/',P_updateblog.as_view(),name='P_updateblog'),
    path('P-blog/delete/<str:pk>/',deleteblog.as_view(),name='deleteblog'),
    path('blogcategory/<str:cats>/', categoryview, name='blogcategory'),
    path('hh/',test,name='hh')
]