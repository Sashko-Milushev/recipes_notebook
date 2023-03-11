from django.contrib.auth import forms as auth_forms, get_user_model, authenticate
from django import forms
from django.contrib.auth.forms import AuthenticationForm

UserModel = get_user_model()


class RegisterForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput()
        self.fields['last_name'].widget = forms.TextInput()
        self.fields['email'].widget = forms.EmailInput()
        self.fields['password1'].widget = forms.PasswordInput()
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget = forms.PasswordInput()
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    email = forms.EmailField(label='Email', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
