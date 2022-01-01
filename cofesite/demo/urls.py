from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('' ,include('core.urls',namespace='core')),
    path('profile/' ,include('userprofile.urls',namespace='profile')),
    path('blogs/' ,include('blogs.urls',namespace='blogs')),
    path('summernote/', include('django_summernote.urls')),
    
    #path('login', django.contrib.auth.views.LoginView.as_view(template_name='account/login.html'),name='login'),
    #path(r'^logout/$', django.contrib.auth.views.logout_then_login, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
