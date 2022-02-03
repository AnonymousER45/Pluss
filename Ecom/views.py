from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from decimal import Context
from .models import Category,Product,Banner,Requestbook,CartProduct,Cart, EcomOrder, WishlistProduct
from Accounts.models import Address, Customer
from math import ceil
from .forms import  RequestForm

import environ
from . import Checksum

env = environ.Env()
environ.Env.read_env()



def Index(request):
    products1 = Product.objects.filter(Category=4)
    products2 = Product.objects.filter(Category=3)
    products3 = Product.objects.filter(Category=5,subCategory=1,medium="English")
    products4 = Product.objects.filter(Category=2,subCategory=1,medium="English")
    products5 = Product.objects.filter(Category=8)
    products6 = Product.objects.filter(Category=7)
    products7 = Product.objects.filter(Category=6)
    products8 = Product.objects.filter(Category=1,subCategory=1,medium="English")
    products9 = Product.objects.filter(Category=13,subCategory=1,medium="English")
    products10 = Product.objects.filter(Category=12,subCategory=1,medium="English")
    products11 = Product.objects.filter(Category=11,subCategory=1,medium="English")

    ban = Banner.objects.all()
    param ={'product1': products1,'product2': products2,'product3': products3,'product4': products4,'product5': products5,'product6': products6,'product7': products7,'product8': products8,'product8': products8,'product9': products9,'product10': products10,'product11': products11,'banner':ban,}
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/index.html',param)

def Category1(request,myid):
    category=myid
    subcat1 = 1
    subcat2 = 2
    subcat3 = 13
    combos1 = Product.objects.filter(Category=category,subCategory=subcat3,medium="English")
    combos2 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Marathi")
    combos3 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Hindi")
    textbook1 = Product.objects.filter(Category=category,subCategory=subcat1,medium="English")
    textbook2 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Marathi")
    textbook3 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Hindi")
    digest1 = Product.objects.filter(Category=category,subCategory=subcat2,medium="English")
    digest2 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Marathi")
    digest3 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Hindi")
    set1 = Product.objects.filter(Category=category,subCategory=21,medium="English")
    set2 = Product.objects.filter(Category=category,subCategory=21,medium="Marathi")
    set3 = Product.objects.filter(Category=category,subCategory=21,medium="Hindi")
    helping1 = Product.objects.filter(Category=category,subCategory=23,medium="English")
    helping2 = Product.objects.filter(Category=category,subCategory=23,medium="Marathi")
    helping3 = Product.objects.filter(Category=category,subCategory=23,medium="Hindi")
    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'combo1':combos1,'combo2':combos2,'combo3':combos3,'textbook1':textbook1,'textbook2':textbook2,'textbook3':textbook3,'digest1':digest1,'digest2':digest2,'digest3':digest3,'set1':set1,'set2':set2,'set3':set3,'helping1':helping1,'helping2':helping2,'helping3':helping3}
    param['myid'] = myid
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/product-listing-2.html',param)

def Category2(request,myid):
    category=myid
    subcat1 = 1
    subcat2 = 2
    subcat3 = 13
    combos1 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Science")
    combos2 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Commerce")
    combos3 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Arts")
    textbook1 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Science")
    textbook2 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Commerce")
    textbook3 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Arts")
    digest1 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Science")
    digest2 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Commerce")
    digest3 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Arts")
    helping1 = Product.objects.filter(Category=category,subCategory=23,medium="Science")
    helping2 = Product.objects.filter(Category=category,subCategory=23,medium="Commerce")
    helping3 = Product.objects.filter(Category=category,subCategory=23,medium="Arts")
    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'combo1':combos1,'combo2':combos2,'combo3':combos3,'textbook1':textbook1,'textbook2':textbook2,'textbook3':textbook3,'digest1':digest1,'digest2':digest2,'digest3':digest3,'helping1':helping1,'helping2':helping2,'helping3':helping3}
    param['myid'] = myid
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/product-listing-1.html',param)


def Category3(request,myid):
    category=myid
    Prod1 = Product.objects.filter(Category=6,subCategory=28)
    Prod2 = Product.objects.filter(Category=6,subCategory=27)
    Prod3 = Product.objects.filter(Category=6,subCategory=26)
    Prod4 = Product.objects.filter(Category=6,subCategory=29)
    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'Prod1':Prod1,'Prod2':Prod2,'Prod3':Prod3,'Prod4':Prod4,}
    param['myid'] = myid
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/product-listing-3.html',param)

def Category3b(request,myid):
    category=myid
    Prod1 = Product.objects.filter(Category=6,subCategory=28)
    Prod2 = Product.objects.filter(Category=6,subCategory=27)
    Prod3 = Product.objects.filter(Category=6,subCategory=26)
    Prod4 = Product.objects.filter(Category=6,subCategory=29)
    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'Prod1':Prod1,'Prod2':Prod2,'Prod3':Prod3,'Prod4':Prod4,}
    param['myid'] = myid
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/product-listing-3b.html',param)
def Category3c(request,myid):
    category=myid
    Prod1 = Product.objects.filter(Category=6,subCategory=28)
    Prod2 = Product.objects.filter(Category=6,subCategory=27)
    Prod3 = Product.objects.filter(Category=6,subCategory=26)
    Prod4 = Product.objects.filter(Category=6,subCategory=29)
    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'Prod1':Prod1,'Prod2':Prod2,'Prod3':Prod3,'Prod4':Prod4,}
    param['myid'] = myid
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/product-listing-3c.html',param)


def Category4(request,myid):
    category=myid
    Prod1 = Product.objects.filter(Category=category,subCategory=11)
    Prod2 = Product.objects.filter(Category=category,subCategory=10)
    Prod3 = Product.objects.filter(Category=category,subCategory=12)
    Prod4= Product.objects.filter(Category=7,subCategory=24)
    Prod5= Product.objects.filter(Category=7,subCategory=25)

    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'Prod1':Prod1,'Prod2':Prod2,'Prod3':Prod3,'Prod4':Prod4,'Prod5':Prod5}
    param['myid'] = myid
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/product-listing-4.html',param)

def Category4b(request,myid):
    category=myid
    Prod1 = Product.objects.filter(Category=category,subCategory=24)
    Prod2 = Product.objects.filter(Category=category,subCategory=25)
    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'Prod1':Prod1,'Prod2':Prod2,}
    param['myid'] = myid
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/product-listing-4.html',param)


def Category5(request,myid):
    category=myid
    category2=9
    Prod1 = Product.objects.filter(Category=10,subCategory=15)
    Prod2 = Product.objects.filter(Category=10,subCategory=17)
    Prod3 = Product.objects.filter(Category=10,subCategory=18)
    Prod4 = Product.objects.filter(Category=10,subCategory=19)
    Prod5 = Product.objects.filter(Category=9,subCategory=20)
    Prod6 = Product.objects.filter(Category=9,subCategory=22)
    Prod7 = Product.objects.filter(Category=9,subCategory=21)
    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'Prod1':Prod1,'Prod2':Prod2,'Prod3':Prod3,'Prod4':Prod4,'Prod5':Prod5,'Prod6':Prod6,'Prod7':Prod7,}
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/product-listing-5.html',param)

