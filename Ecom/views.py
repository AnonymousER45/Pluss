from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . models import Product
from math import ceil

# Create your views here.
def Index(request):
    products = Product.objects.all()
    #print(products)
    n = len(products)
    slides= n//5 +ceil((n/5)-(n//5))
    param ={'product': products,'no_of_slides':slides,'range':range(slides)}
    return render(request,'ecom/index.html',param)
    

def Category1(request):
    return render(request,'ecom/product-listing1.html')

def Category2(request):
    return render(request,'ecom/produt-listing2.html')

def Productdetails(request):
    return render(request,'ecom/product-details.html')

def cart(request):
    return render(request,'ecom/cart.html')

def wishlist(request):
    return render(request,'ecom/wishlist.html')

def aboutus(request):
    return render(request,'ecom/aboutus.html')

def policies(request):
    return render(request,'ecom/policies.html')