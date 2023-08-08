
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('membership_form/', views.membership_form, name='membership_form'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)