def Category6(request,myid):
    category=myid
    subcat1 = 1
    subcat2 = 2
    subcat3 = 13
    textbook1 = Product.objects.filter(Category=category,subCategory=subcat1,medium="First Year")
    textbook2 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Second Year")
    textbook3 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Third Year")
    digest1 = Product.objects.filter(Category=category,subCategory=subcat2,medium="First Year")
    digest2 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Second Year")
    digest3 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Third Year")
    helping1 = Product.objects.filter(Category=category,subCategory=23,medium="First Year")
    helping2 = Product.objects.filter(Category=category,subCategory=23,medium="Second Year")
    helping3 = Product.objects.filter(Category=category,subCategory=23,medium="Third Year")
    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'textbook1':textbook1,'textbook2':textbook2,'textbook3':textbook3,'digest1':digest1,'digest2':digest2,'digest3':digest3,'helping1':helping1,'helping2':helping2,'helping3':helping3}
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/product-listing-6.html',param)

def Category7(request,myid):
    category=myid
    subcat1 = 1
    subcat2 = 2
    subcat3 = 13
    combos1 = Product.objects.filter(Category=category,subCategory=subcat3,medium="First Year")
    combos2 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Second Year")
    combos3 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Third Year")
    textbook1 = Product.objects.filter(Category=category,subCategory=subcat1,medium="First Year")
    textbook2 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Second Year")
    textbook3 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Third Year")
    digest1 = Product.objects.filter(Category=category,subCategory=subcat2,medium="First Year")
    digest2 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Second Year")
    digest3 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Third Year")
    helping1 = Product.objects.filter(Category=category,subCategory=23,medium="First Year")
    helping2 = Product.objects.filter(Category=category,subCategory=23,medium="Second Year")
    helping3 = Product.objects.filter(Category=category,subCategory=23,medium="Third Year")
    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'combo1':combos1,'combo2':combos2,'combo3':combos3,'textbook1':textbook1,'textbook2':textbook2,'textbook3':textbook3,'digest1':digest1,'digest2':digest2,'digest3':digest3,'helping1':helping1,'helping2':helping2,'helping3':helping3}

    return render(request,'ecom/product-listing-7.html',param)

def Category8(request,myid):
    category=myid
    subcat1 = 1
    subcat2 = 2
    subcat3 = 13
    combos1 = Product.objects.filter(Category=category,subCategory=subcat3,medium="First Year")
    combos2 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Second Year")
    combos3 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Third Year")
    textbook1 = Product.objects.filter(Category=category,subCategory=subcat1,medium="First Year")
    textbook2 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Second Year")
    textbook3 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Third Year")
    digest1 = Product.objects.filter(Category=category,subCategory=subcat2,medium="First Year")
    digest2 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Second Year")
    digest3 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Third Year")
    helping1 = Product.objects.filter(Category=category,subCategory=23,medium="First Year")
    helping2 = Product.objects.filter(Category=category,subCategory=23,medium="Second Year")
    helping3 = Product.objects.filter(Category=category,subCategory=23,medium="Third Year")
    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'combo1':combos1,'combo2':combos2,'combo3':combos3,'textbook1':textbook1,'textbook2':textbook2,'textbook3':textbook3,'digest1':digest1,'digest2':digest2,'digest3':digest3,'helping1':helping1,'helping2':helping2,'helping3':helping3}

    return render(request,'ecom/product-listing-8.html',param)

def Category9(request,myid):
    category=myid
    subcat1 = 1
    subcat2 = 2
    subcat3 = 13
    combos1 = Product.objects.filter(Category=category,subCategory=subcat3,medium="First Year")
    combos2 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Second Year")
    combos3 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Third Year")
    textbook1 = Product.objects.filter(Category=category,subCategory=subcat1,medium="First Year")
    textbook2 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Second Year")
    textbook3 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Third Year")
    digest1 = Product.objects.filter(Category=category,subCategory=subcat2,medium="First Year")
    digest2 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Second Year")
    digest3 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Third Year")
    helping1 = Product.objects.filter(Category=category,subCategory=23,medium="First Year")
    helping2 = Product.objects.filter(Category=category,subCategory=23,medium="Second Year")
    helping3 = Product.objects.filter(Category=category,subCategory=23,medium="Third Year")
    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'combo1':combos1,'combo2':combos2,'combo3':combos3,'textbook1':textbook1,'textbook2':textbook2,'textbook3':textbook3,'digest1':digest1,'digest2':digest2,'digest3':digest3,'helping1':helping1,'helping2':helping2,'helping3':helping3}

    return render(request,'ecom/product-listing-9.html',param)

def Category10(request,myid):
    # myid=35
    combos1 = Product.objects.filter(Category=myid,subCategory=58)
    combos2 = Product.objects.filter(Category=myid,subCategory=59)
    combos3 = Product.objects.filter(Category=myid,subCategory=60)
    combos4 = Product.objects.filter(Category=myid,subCategory=61)
    combos5 = Product.objects.filter(Category=myid,subCategory=62)
    combos6 = Product.objects.filter(Category=myid,subCategory=63)
    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'combo1':combos1,'combo2':combos2,'combo3':combos3,'combo4':combos4,'combo5':combos5,'combo6':combos6,}
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/schoolcomboview.html',param)

def schoolzonelistview(request):
    return render(request,'ecom/schoolzonelistview.html')


def Productdetails(request,id):
    product=Product.objects.filter(id=id)
    products = Product.objects.filter(Category=1)
    param = {'product': product[0],'products': products}
    wishprod_ids = []
    param['wishprod_ids'] = wishprod_ids
    param['wishlisted'] = False
    if request.user.is_authenticated:
        total_items(request)
        user = Customer.objects.filter(email=request.user).first()
        qs_wish = user.wishlist_set.first()
        wish_products = qs_wish.wishlistproduct_set.all()

        for prod in wish_products:
            wishprod_ids.append(prod.Product.id)
            if prod.Product.id == product.first().id:
                param['wishlisted'] = True
        param['wishprod_ids'] = wishprod_ids
        print(wishprod_ids)

    return render(request,'ecom/product-detail-2.html',param)


def wishlist(request):
    Context = {}
    if request.user:
        total_items(request)
        user_id = Customer.objects.filter(email=request.user).first()
        qs = WishlistProduct.objects.filter(userx=user_id)
        if qs.exists():
            Context['wishlist'] = qs
            return render(request,'ecom/wishlist.html',Context)
        else :
            return render(request,'ecom/empty-wishlist.html')

def aboutus(request):
    return render(request,'ecom/aboutus.html')

def contactus(request):
    return render(request,'ecom/contactus.html')

def policies(request):
    return render(request,'ecom/policies.html')

def requestbook(request):
    context = {}
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            email= form.cleaned_data['email']
            raw_password = form.cleaned_data['password1']
            phone = form.cleaned_data['phone_number']
            username = form.cleaned_data['username']
            pincode = form.cleaned_data['pincode']
            Customer.email = email
            Customer.Cust_Name = username
            Customer.phone_number = phone
            Customer.pincode = pincode
            Customer.set_password(raw_password)
            Customer.save()

        fm = RequestForm()
        context = {'form':fm}
        return render(request, 'ecom/request-book.html',context)

    else:
        fm = RequestForm()
        context={'form':fm}
        return render(request,'ecom/request-book.html',context)

def myorders(request):
    context = {}
    if request.user:
        qs = EcomOrder.objects.filter(Order_placed_BY=request.user)
        context['orders'] = qs
    return render(request,'ecom/myorders.html',context)

def orders_details(request,order_id):
    context = {}
    if request.user:
        qs = EcomOrder.objects.filter(id=order_id).first()
        context['orders'] = qs
        # context['productname'] =
        products_list = []
        products = qs.products.split(',')
        #products.remove("")
        for prod in products:
            name = prod.split(':')[0]
            price = prod.split(':')[1]

            imagelink = "/media/uploads/" + prod.split(':')[-1]
            products_list.append({"name":name,"price":price,"image":imagelink})
        print(products_list)
        context['products_list']= products_list
    return render(request,'ecom/order-details.html',context)


