from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.core.validators import EmailValidator

# Create your forms here
class Registration_Form(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder' : 'Enter Your Password'}), required=False)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder' : 'Confirm Your Password'}), required=False)
    
    def __init__(self, *args, **kwargs):
        super(Registration_Form, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields.get('username').required = False
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
        }

        widgets = {
            'username' : forms.TextInput(attrs={'placeholder' : 'Username'}),
            'first_name' : forms.TextInput(attrs={'placeholder' : 'First Name'}),
            'last_name' : forms.TextInput(attrs={'placeholder' : 'Last Name'}),
            'email' : forms.TextInput(attrs={'placeholder' : 'Email'}),
        }

        help_texts = {
            'username' : "You can keep it same as your email!",
        }

    def clean_username(self):
        inp_username = self.cleaned_data.get('username')
        if len(inp_username) == 0:
            raise ValidationError(_("Please Enter Username!"))
        return inp_username

    def clean_first_name(self):
        inp_first_name = self.cleaned_data.get('first_name')
        if len(inp_first_name) == 0:
            raise ValidationError(_("Please Enter First Name!"))
        return inp_first_name

    def clean_last_name(self):
        inp_last_name = self.cleaned_data.get('last_name')
        if len(inp_last_name) == 0:
            raise ValidationError(_("Please Enter Last Name!"))
        return inp_last_name

    def clean_email(self):
        inp_email = self.cleaned_data.get('email')
        if len(inp_email) == 0:
            raise ValidationError(_("Please Enter Email!"))
        validator = EmailValidator(_("Please Enter Valid Email!")) 
        validator(inp_email)
        if User.objects.filter(email=inp_email, is_active=True).exists():
            raise ValidationError(_(f"{inp_email} Already Exists!"))
        return inp_email

    def clean_password1(self):
        inp_password1 = self.cleaned_data.get('password1')
        if len(inp_password1) == 0:
            raise ValidationError(_("Please Enter Password!"))
        if len(inp_password1) < 8:
            raise ValidationError(_("Password Must Be of 8 Characters!"))
        return inp_password1

    def clean_password2(self):
        inp_password1 = self.data.get('password1')
        inp_password2 = self.cleaned_data.get('password2')
        if len(inp_password2) == 0:
            raise ValidationError(_("Please Confirm Your Password!"))
        if inp_password1 != inp_password2:
            raise ValidationError(_("Password and Confirm Password Must Matched!"))
        return inp_password2


class Login_Form(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder' : 'Username'}), required=False)
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder' : "Password"}),required=False
    )
    
    def clean_username(self):
        inp_username = self.cleaned_data.get('username')
        if len(inp_username) == 0:
            raise ValidationError(_("Please Enter Username!"))
        return inp_username

    def clean_password(self):
        inp_password = self.cleaned_data.get('password')
        if len(inp_password) == 0:
            raise ValidationError(_("Please Enter Password!"))
        return inp_password
