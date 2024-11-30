from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def popular_list(request):
    products = Product.objects.filter(available=True)[:3]
    return render(request, "main/index/index.html", {"products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, "main/product/detail.html", {"product": product})


def get_error(request):
    return render(request, "main/errors/r1.html")

def get_error1(request):
    return render(request, "main/errors/r2.html")

def get_error2(request):
    return render(request, "main/errors/r3.html")
