from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def about(request):
    # return HttpResponse("We are at about")
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("We are at contact")
    #return render(request, 'shop/contact.html')


def tracker(request):
    return HttpResponse("We are at tracker")
    #return render(request, 'shop/tracker.html')


def search(request):
    return HttpResponse("We are at search")
    #return render(request, 'shop/search.html')


def productView(request):
    return HttpResponse("We are at productView")
    #return render(request, 'shop/productview.html')


def checkout(request):
    return HttpResponse("We are at checkout")
    #return render(request, 'shop/checkout.html')