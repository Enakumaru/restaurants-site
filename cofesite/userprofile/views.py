from django.db.models import fields
from django.db.models.base import Model
from django.http import request
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic.base import TemplateView
from django.views.generic import ListView,CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import BaseUpdateView, FormMixin, ModelFormMixin
from userprofile.forms import EditprofileForm,costomersdedatil
from core.models import *
from allauth.account.views  import SignupView
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib import messages
def profile(request):
    
    
    context = {
        
        
    }
    return render(request,'profile/profile.html',context)

class profileView(DetailView):
    model=Customer
    template_name='profile/profile.html'
    
    
    def get_context_data(self, **kwargs):
        context = super(profileView,self).get_context_data(**kwargs)
        page_user=get_object_or_404(Customer,id=self.kwargs['pk'])
        order_id=Order.objects.filter(customer_id=self.kwargs['pk']).values_list('id', flat=True)
        l=[]
        for i in order_id:
            
            orderitem=OrderItem.objects.filter(order_id=i)
            l.append(orderitem)
        for i in l:
            print(i.values())
        context["page_user"] = page_user 
        context["orderitem"] = l[::-1]
        return context
    #, flat=True
    
    
class orderHistory(DetailView):
    model=Order
    template_name='profile/orderHistory.html'
    
    def get_context_data(self, **kwargs):
        context = super(orderHistory,self).get_context_data(**kwargs)
        order_id=Order.objects.filter(customer_id=self.kwargs['pk']).values_list('id', flat=True)
        l=[]
        for i in order_id:
            orderitem=OrderItem.objects.filter(order_id=i)
            l.append(orderitem)
        for i in l:
            print(i.values())
        context["orderitem"] = l[::-1]
        return context
    
class edit_userSetting(UpdateView):
    form_class=EditprofileForm
    template_name='profile/editprofile.html'
    success_url=reverse_lazy('core:index')
    print(form_class.errors)
    def get_object(self):
        return self.request.user
    
class edit_Customer(UpdateView):
    model=Customer
    fields='__all__'
    #form_class=costomersdedatil
    template_name='profile/test.html'
    success_url=reverse_lazy('core:index')
    
class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "/"
        return path
    def get_signup_redirect_url(self, request):
        email= request.user.email
        name=request.user.first_name+' '+request.user.last_name
        customer,created=Customer.objects.get_or_create(email=email,user=request.user,name=name)
        print(email,customer)
        path = "/"
        return path

class tet(UpdateView):
    model=Customer
    form_class=costomersdedatil
    second_form_class =EditprofileForm
    template_name='profile/test2.html'
    success_url=reverse_lazy('core:index')
    def get_object(self):
        return self.request.user
    def get_context_data(self, **kwargs):
        context = super(tet, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(instance=self.request.user.customer)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=self.request.user)
        context['form'] = self.form_class(instance=self.request.user.customer)
        context['form2'] = self.second_form_class(instance=self.request.user)
        return context
    def get(self, request, *args, **kwargs):
        super(tet, self).get(request, *args, **kwargs)
        form = self.form_class
        form2 = self.second_form_class
        return self.render_to_response(self.get_context_data(
            object=self.object, form=form, form2=form2))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'POST':
            form = self.form_class(request.POST,instance=self.request.user.customer,files=request.FILES)
            form2 = self.second_form_class(request.POST,instance=self.request.user)
            
            if form.is_valid() and form2.is_valid():
                userdata = form.save(commit=False)
                name= form2.cleaned_data.get('first_name')+' '+form2.cleaned_data.get('last_name')
                image=form.cleaned_data['profile_image']
                userdata.name=name
                userdata.profile_image=image
                userdata.save()
                print(name)
                form2.save()
                
                
                messages.success(self.request, 'Settings saved successfully')
                return HttpResponseRedirect(self.get_success_url())
            else:
                return self.render_to_response(
                self.get_context_data(form=form, form2=form2))
    def get_success_url(self):
        return reverse_lazy('core:index')
    
    
    
