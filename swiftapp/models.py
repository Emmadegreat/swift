from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField

# Create your models here.
class SwiftUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('You must provide an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_admin',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusers must have is_staff = True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_super = True')

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin = True')

        return self.create_user(email, password, **extra_fields)

class SwiftUser(AbstractUser):
    username = None
    email = models.CharField(max_length=225,unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(verbose_name="mobile number", max_length=11, blank=True)
    avatar = CloudinaryField("avater")
    last_login = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'phone','avatar', 'first_name', 'last_name']

    objects = SwiftUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True




class UserItems(models.Model):

    garri_list = [('',''),('Quarter','Quarter'), ('Half','Half'),('1-bag','1-bag'),('No','No')]
    rice_list = [('',''),('Quarter','Quarter'), ('Half','Half'),('1-bag','1-bag'),('No','No')]
    honey_beans_list = [('',''),('Quarter','Quarter'), ('Half','Half'),('1-bag','1-bag'),('No','No')]
    oloyin_beans_list = [('',''),('Quarter','Quarter'), ('Half','Half'),('1-bag','1-bag'),('No','No')]
    onions_list = [('',''),('1 pent','1 pent'), ('2 pent','2 pent'), ('Quarter bag','Quarter bag'), ('Half bag','Half bag'), ('1-bag','1-bag'),('No','No')]
    spaghetti_list = [('',''),('Half Carton','Half-Carton'), ('1-Carton','1-Carton'), ('2-Cartons','2-Cartons'), ('3-Cartons','3-Cartons'),('No','No')]
    indomie_list = [('',''),('Half Carton','Half-Carton'), ('1-Carton','1-Carton'), ('2-Cartons','2-Cartons'), ('3-Cartons','3-Cartons'),('No','No')]
    yam_list = [('', ''), ('1', '1'), ('2', '2'), ('3', '3'), ('4','4'), ('5', '5'), ('6', '6'), ('7','7'), ('8', '8'),('9', '9'), ('10', '10'), ('11','11'), ('12','12'), ('13','13'), ('14','14')]
    duration_list = [('',''),('1st Quarter','1st Quarter'), ('2nd Quarter','2nd Quarter'), ('3rd Quarter','3rd Quarter'), ('4th Quarter','4th Quarter')]

    user = models.OneToOneField('SwiftUser', on_delete=models.CASCADE)
    garri = models.CharField(choices=garri_list, null=True, blank=True, max_length=20)
    rice = models.CharField(choices=rice_list, null=True, blank=True, max_length=20)
    honey_beans = models.CharField(choices=honey_beans_list, null=True, blank=True, max_length=10)
    oloyin_beans = models.CharField(choices=oloyin_beans_list, null=True, blank=True, max_length=10)
    onions = models.CharField(choices=onions_list, null=True, blank=True, max_length=20)
    spaghetti = models.CharField(choices=spaghetti_list, null=True, blank=True, max_length=20)
    indomie = models.CharField(choices=indomie_list, null=True, blank=True, max_length=20)
    yam_tubers = models.CharField(choices=yam_list, null=True, blank=True, max_length=20)
    duration = models.CharField(choices=duration_list, null=True, blank=True, max_length=20)

    def __str__(self):
        return f"{self.user.email}- Yam: {self.yam_tubers}, Garri: {self.garri}, Rice: {self.rice}, Honey_beans: {self.honey_beans}, Oloyin_beans: {self.oloyin_beans},Onions: {self.onions}, Spagehetti: {self.spaghetti}, Indomie: {self.indomie}, Duration: {self.duration}"
