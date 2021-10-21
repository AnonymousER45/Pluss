from decimal import Context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Category,Product,Banner,Requestbook,CartProduct,Cart, EcomOrder, WishlistProduct
from Accounts.models import Address, Customer
from math import ceil
from .forms import  RequestForm


def Index(request):
    products1 = Product.objects.filter(Category=1)[:10]
    products2 = Product.objects.filter(isBestSeller=True).order_by('-id')[:10]
    products3 = Product.objects.filter(Category=10)
    products4 = Product.objects.filter(Category=9)
    products5 = Product.objects.filter(Category=8)
    products6 = Product.objects.filter(Category=7)

    ban = Banner.objects.all()
    param ={'product1': products1,'product2': products2,'product3': products3,'product4': products4,'product5': products5,'product6': products6,'banner':ban,}
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
    if request.user.is_authenticated:
        total_items(request)
        wishlisted = wishlisted_ids(request.user)
        param['wishlisted_ids'] = wishlisted 
    
    return render(request,'ecom/product-listing-3.html',param)

def Category4(request,myid):
    category=myid
    category2=7
    Prod1 = Product.objects.filter(Category=category,subCategory=11)
    Prod2 = Product.objects.filter(Category=category,subCategory=10)
    Prod3 = Product.objects.filter(Category=category,subCategory=12)
    Prod4 = Product.objects.filter(Category=category2,subCategory=24)
    Prod5 = Product.objects.filter(Category=category2,subCategory=25)
    cats = Category.objects.filter(id=myid)
    param ={'cat': cats,'Prod1':Prod1,'Prod2':Prod2,'Prod3':Prod3,'Prod4':Prod4,'Prod5':Prod5,}
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
        products.remove("")
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


def showall(request):
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
    
    return render(request,'ecom/productshowall.html',param)
 


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


def payment(request,order_id):
    return render(request,'ecom/payment.html')

def orderplaced(request,order_id):
    id = order_id
    param={"order_id":id}
    return render(request,'ecom/orderplaced.html',param)

def add_address(request):
    return render(request,'ecom/add_address.html')

def edit_address(request):
    return render(request,'ecom/edit_address.html')

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
    return render(request,'ecom/addresbook.html',context)

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