from django.urls import path

from recipes_notebook.accounts.views import RegisterView, login_user

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', login_user, name='login user'),
)
