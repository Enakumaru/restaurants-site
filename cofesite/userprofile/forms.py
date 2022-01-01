from django import forms
from allauth.account.forms import SignupForm

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


#class Meta:
#        model = Profile
#        fields = ('first_name', 'last_name', 'nationality', 'bio')