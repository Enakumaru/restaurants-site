from django.shortcuts import render,redirect
import requests
from .models import *
from .forms import *
from django.http import JsonResponse
import datetime
import json
from django.views.generic import TemplateView



def about(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        Blog=blog.objects.all().order_by('post_date')[:2]
        coffee= Item.objects.filter( category_id=1 )
        context={
            'coffee':coffee,
            'order':order,
            'blog':Blog
        }
        return render(request,"about.html",context)
        
    else:
        Blog=blog.objects.all().order_by('post_date')[:2]
        coffee= Item.objects.filter( category_id=1 )
        context={
            'coffee':coffee,
            'blog':Blog
        }
    return render(request,"home.html",context)
def blog_single(request,id):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        underBlog=blog.objects.all().order_by('post_date')[:2]
        Blogs = blog.objects.get(id = id)
        context = {'order':order,'blog':Blogs,'underblog':underBlog}
    else:
        underBlog=blog.objects.all().order_by('post_date')[:2]
        Blogs = blog.objects.get(id = id)
        context = {'blog':Blogs,'underblog':underBlog}
        
    return render(request,"blog-single.html",context)
def Blog(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        underBlog=blog.objects.all().order_by('post_date')[:2]
        Blog=blog.objects.all()
        context = {'order':order,'blog':Blog,'underblog':underBlog}
    else:
        underBlog=blog.objects.all().order_by('post_date')[:2]
        Blog=blog.objects.all()
        context = {'blog':Blog,'underblog':underBlog}
    return render(request,"blog.html",context)
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        item = order.orderitem_set.all()
        product = Item.objects.all()
        Blog=blog.objects.all().order_by('post_date')[:2]
        context = {'product':product,'order':order,'cartItem':item,'blog':Blog,}
        return render(request,"cart.html",context)
    else:
        return render(request,"account/login.html")
def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        item = OrderItem.objects.all()
        product = Item.objects.all()
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        Blog=blog.objects.all().order_by('post_date')[:2]
        form = Shipping(request.POST or None, request.FILES or None)
        data = {}
        if request.is_ajax():
            if form.is_valid():
                form.save()
                data['name'] = form.cleaned_data.get('name')
                data['status'] = 'ok'
                transaction_id = datetime.datetime.now().timestamp()
                order.transaction_id = transaction_id
                #total=request.POST['total']
                order.complete = True
                order.save()
                return JsonResponse(data)
        coffee= Item.objects.filter( category_id=1 )
        maindish= Item.objects.filter( category_id=2 )
        dessert = Item.objects.filter( category_id=3 )
        drinks= Item.objects.filter( category_id=4 )
        Starter= Item.objects.filter( category_id=5 )
        
        context = {
            'form': form,
            'order':order,
            'cartItem':item,
            'blog':Blog,
            'coffee':coffee,
            'maindish':maindish,
            'dessert': dessert,
            'drinks':drinks,
            'Starter':Starter,
         }
        return render(request,"checkout.html",context)
    else:
        
        return render(request,"account/login.html")
def Contact(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        Blog=blog.objects.all().order_by('post_date')[:2]
        form = Form(request.POST or None, request.FILES or None)
        data = {}
        if request.is_ajax():
            if form.is_valid():
                form.save()
                data['name'] = form.cleaned_data.get('name')
                data['status'] = 'ok'
                return JsonResponse(data)
            
        context = {
            'form': form,
            'order':order,
            'blog':Blog,
        }
    else:
        Blog=blog.objects.all().order_by('post_date')[:2]
        form = Form(request.POST or None, request.FILES or None)
        data = {}
        if request.is_ajax():
            if form.is_valid():
                form.save()
                data['name'] = form.cleaned_data.get('name')
                data['status'] = 'ok'
                return JsonResponse(data)
            
        context = {
            'form': form,
            'blog':Blog,
        }
        
    return render(request, 'contact.html', context)
def menu(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        Blog=blog.objects.all().order_by('post_date')[:2]
        categorys = Category.objects.all()
        coffee= Item.objects.filter( category_id=1 )
        maindish= Item.objects.filter( category_id=2 )
        dessert = Item.objects.filter( category_id=3 )
        drinks= Item.objects.filter( category_id=4 )
        Starter= Item.objects.filter( category_id=5 )
        form = appointmss(request.POST or None, request.FILES or None)
        data = {}
        if request.method == 'POST':
            if form.is_valid():
                firstname= form.cleaned_data.get('firstname')
                data["firstname"]=firstname
                data["status"]="ok"
                form.save()
                return JsonResponse(data)
        #a=categorys.get(pk=3)
        
        context={
            'form': form,
            'categorys': categorys,
            'coffee':coffee,
            'maindish':maindish,
            'dessert': dessert,
            'drinks':drinks,
            'Starter':Starter,
            'order':order,
            'blog':Blog,
            'item':Item,
            
        }
    else:
        Blog=blog.objects.all().order_by('post_date')[:2]
        categorys = Category.objects.all()
        coffee= Item.objects.filter( category_id=1 )
        maindish= Item.objects.filter( category_id=2 )
        dessert = Item.objects.filter( category_id=3 )
        drinks= Item.objects.filter( category_id=4 )
        Starter= Item.objects.filter( category_id=5 )
        form = appointmss(request.POST or None, request.FILES or None)
        data = {}
        if request.method == 'POST':
            if form.is_valid():
                firstname= form.cleaned_data.get('firstname')
                data["firstname"]=firstname
                data["status"]="ok"
                form.save()
                return JsonResponse(data)
        #a=categorys.get(pk=3)
        
        context={
            'form': form,
            'categorys': categorys,
            'coffee':coffee,
            'maindish':maindish,
            'dessert': dessert,
            'drinks':drinks,
            'Starter':Starter,
            'blog':Blog,
            
        }
    return render(request,"menu.html",context)
def product_single(request,id):
    if request.user.is_authenticated: 
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        Blog=blog.objects.all().order_by('post_date')[:2]
        product = Item.objects.get(id = id)
        relative = Item.objects.filter( category_id = product.category.id )
        context={'product': product,'relative':relative,'order':order,'blog':Blog,}
    else:
        Blog=blog.objects.all().order_by('post_date')[:2]
        product = Item.objects.get(id = id)
        relative = Item.objects.filter( category_id = product.category.id )
        context={'product': product,'relative':relative,'blog':Blog,}
    return render(request,"product-single.html",context)
def services(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        Blog=blog.objects.all().order_by('post_date')[:2]
        context={'order':order,
                 'blog':Blog,}
            
    else:
        Blog=blog.objects.all().order_by('post_date')[:2]
        context={
                 'blog':Blog,}
    return render(request,"services.html",context)
def shop(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        Blog=blog.objects.all().order_by('post_date')[:2]
        coffee= Item.objects.filter( category_id=1 )
        maindish= Item.objects.filter( category_id=2 )
        dessert = Item.objects.filter( category_id=3 )
        drinks= Item.objects.filter( category_id=4 )
        Starter= Item.objects.filter( category_id=5 )
        context={
            'coffee':coffee,
            'maindish':maindish,
            'dessert': dessert,
            'drinks':drinks,
            'Starter':Starter,
            'order':order, 
            'blog':Blog,
        }
    else:
        Blog=blog.objects.all().order_by('post_date')[:2]
        coffee= Item.objects.filter( category_id=1 )
        maindish= Item.objects.filter( category_id=2 )
        dessert = Item.objects.filter( category_id=3 )
        drinks= Item.objects.filter( category_id=4 )
        Starter= Item.objects.filter( category_id=5 )
        context={
            'coffee':coffee,
            'maindish':maindish,
            'dessert': dessert,
            'drinks':drinks,
            'Starter':Starter, 
            'blog':Blog,
        }
        
    return render(request,"shop.html",context)
def index(request):    
    if request.user.is_authenticated:   
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        Blog=blog.objects.all().order_by('post_date')[:3]
        coffee= Item.objects.filter( category_id=1 )
        maindish= Item.objects.filter( category_id=2 )
        dessert = Item.objects.filter( category_id=3 )
        drinks= Item.objects.filter( category_id=4 )
        form = appointmss(request.POST or None, request.FILES or None)
        form2 = appointmss2(request.POST or None, request.FILES or None)
        
        data = {}
        if request.method == 'POST':
            if form.is_valid():
                firstname= form.cleaned_data.get('firstname')
                data["firstname"]=firstname
                data["status"]="ok"
                form.save()
                return JsonResponse(data)
            if form2.is_valid():
                firstname= form2.cleaned_data.get('firstname')
                data["firstname"]=firstname
                data["status"]="ok"
                form2.save()
                return JsonResponse(data)
            else:
                print('form is not valid')
        context={
            'form': form,
            'form2': form2,
            'coffee':coffee,
            'maindish':maindish,
            'dessert': dessert,
            'drinks':drinks,
            'order':order,
            'blog':Blog,
        }
    else:
        Blog=blog.objects.all().order_by('post_date')[:3]
        coffee= Item.objects.filter( category_id=1 )
        maindish= Item.objects.filter( category_id=2 )
        dessert = Item.objects.filter( category_id=3 )
        drinks= Item.objects.filter( category_id=4 )
        form = appointmss(request.POST or None, request.FILES or None)
        form2 = appointmss2(request.POST or None, request.FILES or None)
        data = {}
        if request.method == 'POST':
            if form.is_valid():
                firstname= form.cleaned_data.get('firstname')
                data["firstname"]=firstname
                data["status"]="ok"
                form.save()
                return JsonResponse(data)
            if form2.is_valid():
                firstname= form2.cleaned_data.get('firstname')
                data["firstname"]=firstname
                data["status"]="ok"
                form2.save()
                return JsonResponse(data)
            print(form.errors)
        context={
            'form': form,
            'form2': form2,
            'coffee':coffee,
            'maindish':maindish,
            'dessert': dessert,
            'drinks':drinks,
            'blog':Blog,
        }
        
    return render(request,"index.html",context)
def main(request):
    customer=request.user.customer
    item = OrderItem.objects.all()
    product = Item.objects.all()
    order,created=Order.objects.get_or_create(customer=customer, complete=False)
    context = {'product':product,'order':order,'cartItem':item,'blog':Blog,}
    return render(request,'main.html',context)

def updatecart(request):
    if request.is_ajax():
        if request.method == 'POST':
            productID = request.POST['productID']
            categorieID=request.POST['categorieID']
            Action=request.POST['Action']
            quntity=request.POST['quntity']    
           # print(productID,categorieID,Action)          
            customer=request.user.customer
            product=Item.objects.get(id=productID,category_id=categorieID)
            order,created=Order.objects.get_or_create(customer=customer, complete=False)
            orderItem,created=OrderItem.objects.get_or_create(order=order, product=product,category_id=categorieID)
            
            if Action=='add':
                orderItem.quantity = (orderItem.quantity+1)
            elif Action=='remove':
                orderItem.delete()
            #print(orderItem.quantity)
            if orderItem.quantity <= 0 :
                orderItem.delete()
            orderItem.save()
    return JsonResponse('hello',safe=False)

def formms(request):
    form = appointmss(request.POST or None, request.FILES or None)
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request,"test.html",context)



def intiprofile(request):
    form = costomersdedatil(request.POST or None, request.FILES or None)
    data = {}
    if request.is_ajax():
            if form.is_valid():
                custo=form.save(commit=False)
                custo.user=request.user
                custo.save()
                data['name'] = form.cleaned_data.get('name')
                data['status'] = 'ok'
                name=form.cleaned_data.get('name')
                email=form.cleaned_data.get('email')
                return JsonResponse(data)
                
    context = {
        'form': form,
    }  
    return render(request,"home.html",context)


#<a class="dropdown-item" href="{% url 'core:product-single/<str:id>/' %}">Shop</a>



#appointment


#form = appointmss(request.POST or None, request.FILES or None)
    #data = {}
    #if request.method=="GET":
        #if form.is_valid():
           # firstname= form.cleaned_data.get('firstname')
           # data["firstname"]=firstname
           # secondname= form.cleaned_data.get('secondname')
          #  data["secondname"]=secondname
           # date= form.cleaned_data.get('date')
           # data["date"]=date
           # print(data)
       # else:
        #    print('form is not valid')
    #if request.method=="POST":
        #'firstname', 'secondname','date', 'time','phone','message'
        #firstname = request.POST['firstname']
        #secondname=request.POST['secondname']
        #date=request.POST['date']
        #print(firstname,secondname,date)
        #return JsonResponse(data)
        #if form.is_valid():
         #   form.save()
          #  data['name'] = form.cleaned_data.get('name')
           # data['status'] = 'ok'
            #return JsonResponse(data)
            #<!-- #{% for product in item|slice:":6" %}
	#{{product.get_products(coffee)}}
	#{% endfor%} -->