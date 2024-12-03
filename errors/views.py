from django.shortcuts import render
from django.conf.urls import handler500


def get_error_500(request):
    return render(request, "errors/error_500.html")


def get_error_404(request):
    return render(request, "errors/error_404.html")


def get_error_202(request):
    return render(request, "errors/error_202.html")


def get_registration_error(request):
    return render(request, "errors/registration_error.html")


def get_login_error(request):
    return render(request, "errors/login_error.html")
