from django.urls import include, path, re_path
from django.views.generic import TemplateView
from apps.customers.forms import UserRegistrationForm
from django.conf.urls import include, url
from django.contrib.auth.forms import PasswordChangeForm 
import bfmsite.regbackend
import django_registration
from . import views
from apps.customers.views import subscribe, get_host_password, registration_complete, editusers, saveusers, save_emailpassword, editacct, save_account 
from django_registration.backends.activation.views import RegistrationView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [ 
    # Examples:
     path(r'findyourteam/', bfmsite.views.findyourteam, {}),
     path(r'bflogout/', views.bflogout, {}),
     path(r'bflogin/', views.bflogin, {}),
     path(r'bfsearch/', views.teamview, {}),
    # register https always:
     path(r'accounts/register/', RegistrationView.as_view(form_class=UserRegistrationForm), name='django_registration_register',),
     path(r'accounts/', include('django_registration.backends.activation.urls')),
     #path(r'^register/$', django_registration.views.register, {'backend': 'registration.backends.simple.SimpleBackend', 'form_class': UserRegistrationForm }, name='registration_register'),
     re_path(r'register/teampage/(?P<team>\w+)/', views.teamview,{} ),
     path(r'register/username_search/', views.bfname_usersearch, {}),
     path(r'register/bfsubscribe/', subscribe),
     path(r'register/get_host_password/', get_host_password),
     path(r'register/registration_complete/', registration_complete,{'bfemail':'bfemail'},name='registration_complete'),
     path(r'profile/', views.users, ),
     path(r'editprofile/', editusers, ),
     re_path(r'editaccount/(?P<idno>\d+)/', editacct, ),
     path(r'saveprofile/', saveusers, ),
     path(r'savepassword/', save_emailpassword, ),
     path(r'saveaccount/', save_account, ),
     path(r'forgotpassword/', views.forgotpassword, ),
     path(r'features/', TemplateView.as_view(template_name="features.html")),
     path(r'partners/', TemplateView.as_view(template_name="partners.html")),
     path(r'support/', TemplateView.as_view(template_name="support/support.html")),
     path(r'terms/', TemplateView.as_view(template_name="terms.html")),
     path(r'privacy/', TemplateView.as_view(template_name="privacy.html")),
     path(r'passwordchange/', views.changepassword, {}),
     #path(r'^passwordform/$', 'django.contrib.auth.views.password_change', {'template_name': 'django_registration/password_change_form.html', 'post_change_redirect': '/passwordchange/'}),
     path(r'username_registration/', views.bfname_registration),#, {'template_name': 'search/username_registration.html'}),

    #These are the team page urls
     #path(r'^payments/', include('payments.urls')),
     path(r'registration_complete/', registration_complete, {}),
     #path(r'^testregform/', 'bfmsite.test.regcom'),
     #path(r'^testhash/', 'bfmsite.test.testhash'),

     #path(r'^admin/doc/', include(django.contrib.admindocs.urls)),
     path(r'admin/', admin.site.urls),
     re_path(r'(?P<group>\w+)/', views.sports, ),
     path(r'', views.homepage, ),
]
