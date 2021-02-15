from django.contrib import admin
from .models import BFCustomer, SecurityQuestion, CustomerAnswer

# Register your models here.

admin.site.register(BFCustomer)
admin.site.register(SecurityQuestion)
admin.site.register(CustomerAnswer)

