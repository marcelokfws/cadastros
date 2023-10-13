
from django.conf.urls.static import static
from django.urls import path

from core import settings
from myapp import views

urlpatterns = [
    path('add_cadastro/', views.add_cadastro, name='add_cadastro'),


]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
