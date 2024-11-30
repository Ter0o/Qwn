from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.popular_list, name='popular_list'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('error505', views.get_error, name='get_error'),
    path('error404', views.get_error1, name='get_error1'),
    path('error202', views.get_error2, name='get_error2'),
]
