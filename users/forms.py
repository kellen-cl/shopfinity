#users/forms.py
from django import forms
from. models import User #import your custom user model
from django.contrib.auth.hashers import make_password , check_password # for password hashing
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput ,label="Password")
    password2=forms.CharField(widget=forms.PasswordInput ,label="Confirm Password")

    class Meta:
        model= User
        fields=['first_name' , 'last_name' , 'username' , 'email' ] #remove password from fields as it will be handled by set password function in save()
        widgets={
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
        }

    #NB :Remove the clean_password method entirely!
    #def clean password(self):
    #   password =self.cleaned_data['password']
    #    # Your logic for not rehashing is now irrelevant for registration.
    #    # For registration ,it should just return the plain password or raise validation errors on strength
    # return make_password(password) # THIS WAS THE CULPRIT!

    def clean(self):
        '''
        Custom clean method for cross field validation (eg ., password matching)
        This method runs after individual field methods
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            self.add_error('password2', 'Passwords do not match')# add error to password2 field 

        #you can add other crossfield validations here if needed 

        return cleaned_data #always return cleaned data from the clean method
    
    def save(self , commit=True):
        '''
        Save method to create the user with a hashed password 
        '''
        User = super().save(commit=False)#get the user instance but don't save to the database yet
        password=self.cleaned_data['password']#get the plain text data from cleaned data
        User.set_password(password) #hash and set the password using user model method (from AbstarctBaseUser)

        if commit:
            User.save()#save the user to the database
        return User
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #this part is for editing existing users , not directly for signup
        #If the form is used for profile editing where password is optional
        if self.instance and self .instance.pk:
            self.fields['password'].required = False
            self.fields['password2'].required = False# confirm password also not on edit 

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # your custom user model
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']