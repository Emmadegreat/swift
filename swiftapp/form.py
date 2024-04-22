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

    garri_list = [('',''),('Quarter(0.25)','Quarter(0.25)'), ('Half(0.5)','Half(0.5)'),('1-bag','1-bag'),('2-bag','2-bag'),('No','No')]
    rice_list = [('',''),('Quarter(0.25)','Quarter(0.25)'), ('Half(0.5)','Half(0.5)'),('1-bag','1-bag'),('2-bags','2-bags'),('No','No')]
    beans_list = [('',''),('Quarter(0.25)','Quarter(0.25)'), ('Half(0.5)','Half(0.5)'),('1-bag','1-bag'),('No','No')]
    onions_list = [('',''),('Quarter(0.25)','Quarter(0.25)'), ('Half(0.5)','Half(0.5)'),('3-quarter(0.75)','3-quarter(0.75)'),('1', '1'), ('No','No')]
    spaghetti_list = [('',''),('Half(0.5)','Half(0.5)'), ('1-Carton','1-Carton'), ('2-Cartons','2-Cartons'), ('3-Cartons','3-Cartons'),('No','No')]
    noodle_list = [('',''),('1-carton','1-Carton'), ('2-Carton','2-Carton'),('3-Cartons','3-Cartons'),('No','No')]
    yam_list = [('', ''), ('1', '1'), ('2', '2'), ('3', '3'), ('4','4'), ('5', '5'), ('6', '6'), ('7','7'), ('8', '8'),('9', '9'), ('10', '10'), ('11','11'), ('12','12'), ('13','13'), ('No','No')]
    duration_list = [('',''),('1st Quarter','1st Quarter'), ('2nd Quarter','2nd Quarter'), ('3rd Quarter','3rd Quarter'), ('4th Quarter','4th Quarter')]



    white_garri = forms.ChoiceField(label='White-garri', choices=garri_list, widget=forms.Select(attrs={'class': 'form-control'}))
    yellow_garri = forms.ChoiceField(label='White-garri', choices=garri_list, widget=forms.Select(attrs={'class': 'form-control'}))
    nig_rice = forms.ChoiceField(label="Nig-rice", choices=rice_list, widget=forms.Select(attrs={'class':'form-control'}))
    foreign_rice = forms.ChoiceField(label="foreign-rice", choices=rice_list, widget=forms.Select(attrs={'class':'form-control'}))
    honey_beans = forms.ChoiceField(label="Honey-beans", choices=beans_list, widget=forms.Select(attrs={'class':'form-control'}))
    drum_beans = forms.ChoiceField(label="Oloyin-beans", choices=beans_list, widget=forms.Select(attrs={'class':'form-control'}))
    onions = forms.ChoiceField(label="Onions", choices=onions_list, widget=forms.Select(attrs={'class':'form-control'}))
    aunty_b_spag = forms.ChoiceField(label="Aunty-B-spag",choices=spaghetti_list, widget=forms.Select(attrs={'class':'form-control'}))
    g_penny_spag = forms.ChoiceField(label="G-penny-spag",choices=spaghetti_list, widget=forms.Select(attrs={'class':'form-control'}))
    oriental_noodles = forms.ChoiceField(label="Oriental-noodles", choices=noodle_list, widget=forms.Select(attrs={'class':'form-control'}))
    chikki_noodles = forms.ChoiceField(label="Chikki-noodles", choices=noodle_list, widget=forms.Select(attrs={'class':'form-control'}))
    yam_tubers = forms.ChoiceField(label="Yam-tubers", choices=yam_list, widget=forms.Select(attrs={'class': 'form-control'}))
    duration = forms.ChoiceField(label="Duration",choices=duration_list, widget=forms.Select(attrs={'class':'form-control'}))

    #user = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = UserItems
        fields = ('yam_tubers', 'white_garri', 'yellow_garri', 'nig_rice', 'foreign_rice', 'honey_beans', 'drum_beans', 'onions',
                 'aunty_b_spag','g_penny_spag', 'oriental_noodles', 'chikki_noodles', 'duration'
                )