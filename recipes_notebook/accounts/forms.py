from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

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

