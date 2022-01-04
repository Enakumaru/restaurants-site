from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Category) 
admin.site.register(Customer)
admin.site.register(Appointment)
admin.site.register(blog)

class contactAdmin(SummernoteModelAdmin , admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name' ,'email', 'subject', 'message']
class orderitem(SummernoteModelAdmin , admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['product' ,'category', 'order', 'quantity','date_added','product_id',]    
class shipping(SummernoteModelAdmin , admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['firstname', 'email','Phone','State', 'Country','StreetAddress',]    


class Commenting(SummernoteModelAdmin , admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['post' ,'author', 'date_added']

admin.site.register(shippingdetails,shipping)    
admin.site.register(contact,contactAdmin)
admin.site.register(OrderItem,orderitem)
admin.site.register(Comments,Commenting)