def myaccount(request):
    return render(request,'ecom/myaccount.html')

def mycart(request):
    """View for Cart details of Logged in Users"""
    context = {}
    if request.user:
        query_set = CartProduct.objects.filter(user=request.user)
        if query_set.count() == 0:
            return render(request,'ecom/empty-cart.html')
        cart_total_mrp, cart_total_price = 0,0
        for qs in query_set:
            cart_total_mrp += qs.Product.mrp * qs.product_quan
            cart_total_price += qs.Product.price * qs.product_quan
            # print(qs.Product.price,qs.Product.mrp)
        context['products'] = query_set
        context['cart_total_mrp'] = cart_total_mrp
        context['cart_total_price'] = cart_total_price
        context['cart_total_savings'] = cart_total_mrp - cart_total_price
        context['cart_count'] = query_set.count()
        return render(request,'ecom/mycart.html',context=context)

    return render(request,'ecom/empty-cart.html')


def mycart(request):
    """View for Cart details of Logged in Users"""
    context = {}
    query_set = CartProduct.objects.filter(user=request.user)
    user_inst = Customer.objects.filter(email=request.user).first()
    qs_wishlist = WishlistProduct.objects.filter(userx=user_inst)
    if query_set.count() == 0:
        return render(request,'ecom/empty-cart.html')

    cart_total_mrp, cart_total_price = 0,0
    for qs in query_set:
        cart_total_mrp += qs.Product.mrp * qs.product_quan
        cart_total_price += qs.Product.price * qs.product_quan
        # print(qs.Product.price,qs.Product.mrp)
    context['products'] = query_set
    request.session['total_item'] = len(query_set)
    #print(len(query_set))
    context['cart_total_mrp'] = cart_total_mrp
    context['cart_total_price'] = cart_total_price
    context['cart_total_savings'] = cart_total_mrp - cart_total_price
    context['wishlist'] = qs_wishlist

    return render(request,'ecom/mycart.html',context=context)

def myaddressbook(request):
    context = {}
    if request.user:
        query_set = Address.objects.filter(customer_id=request.user)
        context['addresses'] = query_set
        print(query_set)
        print("djbjdbcj")
    return render(request,'ecom/myaddressbook2.html',context)


def showall(request,idshowall):
    if idshowall == 1:
       products = Product.objects.filter(Category=11,subCategory=1,medium="English")
    elif idshowall == 2:
       products = Product.objects.filter(Category=12,subCategory=1,medium="English")
    elif idshowall == 3:
       products = Prodct.objects.filter(Category=13,subCategory=1,medium="English")
    elif idshowall == 4:
       products = Product.objects.filter(Category=1,subCategory=1,medium="English")
    elif idshowall == 5:
       products = Product.objects.filter(Category=2,subCategory=1,medium="English")
    elif idshowall == 6:
       products = Product.objects.filter(Category=5,subCategory=1,medium="English")
    elif idshowall == 7:
       products = Product.objects.filter(Category=3,subCategory=1)
    elif idshowall == 8:
       products = Product.objects.filter(Category=4,subCategory=1)
    elif idshowall == 9:
       products = Product.objects.filter(Category=3,subCategory=1,medium="Science")
    elif idshowall == 10:
       products = Product.objects.filter(Category=3,subCategory=1,medium="Commerce")
    elif idshowall == 11:
       products = Product.objects.filter(Category=3,subCategory=1,medium="Arts")
    elif idshowall == 12:
       products = Product.objects.filter(Category=4,subCategory=1,medium="Science")
    elif idshowall == 13:
       products = Product.objects.filter(Category=4,subCategory=1,medium="Commerce")
    elif idshowall == 14:
       products = Product.objects.filter(Category=4,subCategory=1,medium="Arts")
    elif idshowall == 15:
       products = Product.objects.filter(Category=6)
    elif idshowall == 16:
       products = Product.objects.filter(Category=6,subCategory=28)
    elif idshowall == 17:
       products = Product.objects.filter(Category=6,subCategory=27)
    elif idshowall == 18:
       products = Product.objects.filter(Category=6,subCategory=26)
    elif idshowall == 19:
       products = Product.objects.filter(Category=6,subCategory=29)
    elif idshowall == 20:
       products = Product.objects.filter(Category=7)
    elif idshowall == 21:
       products = Product.objects.filter(Category=8)
    else :
        products = Product.objects.filter(Category=8,subCategory=1,medium="English")
    param ={'product':products}
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/productshowall.html',param)

def comboshowall(request,idshowall):
    if idshowall == 1:
       products = Product.objects.filter(Category=11,subCategory=13,medium="English")
    elif idshowall == 2:
       products = Product.objects.filter(Category=12,subCategory=13,medium="English")
    elif idshowall == 3:
       products = Prodct.objects.filter(Category=13,subCategory=13,medium="English")
    elif idshowall == 4:
       products = Product.objects.filter(Category=1,subCategory=13,medium="English")
    elif idshowall == 5:
       products = Product.objects.filter(Category=2,subCategory=13,medium="English")
    elif idshowall == 6:
       products = Product.objects.filter(Category=5,subCategory=13,medium="English")
    elif idshowall == 9:
       products = Product.objects.filter(Category=3,subCategory=13,medium="Science")
    elif idshowall == 10:
       products = Product.objects.filter(Category=3,subCategory=13,medium="Arts")
    elif idshowall == 11:
       products = Product.objects.filter(Category=3,subCategory=13,medium="Arts")
    elif idshowall == 12:
       products = Product.objects.filter(Category=4,subCategory=13,medium="Science")
    elif idshowall == 13:
       products = Product.objects.filter(Category=4,subCategory=13,medium="Commerce")
    elif idshowall == 14:
       products = Product.objects.filter(Category=4,subCategory=13,medium="Arts")
    else:
       products = Product.object.filter(Category=1,subCategory=13,medium="English")
    param ={'product':products}
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/comboshowall.html',param)



def showalldemo(request):
    a = "0102EN"
    cat = int(a[:2])
    subcat = int(a[2:4])
    med = a[4:]
    products = Product.objects.filter(Category=cat,subCategory=subcat)
    param ={'product':products}
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted

    return render(request,'ecom/produt-showalldemo.html')

def search(request,keyword):
    products = Product.objects.filter(desp__icontains=keyword)[:15]
    key = keyword
    param ={'product':products,'key':key}
    return render(request,'ecom/search.html',param)

