from django.conf import settings

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User

from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox



class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input mb-1', 'placeholder': 'Email'}))

    RECAPTCHA_PUBLIC_KEY = getattr(settings, "RECAPTCHA_PUBLIC_KEY", None)
    RECAPTCHA_PRIVATE_KEY = getattr(settings, "RECAPTCHA_PRIVATE_KEY", None)
    captcha = ReCaptchaField(public_key=RECAPTCHA_PUBLIC_KEY, private_key=RECAPTCHA_PRIVATE_KEY , widget=ReCaptchaV2Checkbox)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "captcha", ]

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input mb-1'
        self.fields['password1'].widget.attrs['class'] = 'input mb-1'
        self.fields['password2'].widget.attrs['class'] = 'input mb-3'

        self.fields['username'].widget.attrs['placeholder'] = ''
        self.fields['email'].widget.attrs['placeholder'] = ''


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'input mb-1', 'placeholder': ''}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input mb-1', 'placeholder': ''}))
    
    RECAPTCHA_PUBLIC_KEY = getattr(settings, "RECAPTCHA_PUBLIC_KEY", None)
    RECAPTCHA_PRIVATE_KEY = getattr(settings, "RECAPTCHA_PRIVATE_KEY", None)
    captcha = ReCaptchaField(public_key=RECAPTCHA_PUBLIC_KEY, private_key=RECAPTCHA_PRIVATE_KEY , widget=ReCaptchaV2Checkbox)


    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='Forgot your password?', widget=forms.EmailInput(attrs={'class': 'input mb-1','placeholder': 'Email', 'type': 'email', 'name': 'email'}) )

    RECAPTCHA_PUBLIC_KEY = getattr(settings, "RECAPTCHA_PUBLIC_KEY", None)
    RECAPTCHA_PRIVATE_KEY = getattr(settings, "RECAPTCHA_PRIVATE_KEY", None)
    captcha = ReCaptchaField(public_key=RECAPTCHA_PUBLIC_KEY, private_key=RECAPTCHA_PRIVATE_KEY , widget=ReCaptchaV2Checkbox)

class UserSetPasswordForm(SetPasswordForm):

    error_messages = {
        'password_mismatch': "Passwords do not match.",
    }
    new_password1 = forms.CharField(label= "New password",
                                    widget=forms.PasswordInput(attrs={'class': 'input mb-1'}))
    new_password2 = forms.CharField(label="New password confirmation",
                                    widget=forms.PasswordInput(attrs={'class': 'input mb-1'}))

    RECAPTCHA_PUBLIC_KEY = getattr(settings, "RECAPTCHA_PUBLIC_KEY", None)
    RECAPTCHA_PRIVATE_KEY = getattr(settings, "RECAPTCHA_PRIVATE_KEY", None)
    captcha = ReCaptchaField(public_key=RECAPTCHA_PUBLIC_KEY, private_key=RECAPTCHA_PRIVATE_KEY , widget=ReCaptchaV2Checkbox)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

