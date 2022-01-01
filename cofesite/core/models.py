from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls.base import reverse_lazy
from ckeditor.fields import RichTextField
# Create your models here.





class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=200)
    
    #def __str__(self) -> str:
        #return self.name
    
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    @property
    def get_products(self):
        return Item.objects.filter(Category__title=self.name)
    
class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    price=models.FloatField()
    category = models.ForeignKey(Category,related_name='Category', blank=True,default=None, on_delete = models.CASCADE)
    description=models.CharField(max_length=1000)
    image=models.ImageField(null=True,blank=True)
    def __str__(self) -> str:
        return self.title
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=' '
        return url
    
    class Meta:
        managed = True
        db_table = 'Item'  
                
class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    customer=models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return str(self.customer)
    @property
    def shipping(self):
        shipping=False
        orderitems=self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital==False:
                shipping=True
        return shipping

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_item(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product=models.ForeignKey(Item,null=True,on_delete=models.SET_NULL)
    category=models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    order=models.ForeignKey(Order,null=True,on_delete=models.SET_NULL)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total= self.product.price * self.quantity
        return total
    
    
    
    class Meta:
        managed = True
        db_table = 'OrderItem'    

class contact(models.Model):
    name=models.CharField(max_length=100, db_index=True,)
    email=models.EmailField(max_length=100, db_index=True)
    subject=models.CharField(max_length=100, db_index=True)
    message=models.TextField(max_length=1000, db_index=True)
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    firstname=models.CharField(max_length=50)
    secondname=models.CharField(max_length=50)
    date=models.DateField(auto_now=False, auto_now_add=False)
    time=models.TimeField(auto_now=False, auto_now_add=False)
    phone=models.IntegerField()
    

class blog(models.Model):
    title=models.CharField(max_length=256)
    header_image=models.ImageField(null=True,blank=True)
    title_tag=models.CharField(max_length=150)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=RichTextField(null=True,blank=True)
    post_date=models.DateField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    snippet=models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('blogs:testt')
    
    
    @property
    def imageURL(self):
        try:
            url=self.header_image.url
        except:
            url=' '
        return url
        
class shippingdetails(models.Model):
    firstname=models.CharField(max_length=50)
    secondname=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    StreetAddress=models.CharField(max_length=50)
    StreetAddress2=models.CharField(max_length=50,null=True,blank=True)
    Town_City=models.CharField(max_length=50)
    Postcode_ZIP=models.IntegerField()
    Phone=models.IntegerField()
    email=models.EmailField(max_length=254)
    