def search(request,keyword):

    list5th = ['5','5 TH','5th','5TH','5 th', '5 th Standard', '5 th Standard', '5 th Std', '5 th Standard','5 th Standrad', '5 th Standrad', '5 th Std', '5 th Standrad','5 th books','5th books','5 th Std books','5 th Standard books','5 th Books','5th Books','5 th Std Books','5 th Standard Books','5 th book','5th book','5 th Std book','5 th Standard book','5 th Book','5th Book','5 th Std Book','5 th Standard Book','5th Standard', '5th Standard', '5 TH Std', '5 TH Standard''5 TH Standrad', '5 TH Standrad', '5 TH Std', '5 TH Standrad','5 TH books',
           '5TH books','5 TH Std books','5 TH Standard books','5 TH Books','5TH Books','5 TH Std Books','5 TH Standard Books','5 TH book','5TH book',
           '5 TH Std book','5 TH Standard book','5 TH Book','5TH Book','5 TH Std Book','5 TH Standard Book','5TH Standard', '5TH Standard', '5TH Std', '5TH Standard''5TH Standrad', '5TH Standrad', '5TH Std', '5TH Standrad','5TH books',
           '5TH books','5TH Std books','5TH Standard books','5TH Books','5TH Books','5TH Std Books','5TH Standard Books','5TH book','5TH book',
           '5TH Std book','5TH Standard book','5TH Book','5TH Book','5TH Std Book','5TH Standard Book','5th Standard', '5th Standard', '5th Std', '5th Standard''5th Standrad', '5th Standrad', '5th Std', '5th Standrad','5th books',
           '5th books','5th Std books','5th Standard books','5th Books','5th Books','5th Std Books','5th Standard Books','5th book','5th book',
           '5th Std book','5th Standard book','5th Book','5th Book','5th Std Book','5th Standard Book']
    list6th = ['6','6 TH','6th','6TH','6 th', '6 th Standard', '6 th Standard', '6 th Std','6 th Standard','6 th Standrad', '6 th Standrad', '6 th Std', '6 th Standrad','6 th books','6th books','6 th Std books','6 th Standard books','6 th Books','6th Books','6 th Std Books','6 th Standard Books','6 th book','6th book','6 th Std book','6 th Standard book','6 th Book','6th Book','6 th Std Book','6 th Standard Book','6th Standard', '6th Standard', '6 TH Std', '6 TH Standard''6 TH Standrad', '6 TH Standrad', '6 TH Std', '6 TH Standrad','6 TH books',
           '6TH books','6 TH Std books','6 TH Standard books','6 TH Books','6TH Books','6 TH Std Books','6 TH Standard Books','6 TH book','6TH book',
           '6 TH Std book','6 TH Standard book','6 TH Book','6TH Book','6 TH Std Book','6 TH Standard Book','6TH Standard', '6TH Standard', '6TH Std', '6TH Standard''6TH Standrad', '6TH Standrad', '6TH Std', '6TH Standrad','6TH books',
           '6TH books','6TH Std books','6TH Standard books','6TH Books','6TH Books','6TH Std Books','6TH Standard Books','6TH book','6TH book',
           '6TH Std book','6TH Standard book','6TH Book','6TH Book','6TH Std Book','6TH Standard Book','6th Standard', '6th Standard', '6th Std', '6th Standard''6th Standrad', '6th Standrad', '6th Std', '6th Standrad','6th books',
           '6th books','6th Std books','6th Standard books','6th Books','6th Books','6th Std Books','6th Standard Books','6th book','6th book',
           '6th Std book','6th Standard book','6th Book','6th Book','6th Std Book','6th Standard Book']
    list7th = ['7','7 TH','7th','7TH','7 th','7 th Standard', '7 th Standard', '7 th Std', '7 th Standard','7 th Standrad', '7 th Standrad', '7 th Std', '7 th Standrad','7 th books','7th books','7 th Std books','7 th Standard books','7 th Books','7th Books','7 th Std Books','7 th Standard Books','7 th book','7th book','7 th Std book','7 th Standard book','7 th Book','7th Book','7 th Std Book','7 th Standard Book','7th Standard', '7th Standard', '7 TH Std', '7 TH Standard''7 TH Standrad', '7 TH Standrad', '7 TH Std', '7 TH Standrad','7 TH books',
           '7TH books','7 TH Std books','7 TH Standard books','7 TH Books','7TH Books','7 TH Std Books','7 TH Standard Books','7 TH book','7TH book',
           '7 TH Std book','7 TH Standard book','7 TH Book','7TH Book','7 TH Std Book','7 TH Standard Book','7TH Standard', '7TH Standard', '7TH Std', '7TH Standard''7TH Standrad', '7TH Standrad', '7TH Std', '7TH Standrad','7TH books',
           '7TH books','7TH Std books','7TH Standard books','7TH Books','7TH Books','7TH Std Books','7TH Standard Books','7TH book','7TH book',
           '7TH Std book','7TH Standard book','7TH Book','7TH Book','7TH Std Book','7TH Standard Book','7th Standard', '7th Standard', '7th Std', '7th Standard''7th Standrad', '7th Standrad', '7th Std', '7th Standrad','7th books',
           '7th books','7th Std books','7th Standard books','7th Books','7th Books','7th Std Books','7th Standard Books','7th book','7th book',
           '7th Std book','7th Standard book','7th Book','7th Book','7th Std Book','7th Standard Book']
    list8th = ['8','8 TH','8th','8TH','8 th', '8 th Standard', '8 th Standard', '8 th Std', '8 th Standard','8 th Standrad', '8 th Standrad', '8 th Std', '8 th Standrad',
	        '8 th books','8th books','8 th Std books','8 th Standard books','8 th Books','8th Books','8 th Std Books','8 th Standard Books',
	        '8 th book','8th book','8 th Std book','8 th Standard book','8 th Book','8th Book','8 th Std Book','8 th Standard Book','8th Standard', '8th Standard', '8 TH Std', '8 TH Standard''8 TH Standrad', '8 TH Standrad', '8 TH Std', '8 TH Standrad','8 TH books',
           '8TH books','8 TH Std books','8 TH Standard books','8 TH Books','8TH Books','8 TH Std Books','8 TH Standard Books','8 TH book','8TH book',
           '8 TH Std book','8 TH Standard book','8 TH Book','8TH Book','8 TH Std Book','8 TH Standard Book','8TH Standard', '8TH Standard', '8TH Std', '8TH Standard''8TH Standrad', '8TH Standrad', '8TH Std', '8TH Standrad','8TH books',
           '8TH books','8TH Std books','8TH Standard books','8TH Books','8TH Books','8TH Std Books','8TH Standard Books','8TH book','8TH book',
           '8TH Std book','8TH Standard book','8TH Book','8TH Book','8TH Std Book','8TH Standard Book','8th Standard', '8th Standard', '8th Std', '8th Standard''8th Standrad', '8th Standrad', '8th Std', '8th Standrad','8th books',
           '8th books','8th Std books','8th Standard books','8th Books','8th Books','8th Std Books','8th Standard Books','8th book','8th book',
           '8th Std book','8th Standard book','8th Book','8th Book','8th Std Book','8th Standard Book']

    list9th = ['9', '9 th', '9 TH','9th','9TH','9 th', '9 th Standard', '9 th Standard', '9 th Std', '9 th Standard''9 th Standrad', '9 th Standrad', '9 th Std',
	           '9 th Standrad','9 th books','9th books','9 th Std books','9 th Standard books','9 th Books','9th Books','9 th Std Books',
	           '9 th Standard Books','9 th book','9th book','9 th Std book','9 th Standard book','9 th Book','9th Book','9 th Std Book','9 th Standard Book','9th Standard', '9th Standard', '9 TH Std', '9 TH Standard''9 TH Standrad', '9 TH Standrad', '9 TH Std', '9 TH Standrad','9 TH books',
           '9TH books','9 TH Std books','9 TH Standard books','9 TH Books','9TH Books','9 TH Std Books','9 TH Standard Books','9 TH book','9TH book',
           '9 TH Std book','9 TH Standard book','9 TH Book','9TH Book','9 TH Std Book','9 TH Standard Book','9TH Standard', '9TH Standard', '9TH Std', '9TH Standard''9TH Standrad', '9TH Standrad', '9TH Std', '9TH Standrad','9TH books',
           '9TH books','9TH Std books','9TH Standard books','9TH Books','9TH Books','9TH Std Books','9TH Standard Books','9TH book','9TH book',
           '9TH Std book','9TH Standard book','9TH Book','9TH Book','9TH Std Book','9TH Standard Book','9th Standard', '9th Standard', '9th Std', '9th Standard''9th Standrad', '9th Standrad', '9th Std', '9th Standrad','9th books',
           '9th books','9th Std books','9th Standard books','9th Books','9th Books','9th Std Books','9th Standard Books','9th book','9th book',
           '9th Std book','9th Standard book','9th Book','9th Book','9th Std Book','9th Standard Book']
    list10th = ['10','10 TH','10th','10TH','10 th', '10 th Standard', '10 th Standard', '10 th Std', '10 th Standard''10 th Standrad', '10 th Standrad', '10 th Std',
	            '10 th Standrad','10 th books','10th books','10 th Std books','10 th Standard books','10 th Books','10th Books','10 th Std Books',
	            '10 th Standard Books','10 th book','10th book','10 th Std book','10 th Standard book','10 th Book','10th Book','10 th Std Book',
	            '10 th Standard Book','10th Standard', '10th Standard', '10 TH Std', '10 TH Standard''10 TH Standrad', '10 TH Standrad', '10 TH Std', '10 TH Standrad','10 TH books',
           '10TH books','10 TH Std books','10 TH Standard books','10 TH Books','10TH Books','10 TH Std Books','10 TH Standard Books','10 TH book','10TH book',
           '10 TH Std book','10 TH Standard book','10 TH Book','10TH Book','10 TH Std Book','10 TH Standard Book','10TH Standard', '10TH Standard', '10TH Std', '10TH Standard''10TH Standrad', '10TH Standrad', '10TH Std', '10TH Standrad','10TH books',
           '10TH books','10TH Std books','10TH Standard books','10TH Books','10TH Books','10TH Std Books','10TH Standard Books','10TH book','10TH book',
           '10TH Std book','10TH Standard book','10TH Book','10TH Book','10TH Std Book','10TH Standard Book','10th Standard', '10th Standard', '10th Std', '10th Standard''10th Standrad', '10th Standrad', '10th Std', '10th Standrad','10th books',
           '10th books','10th Std books','10th Standard books','10th Books','10th Books','10th Std Books','10th Standard Books','10th book','10th book',
           '10th Std book','10th Standard book','10th Book','10th Book','10th Std Book','10th Standard Book']

    list11th = ['11','11 TH','11th','11TH','11 th', '11 th Standard', '11 th Standard', '11 th Std', '11 th Standard''11 th Standrad', '11 th Standrad', '11 th Std',
	            '11 th Standrad','11 th books','11th books','11 th Std books','11 th Standard books','11 th Books','11th Books','11 th Std Books',
	            '11 th Standard Books','11 th book','11th book','11 th Std book','11 th Standard book','11 th Book','11th Book','11 th Std Book',
	            '11 th Standard Book','11th Standard', '11th Standard', '11 TH Std', '11 TH Standard''11 TH Standrad', '11 TH Standrad', '11 TH Std', '11 TH Standrad','11 TH books',
           '11TH books','11 TH Std books','11 TH Standard books','11 TH Books','11TH Books','11 TH Std Books','11 TH Standard Books','11 TH book','11TH book',
           '11 TH Std book','11 TH Standard book','11 TH Book','11TH Book','11 TH Std Book','11 TH Standard Book','11TH Standard', '11TH Standard', '11TH Std', '11TH Standard''11TH Standrad', '11TH Standrad', '11TH Std', '11TH Standrad','11TH books',
           '11TH books','11TH Std books','11TH Standard books','11TH Books','11TH Books','11TH Std Books','11TH Standard Books','11TH book','11TH book',
           '11TH Std book','11TH Standard book','11TH Book','11TH Book','11TH Std Book','11TH Standard Book','11th Standard', '11th Standard', '11th Std', '11th Standard''11th Standrad', '11th Standrad', '11th Std', '11th Standrad','11th books',
           '11th books','11th Std books','11th Standard books','11th Books','11th Books','11th Std Books','11th Standard Books','11th book','11th book',
           '11th Std book','11th Standard book','11th Book','11th Book','11th Std Book','11th Standard Book']

    list12th = ['12','12 TH','12th','12TH','12 th','12 th Standard', '12 th Standard', '12 th Std', '12 th Standard''12 th Standrad', '12 th Standrad', '12 th Std',
	            '12 th Standrad','12 th books','12th books','12 th Std books','12 th Standard books','12 th Books','12th Books','12 th Std Books',
	            '12 th Standard Books','12 th book','12th book','12 th Std book','12 th Standard book','12 th Book','12th Book','12 th Std Book',
	            '12 th Standard Book','12th Standard', '12th Standard', '12 TH Std', '12 TH Standard''12 TH Standrad', '12 TH Standrad', '12 TH Std', '12 TH Standrad','12 TH books',
           '12TH books','12 TH Std books','12 TH Standard books','12 TH Books','12TH Books','12 TH Std Books','12 TH Standard Books','12 TH book','12TH book',
           '12 TH Std book','12 TH Standard book','12 TH Book','12TH Book','12 TH Std Book','12 TH Standard Book','12TH Standard', '12TH Standard', '12TH Std', '12TH Standard''12TH Standrad', '12TH Standrad', '12TH Std', '12TH Standrad','12TH books',
           '12TH books','12TH Std books','12TH Standard books','12TH Books','12TH Books','12TH Std Books','12TH Standard Books','12TH book','12TH book',
           '12TH Std book','12TH Standard book','12TH Book','12TH Book','12TH Std Book','12TH Standard Book','12th Standard', '12th Standard', '12th Std', '12th Standard''12th Standrad', '12th Standrad', '12th Std', '12th Standrad','12th books',
           '12th books','12th Std books','12th Standard books','12th Books','12th Books','12th Std Books','12th Standard Books','12th book','12th book',
           '12th Std book','12th Standard book','12th Book','12th Book','12th Std Book','12th Standard Book']

    branch1 = [' Science',' science',' SCI',' SCIENCE',' Sci',' Sci.',' SCI.']
    branch2 = [' ARTS',' arts',' Arts',' art',' Art',' ART',' arts.',' ARTS.']
    branch3 = [' Commerce',' COMMERCE',' commerce',' Com',' Com.',' COM',' COM.',' com.',' com']
    Catlist = [' Textbook',' Textbooks',' TB',' tb',' text book',' textbook',' Text Book']
    Catlist1 = [' Digest','DIGEST',' Digests','DIGESTS',' DIG' ,' Dig','Digst','Digest']
	#Catlist2 = ['HH','hh','Helping Hands','HELPING HANDS','HELPING','helping','helping Hands''helping hands''helping Hand''helping hand']
    list5th1 = []
    list6th1 = []
    list7th1 = []
    list8th1 = []
    list9th1 = []
    list9th1 = []
    list10th1 = []
    list11thSci1 = []
    list12thSci1 = []
    list11thCom1 = []
    list12thCom1 = []
    list11thArt1 = []
    list12thArt1 = []
    list11thSci2 = []
    list12thSci2 = []
    list11thCom2 = []
    list12thCom2 = []
    list11thArt2 = []
    list12thArt2 = []

    for i in range(0, len(list5th)):
	    for j in range(0 ,len(Catlist)):
	        list5th1.append(list5th[i]+Catlist[j])

    for i in range(0, len(list6th)):
	    for j in range(0 ,len(Catlist)):
	        list6th1.append(list6th[i]+Catlist[j])

    for i in range(0, len(list7th)):
	    for j in range(0 ,len(Catlist)):
	        list7th1.append(list7th[i]+Catlist[j])

    for i in range(0, len(list8th)):
	    for j in range(0 ,len(Catlist)):
	        list8th1.append(list8th[i]+Catlist[j])

    for i in range(0, len(list9th)):
	    for j in range(0 ,len(Catlist)):
	        list9th1.append(list9th[i]+Catlist[j])

    for i in range(0, len(list10th)):
	    for j in range(0 ,len(Catlist)):
	        list10th1.append(list10th[i]+Catlist[j])

    for i in range(0, len(list11th)):

	    for j in range(0 ,len(Catlist)):
	        list10th1.append(list10th[i]+Catlist[j])

    for i in range(0, len(list11th)):
	    for a in range(0 ,len(branch1)):
	        list11thSci1.append(list11th[i]+branch1[a])
	        list11thSci2.append(list11th[i]+branch1[a])
	    for b in range(0 ,len(branch2)):
	        list11thCom1.append(list11th[i]+branch3[b])
	        list11thCom2.append(list11th[i]+branch3[b])
	    for c in range(0 ,len(branch2)):
	        list11thArt1.append(list11th[i]+branch2[c])
	        list11thArt2.append(list11th[i]+branch2[c])
	    for j in range(0 ,len(Catlist)):
	        list11thSci1.append(list11thSci1[i]+Catlist[j])
	        list11thCom1.append(list11thCom1[i]+Catlist[j])
	        list11thArt1.append(list11thArt1[i]+Catlist[j])

    for i in range(0, len(list12th)):
	    for a in range(0 ,len(branch1)):
	        list12thSci1.append(list12th[i]+branch1[a])
	        list12thSci2.append(list12th[i]+branch1[a])
	    for b in range(0 ,len(branch2)):
	        list12thCom1.append(list12th[i]+branch3[b])
	        list12thCom2.append(list12th[i]+branch3[b])
	    for c in range(0 ,len(branch2)):
	        list12thArt1.append(list12th[i]+branch2[c])
	        list12thArt2.append(list12th[i]+branch2[c])
	    for j in range(0 ,len(Catlist)):
	        list12thSci1.append(list12thSci1[i]+Catlist[j])
	        list12thCom1.append(list12thCom1[i]+Catlist[j])
	        list12thArt1.append(list12thArt1[i]+Catlist[j])

	# print(list5th1)
	# print("***********")
	# print(list6th1)
	# print("***********")
	# print(list7th1)
	# print("***********")
	# print(list8th1)
	# print("***********")
	# print(list9th1)
	# print("***********")
	# print(list10th1)
	# print("***********")
	# print(list11thSci1)
	# print("***********")
	# print(list11thCom1)
	# print("***********")
	# print(list11thArt1)
	# print("***********")
	# print(list12thSci1)
	# print("***********")
	# print(list12thCom1)
	# print("***********")
	# print(list12thArt1)
	# print("***********")
	# print("***********")
	# print(list11thSci2)
	# print("***********")
	# print(list11thCom2)
	# print("***********")
	# print(list11thArt2)
	# print("***********")
	# print(list12thSci2)
	# print("***********")
	# print(list12thCom2)
	# print("***********")
	# print(list12thArt2)
	# print("***********")

	# test_list1 = ['9', '9 th', '9 TH', '9 th Standard', '9 th Standard', '9 th Std', '9 th Standard']

