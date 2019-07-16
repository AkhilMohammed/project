
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,password=None,is_staff=False,is_admin=False):
        if not email:
            raise ValueError('user must have email address')
        user_obj=self.model(
        email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff=is_staff
        user_obj.admin=is_admin
        user_obj.save(using=self._db)
        return user_obj
    def create_staffuser(self,email,password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self,email,password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    first_name =  models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    active = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)
    staff=models.BooleanField(default=False)
    object=UserManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True


    @property
    def is_staff(self):
        return self.staff,

    @property
    def is_active(self):
        return self.active,

    @property
    def is_admin(self):
        return self.admin,
class city(models.Model):

    id=models.IntegerField(primary_key=True)

    city=models.CharField(max_length=35,)

    countrycode=models.CharField(max_length=3)

    district=models.CharField(max_length=20)

    population=models.IntegerField(default='0')




class country(models.Model):

    code = models.CharField(max_length=3,primary_key=True)

    name = models.CharField(max_length=53)

    continent  = models.CharField(max_length=30)

    region = models.CharField(max_length=50)

    surfaceare = models.DecimalField(max_digits=10,decimal_places=4)

    independentyear = models.IntegerField()

    population = models.IntegerField()

    lifeexpectancy = models.DecimalField(max_digits=50,decimal_places=3)

    gnp = models.DecimalField(max_digits=50,decimal_places=2)

    gnpld = models.DecimalField(max_digits=10,decimal_places=3)

    localname = models.CharField(max_length=50)

    govname = models.CharField(max_length=45)

    headofstat= models.CharField(max_length=60)

    capital = models.IntegerField()

    code2 = models.CharField(max_length=3)

class countrylanguage(models.Model):
    code = models.CharField(max_length=3,primary_key=True)
    language = models.CharField(max_length=60)
    isofficial = models.BooleanField(default=True)
    percentage = models.DecimalField(max_digits=10,decimal_places=2)


