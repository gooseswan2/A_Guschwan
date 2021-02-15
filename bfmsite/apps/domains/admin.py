from django.contrib import admin
from apps.domains.models import Team, Domain, BFName, Account

# Register your models here.

admin.site.register(Team)
admin.site.register(Domain)
admin.site.register(BFName)
admin.site.register(Account)
