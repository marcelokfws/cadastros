
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('register/', include('accounts.urls')),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('employees/', include('employees.urls')),
    path('', include('myapp.urls'))

]
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)  # Adicionar Isto
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)  # Adicionar Isto
