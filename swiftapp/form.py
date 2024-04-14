from django import forms
from django.contrib.auth.forms import UserCreationForm
from swiftapp.models import SwiftUser, UserItems
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib import messages


class RegistrationForm(UserCreationForm):
    username = None
    email = forms.EmailField(label="Email", max_length=225, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone Number', max_length=11, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(label='Profile Picture', widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = SwiftUser
        fields = ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'avatar')

        error_messages = {
            'avatar':{'required':'Please Upload your profile picture'},

            'first_name':{'required':'Fill in your first name'},

            'last_name':{'required':'Fill in your last name'},

            'email':{'required':' Enter your email address'},

            'phone':{'required':' Enter your phone number'},

            'password1':{'required':' Password field is required'},

            'password2':{'required':' Confirm Password field is required'},
        }


class LoginForm(forms.ModelForm):
    email = forms.EmailField(label="Email", max_length=225, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Password", max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = SwiftUser
        fields = ('email','password')


    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise ValidationError('Invalid credentials, wrong password or email')



    '''def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not authenticate(email=email, password=password):
            raise ValidationError('Invalid credentials, wrong password or email')
        return cleaned_data'''


class UserItemForm(forms.ModelForm):

    garri_list = [('',''),('Quarter','Quarter'), ('Half','Half'),('1-bag','1-bag'),('No','No')]
    rice_list = [('',''),('Quarter','Quarter'), ('Half','Half'),('1-bag','1-bag'),('No','No')]
    honey_beans_list = [('',''),('Quarter','Quarter'), ('Half','Half'),('1-bag','1-bag'),('No','No')]
    oloyin_beans_list = [('',''),('Quarter','Quarter'), ('Half','Half'),('1-bag','1-bag'),('No','No')]
    onions_list = [('',''),('1 pent','1 pent'), ('2 pent','2 pent'), ('Quarter bag','Quarter bag'), ('Half bag','Half bag'), ('1-bag','1-bag'),('No','No')]
    spaghetti_list = [('',''),('Half Carton','Half-Carton'), ('1-Carton','1-Carton'), ('2-Cartons','2-Cartons'), ('3-Cartons','3-Cartons'),('No','No')]
    indomie_list = [('',''),('Half Carton','Half-Carton'), ('1-Carton','1-Carton'), ('2-Cartons','2-Cartons'), ('3-Cartons','3-Cartons'),('No','No')]
    duration_list = [('',''),('1st Quarter','1st Quarter'), ('2nd Quarter','2nd Quarter'), ('3rd Quarter','3rd Quarter'), ('4th Quarter','4th Quarter')]

    garri = forms.ChoiceField(label='Garri', choices=garri_list, widget=forms.Select(attrs={'class': 'form-control'}))
    rice = forms.ChoiceField(label="Rice", choices=rice_list, widget=forms.Select(attrs={'class':'form-control'}))
    honey_beans = forms.ChoiceField(label="Honey-Beans", choices=honey_beans_list, widget=forms.Select(attrs={'class':'form-control'}))
    oloyin_beans = forms.ChoiceField(label="Oloyin-Beans", choices=oloyin_beans_list, widget=forms.Select(attrs={'class':'form-control'}))
    onions = forms.ChoiceField(label="Onions", choices=onions_list, widget=forms.Select(attrs={'class':'form-control'}))
    spaghetti = forms.ChoiceField(label="Spaghetti",choices=spaghetti_list, widget=forms.Select(attrs={'class':'form-control'}))
    indomie = forms.ChoiceField(label="Indomie", choices=indomie_list, widget=forms.Select(attrs={'class':'form-control'}))
    duration = forms.ChoiceField(label="Duration",choices=duration_list, widget=forms.Select(attrs={'class':'form-control'}))

    #user = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = UserItems
        fields =('garri', 'rice', 'honey_beans', 'oloyin_beans', 'onions', 'spaghetti','indomie', 'duration')