# 	keyword  = '5 Textbook'

	# res = list(filter(lambda x: list8th in x, keyword))
    res5 = list(filter(lambda x:keyword in x, list5th))
    cat5 = list(filter(lambda x:keyword in x, list5th1))
    res6 = list(filter(lambda x:keyword in x, list6th))
    cat6 = list(filter(lambda x:keyword in x, list6th1))
    res7 = list(filter(lambda x:keyword in x, list7th))
    cat7 = list(filter(lambda x:keyword in x, list7th1))
    res8 = list(filter(lambda x:keyword in x, list8th))
    cat8 = list(filter(lambda x:keyword in x, list8th1))
    res9 = list(filter(lambda x:keyword in x, list9th))
    cat9 = list(filter(lambda x:keyword in x, list9th1))
    res10 = list(filter(lambda x:keyword in x, list10th))
    cat10 = list(filter(lambda x:keyword in x, list10th1))


    res11 = list(filter(lambda x:keyword in x,list11th))
    res11Sci = list(filter(lambda x:keyword in x,list11thSci2))
    res11Com = list(filter(lambda x:keyword in x,list11thCom2))
    res11Art = list(filter(lambda x:keyword in x,list11thArt2))
    cat11Sci1 = list(filter(lambda x:keyword in x,list11thSci1))
    cat11Com1 = list(filter(lambda x:keyword in x,list11thCom1))
    cat11Art1 = list(filter(lambda x:keyword in x,list11thArt1))

    res12 = list(filter(lambda x:keyword in x,list12th))
    res12Sci = list(filter(lambda x:keyword in x,list12thSci2))
    res12Com = list(filter(lambda x:keyword in x,list12thCom2))
    res12Art = list(filter(lambda x:keyword in x,list12thArt2))
    cat12Sci1 = list(filter(lambda x:keyword in x,list12thSci1))
    cat12Com1 = list(filter(lambda x:keyword in x,list12thCom1))
    cat12Art1 = list(filter(lambda x:keyword in x,list12thArt1))

	# res11 = list(filter(lambda x:keyword in x,list12th))
	# res11Sci = list(filter(lambda x:keyword in x, list5th))
	# cat11 = list(filter(lambda x:keyword in x, list5th1))
	# res11 = list(filter(lambda x:keyword in x, list5th))
	# cat11 = list(filter(lambda x:keyword in x, list5th1))
	# res11 = list(filter(lambda x:keyword in x, list5th))
	# cat11 = list(filter(lambda x:keyword in x, list5th1))

    if res5:
	    print("5 th books")
	    query_set = Product.objects.filter(Category=11,medium="English")
    elif cat5:
	    print("5 th textbooks")
	    query_set = Product.objects.filter(Category=11,subCategory=1,medium="English")
    elif res6:
	    print("6 th books")
	    query_set = Product.objects.filter(Category=12,medium="English")
    elif cat6:
	    print("6 th textbooks")
	    query_set = Product.objects.filter(Category=12,subCategory=1,medium="English")

    elif res7:
	    print("7 th books")
	    query_set = Product.objects.filter(Category=13,medium="English")
    elif cat7:
	    print("7 th textbooks")
	    query_set = Product.objects.filter(Category=13,subCategory=1,medium="English")
    elif res8:
	    print("8 th books")
	    query_set = Product.objects.filter(Category=1,medium="English")

    elif cat8:
	    print("8 th textbooks")
	    query_set = Product.objects.filter(Category=1,subCategory=1,medium="English")
    elif res9:
	    query_set = Product.objects.filter(Category=2,medium="English")
	    print("9 th books")
    elif cat9:
	    print("9 th textbooks")
	    query_set = Product.objects.filter(Category=2,subCategory=1,medium="English")
    elif res10:
	    print("10 th books")
	    query_set = Product.objects.filter(Category=5,medium="English")
    elif cat10:
	    print("10 th textbooks")
	    query_set = Product.objects.filter(Category=5,subCategory=1,medium="English")
    elif res11:
	    print("11 th books")
	    query_set = Product.objects.filter(Category=3)
    elif res11Sci:
	    print("11 th Sci books")
	    query_set = Product.objects.filter(Category=3,medium="Science")
    elif res11Com:
	    print("11 th Com books")
	    query_set = Product.objects.filter(Category=3,medium="Commerce")
    elif res11Art:
	    print("11 th Art books")
	    query_set = Product.objects.filter(Category=3,medium="Arts")
    elif cat11Sci1:
	    print("11 th Science textbooks")
	    query_set = Product.objects.filter(Category=3,subCategory=1,medium="Science")
    elif cat11Com1:
	    print("11 th Commerce textbooks")
	    query_set = Product.objects.filter(Category=3,subCategory=1,medium="Commerce")
    elif cat11Art1:
	    print("11 th Artstextbooks")
	    query_set = Product.objects.filter(Category=3,subCategory=1,medium="Arts")
    elif res12:
	    print("12 th books")
	    query_set = Product.objects.filter(Category=4)
    elif res12Sci:
	    print("12 th Sci books")
	    query_set = Product.objects.filter(Category=4,medium="Science")
    elif res12Com:
	    print("12 th Com books")
	    query_set = Product.objects.filter(Category=4,medium="Commerce")
    elif res12Art:
	    print("12 th Art books")
	    query_set = Product.objects.filter(Category=4,medium="Arts")
    elif cat12Sci1:
	    print("12 th Science textbooks")
	    query_set = Product.objects.filter(Category=4,subCategory=1,medium="Science")
    elif cat12Com1:
	    print("12 th Commerce textbooks")
	    query_set = Product.objects.filter(Category=4,subCategory=1,medium="Commerce")
    elif cat12Art1:
	    print("12 th Artstextbooks")
	    query_set = Product.objects.filter(Category=4,subCategory=1,medium="Arts")
    key = keyword
    param ={'product':query_set,'key':key}
    return render(request,'ecom/search.html',param)

