from django.db.models import fields
from django.db.models.base import Model
from django.http import request
from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic import ListView 
from core.models import *
from allauth.account.views  import SignupView
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
def profile(request):
    
    context = {
        'user':request.user
    }
    return render(request,'profile/profile.html',context)

#def Signup (request,SignupView):
    #email= SignupView.user.email
    #customer,created=Customer.objects.get_or_create(email=email,user=request.user)
    #print(email,customer)
    #return render(request,"home.html")






class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "/"
        return path
    def get_signup_redirect_url(self, request):
        email= request.user.email
        customer,created=Customer.objects.get_or_create(email=email,user=request.user)
        print(email,customer)
        path = "/"
        return path
    
def intiprofile(request):
    
    return render(request,"home.html")