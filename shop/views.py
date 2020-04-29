from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


# Create your views here.
def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides+1), 'product': products}
    return render(request, 'shop/index.html', params)


def about(request):
    # return HttpResponse("We are at about")
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("We are at contact")
    # return render(request, 'shop/contact.html')


def tracker(request):
    return HttpResponse("We are at tracker")
    # return render(request, 'shop/tracker.html')


def search(request):
    return HttpResponse("We are at search")
    # return render(request, 'shop/search.html')


def productView(request):
    return HttpResponse("We are at productView")
    # return render(request, 'shop/productview.html')


def checkout(request):
    return HttpResponse("We are at checkout")
    # return render(request, 'shop/checkout.html')