def payment(request,order_id):
    return render(request,'ecom/payment.html')

# def orderplaced(request,order_id):
#     id = order_id
#     param={"order_id":id}
#     return render(request,'ecom/orderplaced.html',param)

def orderplaced(request):
    return render(request,'ecom/orderplaced.html')

def orderfailed(request):
    return render(request,'ecom/orderfailed.html')

def add_address(request):
    # context = {}
    # if request.method == 'POST':
    #     try:
    #         name = request.POST['name']
    #         email = request.POST['email']
    #         phone_number = request.POST['phone']
    #         Password = request.POST['Password']
    #         if request.POST['pincode']:
    #             pincode = request.POST['pincode']
    #     except:
    #         print("Enter all the required Fields")
    #         return render(request, 'ecom/add_address.html',context)
    #     cus = Customer(username=name,email=email,phone_number=phone_number,pincode=pincode)
    #     cus.set_password(Password)
    #     cus.save()
    #     return redirect('login')
    # return render(request, 'ecom/add_address.html',context)

    return render(request,'ecom/add_address.html')

def edit_address(request,id):
    context = {}
    if request.user:
        query_set = Address.objects.filter(id=id)
        context['address'] = query_set
        context['add_id'] = id
        print(query_set)
        print("djbjdbcj")

    return render(request,'ecom/edit_address2.html',context)

