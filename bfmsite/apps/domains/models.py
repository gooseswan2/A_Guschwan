import bfmsite.settings
from django.db import models
from apps.products.models import Product
from django.forms.widgets import HiddenInput

from bfmsite import settings
from base64 import b64encode, b64decode
#from M2Crypto.EVP import Cipher
from django.utils.crypto import get_random_string


# Create your models here.
class Team(models.Model):
    team_name       =	models.CharField(max_length=75)
    short_name      =	models.CharField(max_length=4, unique=True)
    sport           =	models.CharField(max_length=40)

    class Meta:
       ordering = ['short_name']

    def __str__(self):
       return self.short_name

class Domain(models.Model):
    team =		models.ForeignKey(Team, on_delete=models.CASCADE)
    domain_name =	models.CharField(max_length=75)

    class Meta:
       unique_together = ('team', 'domain_name')

    def __str__(self):
       return self.domain_name

class BFName(models.Model):
    domain =            models.ForeignKey(Domain, on_delete=models.CASCADE)
    product =           models.ForeignKey(Product, on_delete=models.CASCADE)
    bfname =            models.CharField(max_length=40)

    class Meta:
       unique_together = ('domain', 'bfname')

    def __str__(self):
       return self.bfname + "@" + self.domain.domain_name

class Account(models.Model):
    customer =          models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bfname =            models.ForeignKey(BFName, on_delete=models.CASCADE)
    host_id =           models.CharField(max_length=40)
    host_password =     models.CharField(max_length=128)
    interests =         models.CharField(max_length=16)
    offer_code =        models.CharField(max_length=30)
    auto_renew =        models.BooleanField()

    def __str__(self):
        return self.bfname.bfname + '@' + self.bfname.domain.domain_name
    
    def save_password(self, clearpass):
        (self.host_password, self.interests)=self.encrypt_hpwd(clearpass) 
        self.save(update_fields=['host_password', 'interests'])
"""
    def encrypt_hpwd(self, clearpass):
        key=settings.SECRET_KEY
        iv=get_random_string(16)
        cipher=Cipher(alg='aes_256_cbc', key=key, iv=iv, op=1)
        v=cipher.update(clearpass) + cipher.final()
        del cipher
        return b64encode(v), iv

    def decrypt_hpwd(self, password):
        data=b64decode(password)
        cipher=Cipher(alg='aes_256_cbc', key=settings.SECRET_KEY, iv=self.interests, op=0)
        v=cipher.update(data) + cipher.final()
        del cipher
        return v
"""
