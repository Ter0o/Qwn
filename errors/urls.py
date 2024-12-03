from django.urls import path
from . import views

app_name = 'errors'

urlpatterns = [
    path('error500', views.get_error_500, name='get_error_500'),
    path('error404', views.get_error_404, name='get_error_404'),
    path('error202', views.get_error_202, name='get_error_202'),
    path('registration_error', views.get_registration_error, name='get_registration_error'),
    path('login_error', views.get_login_error, name='get_login_error'),
]