def edit_addresss(request,id):
    context = {}
    if request.user:
        query_set = Address.objects.filter(id=id)
        context['address'] = query_set
        context['add_id'] = id
        print(query_set)
        print("djbjdbcj")

    return render(request,'ecom/edit_address.html',context)


def ordercancelation(request):
    return render(request,'ecom/ordercancelation.html')

def returnandexchange(request):
    return render(request,'ecom/returnandexchange.html')

def faq(request):
    return render(request,'ecom/faq.html')

def privacy(request):
    return render(request,'ecom/privacy.html')

def termsandcondition(request):
    return render(request,'ecom/termsandcondition.html')

def addressbook(request):
    context = {}
    if request.user:
        query_set = Address.objects.filter(customer_id=request.user)
        context['addresses'] = query_set
        print(query_set)
        print("djbjdbcj")
    return render(request,'ecom/addressbook.html',context)

def personal_info(request):
    return render(request,'ecom/personal-info.html')


def wishlisted_ids(user):
    wishprod_ids = []
    user = Customer.objects.filter(email=user).first()
    qs_wish = user.wishlist_set.first()

    wish_products = qs_wish.wishlistproduct_set.all()

    for prod in wish_products:
        wishprod_ids.append(prod.Product.id)

    print(wishprod_ids)
    return wishprod_ids


def total_items(request):
    if request.user:
        query_set = CartProduct.objects.filter(user=request.user)
        len_qs = len(query_set)
        request.session['total_item'] = len_qs
        return len_qs


def start_onlinepayments(request,order_id):
    order_object = EcomOrder.objects.get(id=order_id)
    param_dict = {
        'MID': env('MERCHANTID'),
        'ORDER_ID': str(order_object.id),
        'TXN_AMOUNT': str(order_object.order_price),
        'CUST_ID': str(order_object.Order_placed_BY),
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'WEBSTAGING',
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL': 'https://www.pluscrown.com/django/api/handlepayment/',
        # this is the url of handlepayment function, paytm will send a POST request to the fuction associated with this CALLBACK_URL
    }

    # create new checksum (unique hashed string) using our merchant key with every paytm payment
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, env('MERCHANTKEY'))
    # send the dictionary with all the credentials to the frontend
    #return Response({'param_dict': param_dict})
    return render(request, 'payments/paytm.html', {'param_dict': param_dict})

def start_onlinepayments2(request,order_id):
    order_object = EcomOrder.objects.get(id=order_id)
    param_dict = {
        'MID': env('MERCHANTID'),
        'ORDER_ID': str(order_object.id),
        'TXN_AMOUNT': str(order_object.order_total),
        'CUST_ID': str(order_object.Order_placed_BY),
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'WEBSTAGING',
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL': 'https://www.pluscrown.com/django/api/handlepayments/',
        # this is the url of handlepayment function, paytm will send a POST request to the fuction associated with this CALLBACK_URL
    }

    # create new checksum (unique hashed string) using our merchant key with every paytm payment
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, env('MERCHANTKEY'))
    # send the dictionary with all the credentials to the frontend
    #return Response({'param_dict': param_dict})
    return render(request, 'payments/paytm.html', {'param_dict': param_dict})


# @api_view(['POST'])
# def handlepayment(request):
#     checksum = ""
#     # the request.POST is coming from paytm
#     form = request.POST

#     response_dict = {}
#     order = None  # initialize the order varible with None

#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             # 'CHECKSUMHASH' is coming from paytm and we will assign it to checksum variable to verify our paymant
#             checksum = form[i]

#         if i == 'ORDERID':
#             # we will get an order with id==ORDERID to turn isPaid=True when payment is successful
#             order = EcomOrder.objects.get(id=form[i])

#     # we will verify the payment using our merchant key and the checksum that we are getting from Paytm request.POST
#     verify = Checksum.verify_checksum(response_dict, env('MERCHANTKEY'), checksum)

#     if verify:

#         if response_dict['RESPCODE'] == '01':
#             # if the response code is 01 that means our transaction is successfull
#             print('order successful')
#             # after successfull payment we will make isPaid=True and will save the order
#             # order.order_completed = True
#             orderid = response_dict['ORDERID']
#             order_object = EcomOrder.objects.get(id=orderid)
#             order_object.order_completed = True
#             order_object.save()
#             # we will render a template to display the payment status
#             #return render(request, 'payments/paymentstatus.html', {'response': response_dict})
#             return response({'response': response_dict,'status':"successfully"})
#         else:
#             print('order was not successful because' + response_dict['RESPMSG'])
#             #return render(request, 'payments/paymentstatus.html', {'response': response_dict})
#             return response({'response': response_dict,'status':"UNsuccessfully"})


