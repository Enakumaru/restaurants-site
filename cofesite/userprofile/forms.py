from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserChangeForm, UsernameField
from django.contrib.auth.models import User

from core.models import Customer
class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'placeholder':'First Name','class':'form-control','id':'firstname'}))
    last_name = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control','id':'lastname'}))

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # here you can change the fields
        self.fields['username']=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'username','class':'form-control','id':'username'}))
        self.fields['email']=forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder':'email','class':'form-control','id':'email'}))
        self.fields['password1']=forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control','id':'password1'}))
        self.fields['password2']=forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Re-type Password','class':'form-control','id':'password2'}))
        
    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        # You must return the original result.
        return user



class EditprofileForm(UserChangeForm):
    #password=forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control','id':'password'}))
    first_name= forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'placeholder':'First Name','class':'form-control','id':'firstname'}))
    last_name= forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control','id':'lastname'}))
    username=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'username','class':'form-control','id':'username'}))
    #last_login=forms.CharField(label='',widget=forms.TextInput(attrs={'value':'','class':'form-control',})),
    email = forms.CharField(label='email',widget=forms.TextInput(attrs={'class':'form-control','id':'email'}))
    #data_joined=forms.CharField(label='',widget=forms.TextInput(attrs={'value':'','class':'form-control',})),
    #is_superuser=forms.CharField(widget=forms.CheckboxInput(attrs={'placeholder':'username','class':'form-check','id':'is_superuser'}))
    #is_staff=forms.CharField(widget=forms.CheckboxInput(attrs={'placeholder':'username','class':'form-check','id':'is_staff'}))
    #is_active=forms.CharField(widget=forms.CheckboxInput(attrs={'placeholder':'username','class':'form-check','id':'is_active'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email',]

class costomersdedatil(forms.ModelForm):
    #name = forms.CharField(label='firstname',widget=forms.TextInput(attrs={'class':'form-control','id':'name','label':'firstname'}))
    #email = forms.CharField(label='email',widget=forms.TextInput(attrs={'class':'form-control','id':'email'}))
    profile_image=forms.ImageField(label='profile',widget=forms.FileInput(attrs={'class':'form-control','type':'file',}),)
    bio=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Add body'})),
    class Meta:
        model=Customer
        fields = ('profile_image','bio')   


    
    