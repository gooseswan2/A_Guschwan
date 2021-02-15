# Create your models here.
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django_localflavor_us.models import USStateField
from bfmsite import settings


class BFCustomerManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None):
        if not email:
           raise ValueError('Users must have an email address')
        print(last_name)
        user = self.model(
            username=self.normalize_email(username),
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password=None):
        user = self.create_user(username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user_is_admin = True
        user.save(using=self._db)
        return user

# Create your models here.
class BFCustomer(AbstractBaseUser, PermissionsMixin):
    username =	        models.CharField(max_length=75,unique=True,db_index=True)
    email =	        models.EmailField(max_length=100, unique=True)
    first_name =	models.CharField(max_length=30)
    last_name =		models.CharField(max_length=40)
    add1 =		models.CharField(verbose_name="Address1", max_length=50, null=True, blank=True)
    add2 =  		models.CharField(verbose_name="Address2", max_length=50,null=True,blank=True)
    city =  		models.CharField(max_length=40, null=True, blank=True)
    state = 		USStateField(null=True, blank=True)
    zipcode =		models.CharField(verbose_name= "Zip code", max_length=10, null=True,blank=True)
    signup_date = 	models.DateTimeField(auto_now_add=True)
    is_active =         models.BooleanField(default=True)
    is_admin =          models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    objects = BFCustomerManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class SecurityQuestion(models.Model):
    question =     models.CharField(max_length=150)

    def __str__(self):
        return self.question

class CustomerAnswer(models.Model):
    customer =                  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    security_question =         models.ForeignKey(SecurityQuestion, on_delete=models.CASCADE)
    answer =                    models.CharField(max_length=75)
