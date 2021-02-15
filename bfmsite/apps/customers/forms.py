from django_registration.forms import RegistrationForm
from django import forms
from localflavor.us.forms import USStateSelect, USZipCodeField
from apps.customers.models import BFCustomer, SecurityQuestion
from django.contrib.auth.hashers import make_password

class UserRegistrationForm(RegistrationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField(required=True)
    add1 = forms.CharField(label='Address1', required=False)
    add2 = forms.CharField(label='Address2', required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(widget=USStateSelect(),required=False)
    #zipcode = USZipCodeField(label='Zip code',required=False)
    zipcode = forms.CharField(max_length=5, min_length=5)
    sec_question1 = forms.ModelChoiceField(label='Security question1',queryset=SecurityQuestion.objects.all())
    sec_answer1 = forms.CharField(label='Security answer1',)
    #sec_question2 = forms.ModelChoiceField(label='Security question2',queryset=SecurityQuestion.objects.all())
    #sec_answer2 = forms.CharField(label='Security answer2',)

    def clean_password1(self):
        password = self.cleaned_data['password1']
        if len(password) < 6:
            raise forms.ValidationError('Password has to be at least 6 characters long.')
        return password

    def add_fields(self, request, bfname="", domainname=""):
       if request.method == 'GET':
          self.fields['bfname'] = forms.CharField(initial=bfname,widget=HiddenInput)
       else:
          self.fields['bfname'] = forms.CharField(initial=request.POST['bfname'],widget=HiddenInput)

       if request.method == 'GET':
          self.fields['domainname'] = forms.CharField(initial=domainname,widget=HiddenInput)
       else:
          self.fields['domainname'] = forms.CharField(initial=request.POST['domainname'],widget=HiddenInput)

       if request.method == 'GET':
          plan = request.GET['plan']
          self.fields['plan'] = forms.CharField(initial=plan,widget=HiddenInput)
       else:
          self.fields['plan'] = forms.CharField(initial=request.POST['plan'],widget=HiddenInput)

    class Meta:
        model = BFCustomer
        fields = ["username", "first_name", "last_name", "add1", "add2", "city", "state", "zipcode", "is_active", "is_admin"]
