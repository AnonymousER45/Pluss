from django.http import HttpResponse
from django.shortcuts import render
from . models import Product
from math import ceil


def index(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    params={'allProds':allProds }
    return render(request, 'ecom/index.html',params)


    
def about(request):
    return render(request, 'ecom/aboutus.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    #Product = get_object_or_404(Product, pk=my_id)
    #product=Product.objects.filter(id=my_id)
    #print(product)
    return render(request, "ecom/productview.html")


def checkout(request):
    return HttpResponse("We are at checkout")

def login(request):
	return render(request,'ecom/login.html')


