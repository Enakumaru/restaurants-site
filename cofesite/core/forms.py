from django import forms
from django.forms import ModelForm
from .models import contact,shippingdetails,Appointment,Customer


class Form(forms.ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'name','class':'form-control','id':'name'}))
    email = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'email','class':'form-control','id':'email'}))
    subject = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'subject','class':'form-control','id':'subject'}))
    message = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Message','class':'form-control','id':'message','cols':'30','rows':'7'}))
    class Meta:
        model = contact
        fields = ('name', 'email','subject', 'message')

class appointmss(forms.ModelForm):
    firstname = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'First Name','class':'form-control','id':'firstname'}))
    secondname= forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control','id':'secondname'}))
    date = forms.DateField(input_formats=['%m/%d/%Y'],label='',widget=forms.DateInput(attrs={'placeholder':'Date','class':'form-control appointment_date','id':'Date','autocomplete':'off'}))
    time = forms.TimeField(widget=forms.TextInput(attrs={'placeholder':'Time','class':'form-control appointment_time','id':'Time',}))
    phone=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Phone','class':'form-control','id':'phone',}))
    message = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Message','class':'form-control','id':'message','cols':'30','rows':'2'}))
    class Meta:
        model = Appointment
        fields = ('firstname', 'secondname','date', 'time','phone','message')
        
class appointmss2(forms.ModelForm):
    firstname = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'First Name','class':'form-control','id':'firstname2'}))
    secondname= forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control','id':'secondname2'}))
    date = forms.DateField(input_formats=['%m/%d/%Y'],label='',widget=forms.DateInput(attrs={'placeholder':'Date','class':'form-control appointment_date','id':'Date2' ,'autocomplete':'off'}))
    time = forms.TimeField(widget=forms.TextInput(attrs={'placeholder':'Time','class':'form-control appointment_time','id':'Time2',}))
    phone=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Phone','class':'form-control','id':'phone2',}))
    message = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Message','class':'form-control','id':'message2','cols':'30','rows':'2'}))
    class Meta:
        model = Appointment
        fields = ('firstname', 'secondname','date', 'time','phone','message')


class costomersdedatil(forms.ModelForm):
    name = forms.CharField(label='firstname',widget=forms.TextInput(attrs={'class':'form-control','id':'name','label':'firstname'}))
    email = forms.CharField(label='email',widget=forms.TextInput(attrs={'class':'form-control','id':'email'}))
    
    class Meta:
        model=Customer
        fields = ('name','email',)
    
    
        

        

class Shipping(forms.ModelForm):
    firstname = forms.CharField(label='firstname',widget=forms.TextInput(attrs={'class':'form-control','id':'firstname','label':'firstname'}))
    secondname = forms.CharField(label='secondname',widget=forms.TextInput(attrs={'class':'form-control','id':'secondname'}))
    State = forms.CharField(label='State',widget=forms.TextInput(attrs={'class':'form-control','id':'State'}))
    Country = forms.CharField(label='Country',widget=forms.TextInput(attrs={'class':'form-control','id':'Country'}))
    StreetAddress = forms.CharField(label='StreetAddress',widget=forms.TextInput(attrs={'class':'form-control','id':'StreetAddress','placeholder':"House number and street name"}))
    StreetAddress2 = forms.CharField(label='StreetAddress2',widget=forms.TextInput(attrs={'class':'form-control','id':'StreetAddress2','placeholder':"Appartment, suite, unit etc: (optional)"}))
    Town_City = forms.CharField(label='Town/City',widget=forms.TextInput(attrs={'class':'form-control','id':'Town_City'}))
    Postcode_ZIP = forms.CharField(label='Postcode/ZIP*',widget=forms.TextInput(attrs={'class':'form-control','id':'Postcode_ZIP'}))
    Phone = forms.CharField(label='Phone',widget=forms.TextInput(attrs={'class':'form-control','id':'Phone'}))
    email = forms.CharField(label='email',widget=forms.TextInput(attrs={'class':'form-control','id':'email'}))
    
    class Meta:
        model = shippingdetails
        fields = ('firstname', 'secondname','State', 'Country','StreetAddress','StreetAddress2','Town_City','Postcode_ZIP','Phone','email')
    pass