
from django.urls import path
from . import views


app_name = 'errors'

urlpatterns = [
    path('error502', views.get_error_502, name='get_error'),
    path('error404', views.get_error_404, name='get_error1'),
    path('error202', views.get_error_202, name='get_error2'),
]