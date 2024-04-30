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


    #def save(self, *args, **kwargs):
        #super().save(*args, **kwargs)
        #if self.is_superuser:
            #ShowElement.objects.update_or_create(defaults={'are_visible': self.toggle_status})


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'phone','avatar', 'first_name', 'last_name']

    objects = SwiftUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


#class ShowElement(models.Model):
    #are_visible = models.BooleanField(default=False)

class UserItems(models.Model):

    garri_list = [('',''),('Quarter(0.25)','Quarter(0.25)'), ('Half(0.5)','Half(0.5)'),('1-bag','1-bag'),('2-bag','2-bag'),('No','No')]
    rice_list = [('',''),('Quarter(0.25)','Quarter(0.25)'), ('Half(0.5)','Half(0.5)'),('1-bag','1-bag'),('2-bags','2-bags'),('No','No')]
    beans_list = [('',''),('Quarter(0.25)','Quarter(0.25)'), ('Half(0.5)','Half(0.5)'),('1-bag','1-bag'),('No','No')]
    onions_list = [('',''),('Quarter(0.25)','Quarter(0.25)'), ('Half(0.5)','Half(0.5)'),('3-quarter(0.75)','3-quarter(0.75)'),('1', '1'), ('No','No')]
    spaghetti_list = [('',''),('Half(0.5)','Half(0.5)'), ('1-Carton','1-Carton'), ('2-Cartons','2-Cartons'), ('3-Cartons','3-Cartons'),('No','No')]
    noodle_list = [('',''),('1-carton','1-Carton'), ('2-Cartons','2-Cartons'),('3-Cartons','3-Cartons'),('No','No')]
    #yam_list = [('', ''), ('1', '1'), ('2', '2'), ('3', '3'), ('4','4'), ('5', '5'), ('6', '6'), \
        #('7','7'), ('8', '8'),('9', '9'), ('10', '10'), ('11','11'), ('12','12'), ('13','13'), ('No','No'), ('not-available', 'not-available')]
    red_oil_list = [('',''),('Quarter(0.25)','Quarter(0.25)'), ('Half(0.5)','Half(0.5)'),('1','1'),('2','2'),('No','No')]
    veg_oil_list = [('',''),('Quarter(0.25)','Quarter(0.25)'), ('Half(0.5)','Half(0.5)'),('1','1'),('2','2'),('No','No')]
    tomatoe_satchet_list = [('',''),('1-carton','1-carton'),('2-cartons','2-cartons'),('3-cartons','3-cartons'),('No','No')]
    tomatoe_list = [('',''),('Quarter(0.25)','Quarter(0.25)'),('Half(0.5)','Half(0.5)'),('1','1'),('2','2'),('No','No')]
    semo_list = [('',''),('1-bag','1-bag'),('2-bag','2-bag'),('2-bag','2-bag'), ('No','No')]
    #duration_list = [('',''),('1st Quarter','1st Quarter'), ('2nd Quarter','2nd Quarter'), ('3rd Quarter','3rd Quarter'), ('4th Quarter','4th Quarter')]

    user = models.OneToOneField('SwiftUser', on_delete=models.CASCADE)
    white_garri_ijebu = models.CharField(choices=garri_list, null=True, blank=True, max_length=40)
    white_garri_bendel = models.CharField(choices=garri_list, null=True, blank=True, max_length=40)
    yellow_garri = models.CharField(choices=garri_list, null=True, blank=True, max_length=40)
    nig_rice = models.CharField(choices=rice_list, null=True, blank=True, max_length=40)
    foreign_rice_small_grain = models.CharField(choices=rice_list, null=True, blank=True, max_length=40)
    foreign_rice_big_grain = models.CharField(choices=rice_list, null=True, blank=True, max_length=40)
    honey_beans = models.CharField(choices=beans_list, null=True, blank=True, max_length=40)
    drum_beans = models.CharField(choices=beans_list, null=True, blank=True, max_length=40)
    pelebe_beans = models.CharField(choices=beans_list, null=True, blank=True, max_length=40)
    onions_big_size = models.CharField(choices=onions_list, null=True, blank=True, max_length=40)
    onions_gen_size = models.CharField(choices=onions_list, null=True, blank=True, max_length=40)
    aunty_b_spag = models.CharField(choices=spaghetti_list, null=True, blank=True, max_length=40)
    g_penny_spag = models.CharField(choices=spaghetti_list, null=True, blank=True, max_length=40)
    crown_spag = models.CharField(choices=spaghetti_list, null=True, blank=True, max_length=40)
    dangote_spag = models.CharField(choices=spaghetti_list, null=True, blank=True, max_length=40)
    indomie_oriental = models.CharField(choices=noodle_list, null=True, blank=True, max_length=40)
    indomie_chicken = models.CharField(choices=noodle_list, null=True, blank=True, max_length=40)
    chikki_noodles = models.CharField(choices=noodle_list, null=True, blank=True, max_length=40)
    mimee_noodles = models.CharField(choices=noodle_list, null=True, blank=True, max_length=40)
    #yam_tubers = models.CharField(choices=yam_list, null=True, blank=True, default='', max_length=40)
    red_oil = models.CharField(choices=red_oil_list, null=True, blank=True, max_length=40)
    veg_oil = models.CharField(choices=veg_oil_list, null=True, blank=True, max_length=40)
    satchet_tomatoe = models.CharField(choices=tomatoe_satchet_list, null=True, blank=True, max_length=40)
    tin_tomatoe_220g = models.CharField(choices=tomatoe_list, null=True, blank=True, max_length=40)
    tin_tomatoe_450g = models.CharField(choices=tomatoe_list, null=True, blank=True, max_length=40)
    semo = models.CharField(choices=semo_list, null=True, blank=True, max_length=40)
    #duration = models.CharField(choices=duration_list, null=True, blank=True, max_length=40)



    def __str__(self):
        return (
            f"{self.user.email}- White_garri_ijebu: {self.white_garri_ijebu}, White_garri_bendel: {self.white_garri_bendel},"
            f"Yellow_garri: {self.yellow_garri}, Nig_rice: {self.nig_rice},Red_oil: {self.red_oil}, Foreign_rice_small_grain: {self.foreign_rice_small_grain},"
            f"Foreign_rice_big_grain: {self.foreign_rice_big_grain},Honey_beans: {self.honey_beans}, Drum_beans: {self.drum_beans},""Pelebe_beans:{self.pelebe_beans},"
            f"Onions_big_size: {self.onions_big_size}, Onions_gen_size: {self.onions_gen_size}, Satchet_tomatoe: {self.satchet_tomatoe}, Tin_tomatoe_220g: {self.tin_tomatoe_220g},"
            f"Tin_tomatoe_450g: {self.tin_tomatoe_450g},Aunty_B_Spag: {self.aunty_b_spag}, G_penny_Spag: {self.g_penny_spag}, Crown_Spag: {self.crown_spag},"
            f"dangote_Spag: {self.dangote_spag}, Semo: {self.semo}, Indomie_oriental: {self.indomie_oriental}, Indomie_chicken: {self.indomie_chicken},"
            f"Chikki_noodles: {self.chikki_noodles}, Mimee_noodles: {self.mimee_noodles}"
        )