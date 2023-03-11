from django.contrib.auth import views as auth_views, get_user_model, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import authenticate, login

from recipes_notebook.accounts.forms import RegisterForm, LoginForm

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


#
# class CustomLoginView(auth_views.LoginView):
#     template_name = 'accounts/login-page.html'
#     success_url = reverse_lazy('home')
#     form_class = LoginForm
#
#     def post(self, request, *args, **kwargs):
#         print('post method called')
#         response = super().post(request, *args, **kwargs)
#         print('post method completed')
#         return response
#
#     def get_success_url(self):
#         if self.success_url:
#             return self.success_url
#         else:
#             return self.get_redirect_url() or self.get_default_redirect_url()
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         login(self.request, self.user_cache)
#         return response


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid login credentials')
    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'accounts/login-page.html', context)
