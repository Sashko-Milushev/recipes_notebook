
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('recipes_notebook.accounts.urls')),
    path('', include('recipes_notebook.common.urls')),
    path('recipes/', include('recipes_notebook.recipes.urls'))

]