# def Category1(request,myid):
#     category=myid
#     subcat1 = 1
#     subcat2 = 2
#     subcat3 = 13
#     combos1 = Product.objects.filter(Category=category,subCategory=subcat3,medium="English")
#     combos2 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Marathi")
#     combos3 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Hindi")
#     textbook1 = Product.objects.filter(Category=category,subCategory=subcat1,medium="English")
#     textbook2 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Marathi")
#     textbook3 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Hindi")
#     digest1 = Product.objects.filter(Category=category,subCategory=subcat2,medium="English")
#     digest2 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Marathi")
#     digest3 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Hindi")
#     set1 = Product.objects.filter(Category=category,subCategory=21,medium="English")
#     set2 = Product.objects.filter(Category=category,subCategory=21,medium="Marathi")
#     set3 = Product.objects.filter(Category=category,subCategory=21,medium="Hindi")
#     helping1 = Product.objects.filter(Category=category,subCategory=23,medium="English")
#     helping2 = Product.objects.filter(Category=category,subCategory=23,medium="Marathi")
#     helping3 = Product.objects.filter(Category=category,subCategory=23,medium="Hindi")
#     cats = Category.objects.filter(id=myid)
#     param ={'cat': cats,'combo1':combos1,'combo2':combos2,'combo3':combos3,'textbook1':textbook1,'textbook2':textbook2,'textbook3':textbook3,'digest1':digest1,'digest2':digest2,'digest3':digest3,'set1':set1,'set2':set2,'set3':set3,'helping1':helping1,'helping2':helping2,'helping3':helping3}
#     return render(request,'ecom/productlisting.html',param)

# def Category2(request,myid):
#     category=myid
#     subcat1 = 1
#     subcat2 = 2
#     subcat3 = 13
#     combos1 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Science")
#     combos2 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Commerce")
#     combos3 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Arts")
#     textbook1 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Science")
#     textbook2 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Commerce")
#     textbook3 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Arts")
#     digest1 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Science")
#     digest2 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Commerce")
#     digest3 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Arts")
#     helping1 = Product.objects.filter(Category=category,subCategory=23,medium="Science")
#     helping2 = Product.objects.filter(Category=category,subCategory=23,medium="Commerce")
#     helping3 = Product.objects.filter(Category=category,subCategory=23,medium="Arts")
#     set1 = Product.objects.filter(Category=4,subCategory=23,medium="Science")
#     set2 = Product.objects.filter(Category=4,subCategory=23,medium="Commerce")
#     set3 = Product.objects.filter(Category=4,subCategory=23,medium="Arts")
#     cats = Category.objects.filter(id=myid)
#     param ={'cat': cats,'combo1':combos1,'combo2':combos2,'combo3':combos3,'textbook1':textbook1,'textbook2':textbook2,'textbook3':textbook3,'digest1':digest1,'digest2':digest2,'digest3':digest3,'set1':set1,'set2':set2,'set3':set3,'helping1':helping1,'helping2':helping2,'helping3':helping3}
#     return render(request,'ecom/product-listing3.html',param)


# def Category3(request,myid):
#     category=myid
#     subcat1 = 1
#     subcat2 = 2
#     subcat3 = 13
#     combos1 = Product.objects.filter(Category=category,subCategory=subcat3,medium="First Year")
#     combos2 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Second Year")
#     combos3 = Product.objects.filter(Category=category,subCategory=subcat3,medium="Third Year")
#     textbook1 = Product.objects.filter(Category=category,subCategory=subcat1,medium="First Year")
#     textbook2 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Second Year")
#     textbook3 = Product.objects.filter(Category=category,subCategory=subcat1,medium="Third Year")
#     digest1 = Product.objects.filter(Category=category,subCategory=subcat2,medium="First Year")
#     digest2 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Second Year")
#     digest3 = Product.objects.filter(Category=category,subCategory=subcat2,medium="Third Year")
#     helping1 = Product.objects.filter(Category=category,subCategory=23,medium="First Year")
#     helping2 = Product.objects.filter(Category=category,subCategory=23,medium="Second Year")
#     helping3 = Product.objects.filter(Category=category,subCategory=23,medium="Third Year")
#     cats = Category.objects.filter(id=myid)
#     param ={'cat': cats,'combo1':combos1,'combo2':combos2,'combo3':combos3,'textbook1':textbook1,'textbook2':textbook2,'textbook3':textbook3,'digest1':digest1,'digest2':digest2,'digest3':digest3,'helping1':helping1,'helping2':helping2,'helping3':helping3}
#     return render(request,'ecom/product-listing4.html',param)

# def Category4(request,myid):
#     category=myid
#     subcat1 = 15
#     subcat2 = 16
#     subcat3 = 17
#     subcat4 = 18
#     subcat5 = 19
#     subcat6 = 20
#     subcat7 = 21
#     subcat8 = 22
#     Subcat1 = Product.objects.filter(Category=category,subCategory=subcat1,medium="English")
#     Subcat2 = Product.objects.filter(Category=category,subCategory=subcat2,medium="English")
#     Subcat3 = Product.objects.filter(Category=category,subCategory=subcat3,medium="English")
#     Subcat4 = Product.objects.filter(Category=category,subCategory=subcat4,medium="English")
#     Subcat5 = Product.objects.filter(Category=category,subCategory=subcat5,medium="English")
#     Subcat6 = Product.objects.filter(Category=category,subCategory=subcat6,medium="English")
#     Subcat7 = Product.objects.filter(Category=category,subCategory=subcat7,medium="English")
#     Subcat8 = Product.objects.filter(Category=category,subCategory=subcat8,medium="English")
#     cats = Category.objects.filter(id=myid)
#     param ={'cat':cats,'Subcat1':Subcat1,'Subcat2':Subcat2,'Subcat3':Subcat3,'Subcat4':Subcat4,'Subcat5':Subcat5,'Subcat6':Subcat6,'Subcat7':Subcat7,'Subcat8':Subcat8,}
#     return render(request,'ecom/product-listing5.html',param)

# def Productdetails(request,id):
#     product=Product.objects.filter(id=id)
#     products = Product.objects.filter(Category=1)
#     param = {'product': product[0],'products': products}
#     return render(request,'ecom/product-detail.html',param)

# def cart(request):
#     return render(request,'ecom/empty-cart.html')

# def wishlist(request):
#     return render(request,'ecom/wishlist.html')

# def aboutus(request):
#     return render(request,'ecom/aboutus.html')

# def policies(request):
#     return render(request,'ecom/policies.html')

# def requestbook(request):
#     context = {}
#     if request.method == 'POST':
#         form = RequestForm(request.POST)
#         if form.is_valid():
#             email= form.cleaned_data['email']
#             raw_password = form.cleaned_data['password1']
#             phone = form.cleaned_data['phone_number']
#             username = form.cleaned_data['username']
#             pincode = form.cleaned_data['pincode']
#             Customer.email = email
#             Customer.Cust_Name = username
#             Customer.phone_number = phone
#             Customer.pincode = pincode
#             Customer.set_password(raw_password)
#             Customer.save()

#         fm = RequestForm()
#         context = {'form':fm}
#         return render(request, 'ecom/request-book.html',context)

#     else:
#         fm = RequestForm()
#         context={'form':fm}
#         return render(request,'ecom/request-book.html',context)

# def myorders(request):
#     return render(request,'ecom/myorders.html')

# def myaccount(request):
#     return render(request,'ecom/myaccount.html')

# def mycart(request):
#     return render(request,'ecom/mycart.html')

# def myaddressbook(request):
#     return render(request,'ecom/myaddressbook.html')

# def payment(request):
#     return render(request,'ecom/payment.html')

# def orderplaced(request):
#     return render(request,'ecom/orderplaced.html')

# def editaddress(request):
#     return render(request,'ecom/productlisting.html')

# def ordercancelation(request):
#     return render(request,'ecom/ordercancelation.html')

# def returnandexchange(request):
#     return render(request,'ecom/returnandexchange.html')

# def faq(request):
#     return render(request,'ecom/faq.html')

# def privacy(request):
#     return render(request,'ecom/privacy.html')

# def termsandcondition(request):
#     return render(request,'ecom/termsandcondition.html')

