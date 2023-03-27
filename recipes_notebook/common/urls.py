from django.urls import path

from recipes_notebook.common.views import HomeView, DashboardView, MyDashboardView, SearchRecipeView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('my-dashboard/', MyDashboardView.as_view(), name='my dashboard'),
    path('search/', SearchRecipeView.as_view(), name='search recipe'),
)
