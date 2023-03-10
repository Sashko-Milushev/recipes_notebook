from django.urls import path

from recipes_notebook.common.views import HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
)
