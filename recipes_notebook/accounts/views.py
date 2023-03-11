from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from recipes_notebook.accounts.forms import RegisterForm

UserModel = get_user_model()


class RegisterView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class

        return context

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response
