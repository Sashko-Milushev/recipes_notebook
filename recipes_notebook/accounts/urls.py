from django.urls import path

from recipes_notebook.accounts.views import RegisterView, login_user, LogoutView, update_user

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', login_user, name='login user'),
    path('logout/', LogoutView.as_view(), name='logout user'),
    path('<int:pk>/', update_user, name='update user'),
)
