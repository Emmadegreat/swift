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
    red_oil_list = [('',''),('Quarter(0.25)','Quarter(0.25)'), ('Half(0.5)','Half(0.5)'),('1','1'),('2','2'),('No','No')]
    veg_oil_list = [('',''),('Quarter(0.25)','Quarter(0.25)'), ('Half(0.5)','Half(0.5)'),('1','1'),('2','2'),('No','No')]
    onions_list = [('',''),('Quarter(0.25)','Quarter(0.25)'), ('Half(0.5)','Half(0.5)'),('3-quarter(0.75)','3-quarter(0.75)'),('1', '1'), ('No','No')]
    #spaghetti_list = [('',''),('Half(0.5)','Half(0.5)'), ('1-Carton','1-Carton'), ('2-Cartons','2-Cartons'), ('3-Cartons','3-Cartons'),('No','No')]
    #noodle_list = [('',''),('1-carton','1-Carton'), ('2-Cartons','2-Cartons'),('3-Cartons','3-Cartons'),('No','No')]
    #yam_list = [('', ''), ('1', '1'), ('2', '2'), ('3', '3'), ('4','4'), ('5', '5'), ('6', '6'), ('7','7'), ('8', '8'),\
        #('9', '9'), ('10', '10'), ('11','11'), ('12','12'), ('13','13'), ('No','No'), ('not-available', 'not-available'), ]
    #tomatoe_satchet_list = [('',''),('1-carton','1-carton'),('2-cartons','2-cartons'),('3-cartons','3-cartons'),('No','No')]
    #tomatoe_list = [('',''),('Quarter(0.25)','Quarter(0.25)'),('Half(0.5)','Half(0.5)'),('1','1'),('2','2'),('No','No')]
    #semo_list = [('',''),('1-bag','1-bag'),('2-bag','2-bag'),('3-bag','3-bag'), ('No','No')]
    #duration_list = [('',''),('1st Quarter','1st Quarter'), ('2nd Quarter','2nd Quarter'), ('3rd Quarter','3rd Quarter'), ('4th Quarter','4th Quarter')]



    white_garri_ijebu = forms.ChoiceField(label='White-garri-Ijebu-₦66,000', choices=garri_list, widget=forms.Select(attrs={'class': 'form-control'}))
    white_garri_bendel = forms.ChoiceField(label='White-garri-Bendel-₦52,000', choices=garri_list, widget=forms.Select(attrs={'class': 'form-control'}))
    yellow_garri_bendel = forms.ChoiceField(label='Yellow-garri-bendel-₦52,000', choices=garri_list, widget=forms.Select(attrs={'class': 'form-control'}))
    nig_rice = forms.ChoiceField(label="Nigerian-rice-₦67,000", choices=rice_list, widget=forms.Select(attrs={'class':'form-control'}))
    foreign_rice_small_grain = forms.ChoiceField(label="Foreign-rice-small-grain:₦70,000", choices=rice_list, widget=forms.Select(attrs={'class':'form-control'}))
    foreign_rice_big_grain = forms.ChoiceField(label="Foreign-rice-big-grain:₦75,000", choices=rice_list, widget=forms.Select(attrs={'class':'form-control'}))
    honey_beans = forms.ChoiceField(label="Honey-beans:₦91,000", choices=beans_list, widget=forms.Select(attrs={'class':'form-control'}))
    drum_beans = forms.ChoiceField(label="Drum-beans:₦180,000", choices=beans_list, widget=forms.Select(attrs={'class':'form-control'}))
    pelebe_beans = forms.ChoiceField(label="Pelebe-beans:₦160,000", choices=beans_list, widget=forms.Select(attrs={'class':'form-control'}))
    red_oil = forms.ChoiceField(label="Red-oil:₦30,000-25L", choices=red_oil_list, widget=forms.Select(attrs={'class': 'form-control'}))
    veg_oil = forms.ChoiceField(label="Vegetable-oil:₦52,000-25L", choices=veg_oil_list, widget=forms.Select(attrs={'class': 'form-control'}))

    onions_big_size = forms.ChoiceField(label="Onions-big-size:₦45,000", choices=onions_list, widget=forms.Select(attrs={'class':'form-control'}))
    onions_gen_size = forms.ChoiceField(label="Onions-general-size:₦91,000", choices=onions_list, widget=forms.Select(attrs={'class':'form-control'}))
    #aunty_b_spag = forms.ChoiceField(label="Aunty-b-spaghetti",choices=spaghetti_list, widget=forms.Select(attrs={'class':'form-control'}))
    #g_penny_spag = forms.ChoiceField(label="Golden-penny-spaghetti",choices=spaghetti_list, widget=forms.Select(attrs={'class':'form-control'}))
    #crown_spag = forms.ChoiceField(label="Crown-spaghetti",choices=spaghetti_list, widget=forms.Select(attrs={'class':'form-control'}))
    #dangote_spag = forms.ChoiceField(label="Dangote-spaghetti",choices=spaghetti_list, widget=forms.Select(attrs={'class':'form-control'}))
    #indomie_oriental = forms.ChoiceField(label="Noodles-indomie-oriental", choices=noodle_list, widget=forms.Select(attrs={'class':'form-control'}))
    #indomie_chicken = forms.ChoiceField(label="Noodles-indomie-chicken", choices=noodle_list, widget=forms.Select(attrs={'class':'form-control'}))
    #chikki_noodles = forms.ChoiceField(label="Noodles-chikki-chicken", choices=noodle_list, widget=forms.Select(attrs={'class':'form-control'}))
    #mimee_noodles = forms.ChoiceField(label="Noodles-mimee-chicken", choices=noodle_list, widget=forms.Select(attrs={'class':'form-control'}))
    #satchet_tomatoe = forms.ChoiceField(label="Satchet-tomatoe", choices=tomatoe_satchet_list, widget=forms.Select(attrs={'class': 'form-control'}))
    #tin_tomatoe_220g = forms.ChoiceField(label="Tin-tomatoe-220g", choices=tomatoe_list, widget=forms.Select(attrs={'class': 'form-control'}))
    #tin_tomatoe_450g = forms.ChoiceField(label="Tin-tomatoe-450g", choices=tomatoe_list, widget=forms.Select(attrs={'class': 'form-control'}))
    #semo = forms.ChoiceField(label="Semo", choices=semo_list, widget=forms.Select(attrs={'class': 'form-control'}))
    #yam_tubers = forms.ChoiceField(label="Yam-tubers", choices=yam_list, widget=forms.Select(attrs={'class': 'form-control'}))
    #duration = forms.ChoiceField(label="Duration",choices=duration_list, widget=forms.Select(attrs={'class':'form-control'}))

    #user = forms.IntegerField(widget=forms.HiddenInput())

    '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['yam_tubers'].widget.attrs['disabled'] = True'''

    #def set_dynamic_choices(self, field_name, choices):
        #self.fields[field_name] = forms.ChoiceField(label=field_name,choices=choices,widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = UserItems
        fields = ('white_garri_ijebu', 'white_garri_bendel', 'yellow_garri_bendel', 'nig_rice', 'foreign_rice_small_grain', 'foreign_rice_big_grain','honey_beans',
                'drum_beans', 'pelebe_beans', 'red_oil','veg_oil', 'onions_big_size', 'onions_gen_size'
                )

    """('aunty_b_spag','g_penny_spag', 'crown_spag', 'dangote_spag',
    'indomie_oriental','indomie_chicken', 'chikki_noodles', 'mimee_noodles', 'satchet_tomatoe', 'tin_tomatoe_220g', 'tin_tomatoe_450g', 'semo','yam_tubers') """

