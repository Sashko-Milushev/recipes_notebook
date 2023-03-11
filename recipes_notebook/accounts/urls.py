from django.urls import path

from recipes_notebook.accounts.views import RegisterView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register user'),
)