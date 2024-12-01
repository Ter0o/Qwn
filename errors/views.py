from django.shortcuts import render

def get_error_502(request):
    return render(request, "errors/r1.html")

def get_error_404(request):
    return render(request, "errors/r2.html")

def get_error_202(request):
    return render(request, "errors/r3.html")