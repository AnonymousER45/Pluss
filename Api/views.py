from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from hashids import Hashids
#import smtplib
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
from Accounts.models import Customer,Address ,OTP,OTPmail,Pincode,Coupon,Attendance
from Ecom.models import Product ,Category,Cart,CartProduct,Wishlist,WishlistProduct,subCategory,Banner,ProductUnavailable,Requestbook,EcomOrder
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render
from django.db import IntegrityError
from django.http.response import JsonResponse
from .serializers import ProductSerializer,CategorySerializer,CustomerSerializer,AddressSerializer,subCategorySerializer,BannerSerializer,ProductUnavailableSerializer,RequestbookSerializer,PincodeSerializer
from .otp import generateOTP, generatingOTP,forgotpassOTP
from django.utils.datastructures import MultiValueDictKeyError
#from .CODOTP import generateOTP, generatingOTP
from .mailotp import generatemailOTP, generatingmailOTP
#from .cod import generateOTP, generatingOTP
#from .sendmsg import sendmessage
from django.db.models import Value
from django.db.models.functions import Concat
from decimal import *
from datetime import date,timedelta
import datetime


@api_view(['POST'])
def register_customer(request):

    if 'username' in request.data:
        user_name = request.data['username']
    else:
        return Response({"Error": "Username Not Provided"})

    if 'fname' in request.data:
        fname = request.data['fname']
    else:
        return Response({"Error": "First Name not Provided"})

    if 'lname' in request.data:
        lname = request.data['lname']

    if 'email' in request.data:
        email = request.data['email']
    else:
        return Response({"Error": "Email Not Provided"})

    if 'number' in request.data:
        phone_number = request.data['number']
    else:
        return Response({"Error": "Contact Number Not Provided"})

    if 'password' in request.data:
        password = request.data['password']
    else:
        return Response({"Error": "Password Not Provided"})

    if 'pincode' in request.data:
        pincode = request.data['pincode']
    else:
        return Response({"Error": "Pincode Not Provided"})


    customer = Customer(email=email)
    customer.username = user_name
    customer.phone_number = phone_number
    customer.first_name = fname
    customer.last_name = lname
    customer.pincode = pincode
    customer.set_password(password)
    try:
        customer.save()
        return Response({"registerStatus": True, "IntegrityError": False})
    except IntegrityError as e:
        return Response({"registerStatus": False, "IntegrityError": True})



@api_view(['PUT'])
def update_customer(request):

    if 'username' in request.data:
        new_user_name = request.data['username']
    else:
        return Response({"Error": "Username Not Provided"})

    if 'fname' in request.data:
        new_fname = request.data['fname']
    else:
        return Response({"Error": "First Name not Provided"})

    if 'lname' in request.data:
        new_lname = request.data['lname']
    else:
        return Response({"Error": "Last Name not Provided"})

    if 'email' in request.data:
        email = request.data['email']
    else:
        return Response({"Error": "Email Not Provided"})

    if 'number' in request.data:
        new_phone_number = request.data['number']
    else:
        return Response({"Error": "Contact Number Not Provided"})

    try:
        customer = Customer.objects.get(email=email)
        customer.username = new_user_name
        customer.phone_number = new_phone_number
        customer.first_name = new_fname
        customer.last_name = new_lname
#        customer.set_password(new_password)
        customer.save()
        return Response({"status": True})

    except Customer.DoesNotExist as e:

        return Response({"status": False, "Error ": "Customer does not exist"})


@api_view(['POST'])
def customer_login(request):
    email = request.data["email"]
    password = request.data["password"]
    # it will  match customer email address from Table
    customer = Customer.objects.get(email=email)

        # check password from table and assign a session or auth_token.
    if customer.check_password(password):
        refresh = RefreshToken.for_user(customer)
        return Response({"status": True, "is_admin": False, "refresh": str(refresh), "access": str(refresh.access_token), "loggedIn": str(customer.username), "id": customer.pk,"pincode":str(customer.pincode)})
    else:
        return Response({"status": False})


@api_view(['POST'])
def staff_login(request):
    email = request.data["email"]
    password = request.data["password"]
    # it will  match customer email address from Table
    customer = Customer.objects.get(email=email)

    if customer.is_staff:
        # check password from table and assign a session or auth_token.
        if customer.check_password(password):
            refresh = RefreshToken.for_user(customer)
            return Response({"status": True, "is_Staff": True, "refresh": str(refresh), "access": str(refresh.access_token), "loggedIn": str(customer.username), "id": customer.pk})
        else:
            return Response({"status": False ,"integrety error":True})    # check password from table and assign a session or auth_token.
    else:
        return Response({"status": False,"integrety error":False})


@api_view(['PUT'])
def change_password(request):
    id = request.data['id']
    passwordnew = request.data['new_password']
    customer_object = Customer.objects.get(id=id)
    customer_object.set_password(passwordnew)
    customer_object.save()
    try:
        return Response({'msg': 'password update Successfully'})
    except customer_object.DoesNotExist as e:
        return Response({"status": False, "Error ": "Customer does not exist"})


@api_view(['PUT'])
def password_reset(request):
    email = request.data['email']
    person = Customer.objects.get(email=email)
    person.set_password(request.data['password'])
    person.save()
    try:
        return Response({'msg': 'password update Successfully'})
    except Exception as e:
        print(str(e))

    except Customer.DoesNotExist as e:
        return Response({"status": False, "message": "Customer does not exist"})



# Product functionality
# get products
@api_view(['GET'])
@csrf_exempt
def get_products(request):
        query_set = Product.objects.all()
        serializer_object = ProductSerializer(query_set, many=True)

        return Response(serializer_object.data)

# get products by id
@api_view(['POST'])
@csrf_exempt
def get_product_by_id(request):
        if 'id' in request.data:
            id = request.data['id']
        else:
            return Response({"Error": "product_id not Provided"})

        query_set = Product.objects.filter(id=id)
        serializer_object = ProductSerializer(query_set, many=True)

        return Response(serializer_object.data)

# get products by category
@api_view(['POST'])
@csrf_exempt
def get_Products_by_Category(request):
        if 'category_id' in request.data:
            id = request.data['category_id']
        else:
            return Response({"Error": "product_id not Provided"})

        query_set = Product.objects.filter(Category=id)
        serializer_object = ProductSerializer(query_set, many=True)

        return Response(serializer_object.data)


#get product by subcat
@api_view(['POST'])
@csrf_exempt
def get_Products_by_SubCategory(request):
        if 'cat' in request.data:
            cat_id = request.data['cat']
        else:
            return Response({"Error": "Category_id not Provided"})

        if 'sub_cat' in request.data:
            subCategory_id = request.data['sub_cat']
        else:
            return Response({"Error": "Sub Category not Provided"})

        query_set = Product.objects.filter(Category=cat_id,subCategory=subCategory_id)
        serializer_object = ProductSerializer(query_set, many=True)

        return Response(serializer_object.data)


#get product by branch
@api_view(['POST'])
@csrf_exempt
def get_Products_by_medium(request):
        if 'cat' in request.data:
            cat_id = request.data['cat']
        else:
            return Response({"Error": "Category_id not Provided"})

        if 'sub_cat' in request.data:
            subCategory_id = request.data['sub_cat']
        else:
            return Response({"Error": "Sub Category not Provided"})

        if 'medium' in request.data:
            medium = request.data['medium']
        else:
            return Response({"Error": "Medium not Provided"})

        query_set = Product.objects.filter(Category=cat_id,subCategory=subCategory_id,medium=medium)
        serializer_object = ProductSerializer(query_set, many=True)

        return Response(serializer_object.data)


#get product by branch
@api_view(['POST'])
@csrf_exempt
def get_Products_by_filter(request):
        if 'option' in request.data:
            option = request.data['option']
        else:
            return Response({"Error": "Filter option not Provided"})

        if 'sub_cat' in request.data:
            subCategory_id = request.data['sub_cat']
        else:
            return Response({"Error": "Sub Category not Provided"})


        if option == "1":
            # for B.A Hindi
            query_set = Product.objects.filter(Category=28,subCategory=subCategory_id,medium="Third Year")
        elif option == "2":
            # for B.A English
            query_set = Product.objects.filter(Category=29,subCategory=subCategory_id,medium="Third Year")
        elif option == "3":
            # for B.A Marathi
            query_set = Product.objects.filter(Category=30,subCategory=subCategory_id,medium="Third Year")
        elif option == "4":
            # for B.A History
            query_set = Product.objects.filter(Category=31,subCategory=subCategory_id,medium="Third Year")
        elif option == "5":
            # for B.A Geography
            query_set = Product.objects.filter(Category=32,subCategory=subCategory_id,medium="Third Year")
        elif option == "6":
            # for B.A Sanskrit
            query_set = Product.objects.filter(Category=33,subCategory=subCategory_id,medium="Third Year")
        elif option == "7":
            # for B.A Literature
            query_set = Product.objects.filter(Category=34,subCategory=subCategory_id,medium="Third Year")
        else:
            query_set = Product.objects.filter(Category__in=[28,29,30,31,32,33,34],subCategory=subCategory_id,medium="Third Year")
        serializer_object = ProductSerializer(query_set, many=True)
        return Response(serializer_object.data)


# get products
@api_view(['GET'])
@csrf_exempt
def get_new_arrivals(request):
        query_set = Product.objects.all().order_by('-id')[:10]
        serializer_object = ProductSerializer(query_set, many=True)

        return Response(serializer_object.data)

@api_view(['GET'])
@csrf_exempt
def get_new_bestseller(request):
        query_set = Product.objects.filter(isBestSeller=True).order_by('-id')[:10]
        serializer_object = ProductSerializer(query_set, many=True)

        return Response(serializer_object.data)

# get search product
@api_view(['POST'])
@csrf_exempt
def search(request):
        if 'keyword' in request.data:
            keyword = request.data['keyword']
        else:
            return Response({"Error": "Somethings went Wrong Plz Try again"})

        query_set = Product.objects.filter(title_extact=keyword)
        serializer_object = ProductSerializer(query_set, many=True)

        return Response(serializer_object.data)


@api_view(['GET'])
@csrf_exempt
def get_home_banners(request):
        query_set = Banner.objects.all()
        serializer_object = BannerSerializer(query_set, many=True)

        return Response(serializer_object.data)



## category functionality
#get all category
@api_view(['GET'])
def get_Category(request):
        query_set = Category.objects.all()
        serializer_object = CategorySerializer(query_set, many=True)

        return Response(serializer_object.data)

## category functionality
#get all subcategory
@api_view(['GET'])
def get_SubCategory(request):
        query_set = subCategory.objects.all()
        serializer_object = subCategorySerializer(query_set, many=True)

        return Response(serializer_object.data)



#view cart of the user
@api_view(['POST'])
def get_cart_details(request):
    userx = request.data['id']
    query_set = CartProduct.objects.filter(user=userx)
    print(request.data)
    product_data = []
    result = []
    price = 0
    mrp = 0
    no_of_item=0
    delivery_charge=30
    giftcharge=0
    discount=0
    inline_total = 0
    for items in query_set:
        price = price + items.Product.price
        mrp = mrp+ items.Product.mrp
        inline_total = price * items.product_quan 
        product_data.append({
            'product_name': items.Product.title,
            'product_price': items.Product.price,
            'product_id' : items.Product.id,
            'product_image': str(items.Product.img),
            'product_discountoff':items.Product.discount_per,
            'product_isavailable':items.Product.instock,
            'product_mrp':items.Product.mrp,
            'product_isExchangeable': items.Product.isExchnageable,
            'product_isReturnable' : items.Product.isReturnable,
            'product_quantity': items.product_quan,
            'bind_price' : items.Product.bind_price,


            })
        no_of_item=+1

    saving = mrp-price
    if price > 300:
        delivery_charge=0


    total = inline_total+delivery_charge
    total = total-discount

    result.append(
        {
            'cart_owner_id': userx,
            'product': product_data,
            'cart_price': str(price),
            'cart_mrp': str(mrp),
            'cart_saving': str(saving),
            'cart_delivery': str(delivery_charge),
            'no_of_product': str(no_of_item),
            'coupons_discount': str(discount),
            'gifting_charges' : str(giftcharge),

            'cart_total_amount':str(total)
        }
    )

    return JsonResponse(result,safe=False)


#update gift message
@api_view(['PUT'])
def update_gift_msg(request):
    cart_user = Cart.objects.get(user_id=request.data['id'])
    user_instance = Customer.objects.get(id=request.data['id'])
    product_instance = Product.objects.get(id=request.data['product_id'])
    gm = request.data['gift_msg']
    sender = request.data['gift_from']
    cartproduct = CartProduct.objects.get(user=user_instance, Product=product_instance,cart=cart_user)
    cartproduct.gift_message = gm
    cartproduct.gift_from = sender
    cartproduct.save()
    return Response({"msg": "Gift information updated"})

   

#add product to the cart
@api_view(['POST'])
def add_to_cart(request):
    try:
        cart_user = Cart.objects.get(user_id=request.data['id'])
        user_instance = Customer.objects.get(id=request.data['id'])
        product_instance = Product.objects.get(id=request.data['product_id'])
        is_binding = request.data['is_binding']
        qs = CartProduct.objects.filter(user=user_instance, Product=product_instance)
        if qs.exists() :
            cartproduct = CartProduct.objects.get(user=user_instance, Product=product_instance,cart=cart_user)
            cartproduct.product_quan += 1
            cartproduct.is_binding = is_binding
            cartproduct.save()
            return Response({"msg": "Quantity updated"})
        else:
            cart = CartProduct(user=user_instance,Product=product_instance,is_binding=is_binding,cart=cart_user)
            cart.save()
        return Response({"msg": "Item added to the Cart "})

    except Cart.DoesNotExist as e:
        user_instance = Customer.objects.get(id=request.data['id'])
        new_cart_user = Cart(user_id=user_instance)
        new_cart_user.save()
        user_instance = Customer.objects.get(id=request.data['id'])
        product_instance = Product.objects.get(id=request.data['product_id'])
        cart = CartProduct(user=user_instance,
                           Product=product_instance,cart=new_cart_user)
        cart.save()
        return Response({"msg": "Item added to the Cart "})

#decrase quantity of product
@api_view(['PUT'])
def decrease_product_quan(request):
    user_instance = Customer.objects.get(id=request.data['id'])
    product_instance = Product.objects.get(id=request.data['product_id'])
    cart_user = Cart.objects.get(user_id=request.data['id'])
    qs = CartProduct.objects.filter(user=user_instance, Product=product_instance)
    if qs.exists() :
        cartproduct = CartProduct.objects.get(user=user_instance, Product=product_instance,cart=cart_user)
        cartproduct.product_quan -= 1
        cartproduct.save()
        return Response({"msg": "Quantity updated"})

#Remove product from  cart
@csrf_exempt
@api_view(['POST'])
def remove_from_cart(request):
    user_instance = Customer.objects.get(id=request.data['id'])
    cart_user = Cart.objects.get(user_id=user_instance)
    product_instance = Product.objects.get(id=request.data['product_id'])

    cart = CartProduct.objects.filter(
        user=user_instance, Product=product_instance, cart=cart_user)
    cart.delete()
    return Response({"msg": "Item Deleted"})

#Remove all product from  cart
@csrf_exempt
@api_view(['POST'])
def empty_cart(request):
    user_instance = Customer.objects.get(id=request.data['id'])
    cart_user = Cart.objects.get(user_id=user_instance)
    cart = Cart.objects.filter(
        user_id=user_instance)
    cart.delete()
    return Response({"msg": "All Item Deleted"})


#add_address
@api_view(['POST'])
def add_address(request):
    if 'customer_id' in request.data:
        customer_id = request.data['customer_id']
    else:
        return Response({"Error": "Expected 'Customer ID' "})

    if 'name' in request.data:
        name = request.data['name']
    else:
        return Response({"Error": "Expected 'Name' "})

    if 'city' in request.data:
        city = request.data['city']
    else:
        return Response({"Error": "Expected 'City' "})

    if 'line1' in request.data:
        line1 = request.data['line1']
    else:
        return Response({"Error": "Expected 'Line1' "})

    if 'line2' in request.data:
        line2 = request.data['line2']
    else:
        return Response({"Error": "Expected 'Line2' "})

    if 'line3' in request.data:
        line3 = request.data['line3']
    else:
        return Response({"Error": "Expected 'Line3' "})

    if 'addtype' in request.data:
        addtype = request.data['addtype']
    else:
        return Response({"Error": "Expected 'addtype not provided ' "})

    if 'addpincode' in request.data:
        addpincode = request.data['addpincode']
    else:
        return Response({"Error": "Expected 'Pincode  is not  Provided' "})

    if 'number' in request.data:
        number = request.data['number']
    else:
        return Response({"Error": "Contact Number Not Provided"})

    serializer_object = AddressSerializer(data=request.data)
    if serializer_object.is_valid():
        serializer_object.save()
        return Response({"status": True, "message": "Address added successfully"})
    else:
        return Response(serializer_object.errors)


@api_view(['PUT'])
def update_address(request):

    if 'id' in request.data:
        id = request.data['id']
    else:
        return Response({"Error": "Expected 'Address ID' "})

    if  'customer_id' in request.data:
        customer_id = request.data['customer_id']
    else:
        return Response({"Error": "Expected 'Customer ID' "})

    if 'name' in request.data:
        name = request.data['name']
    else:
        return Response({"Error": "Expected 'Name' "})

    if 'city' in request.data:
        city = request.data['city']
    else:
        return Response({"Error": "Expected 'City' "})

    if 'line1' in request.data:
        line1 = request.data['line1']
    else:
        return Response({"Error": "Expected 'Line1' "})

    if 'line2' in request.data:
        line2 = request.data['line2']
    else:
        return Response({"Error": "Expected 'Line2' "})

    if 'line3' in request.data:
        line3 = request.data['line3']
    else:
        return Response({"Error": "Expected 'Line3' "})

    if 'addtype' in request.data:
        addtype = request.data['addtype']
    else:
        return Response({"Error": "Expected 'addtype not provided ' "})

    if 'addpincode' in request.data:
        addpincode = request.data['addpincode']
    else:
        return Response({"Error": "Expected 'Pincode  is not  Provided' "})

    if 'number' in request.data:
        number = request.data['number']
    else:
        return Response({"Error": "Contact Number Not Provided"})


    try:
        address_to_be_updated = Address.objects.get(id=id)
        serializer_object = AddressSerializer(
            address_to_be_updated, request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response({"status": True, "message": "Address updated successfully"})
        else:
            return Response(serializer_object.errors)

    except Address.DoesNotExist as e:
        return Response({"status": false, "message": "Address does not exist"})


@api_view(["GET"])
def get_address(request,id):
    try:
        query_set = Address.objects.filter(customer_id=id)
        serializer_object = AddressSerializer(query_set, many=True)
        if query_set:
            return Response(serializer_object.data)
        else:
            return Response({"status":False,"message":"Address does not exist for user"})
    except Customer.DoesNotExist as e:
        return Response({"status": False, "message": "Customer does not exist"})


@api_view(["POST"])
def remove_address(request):
    if 'add_id' in request.data:
        id = request.data['add_id']
    else:
        return Response({"Error": "Expected 'Address ID' "})

    try:
        addbook = Address.objects.filter(id=id)
        addbook.delete()
        return Response({"msg": "Address Deleted"})


    except Customer.DoesNotExist as e:
        return Response({"status": False, "message": "Customer does not exist"})

@api_view(["POST"])
def remove_all_address(request):
    if 'id' in request.data:
        id = request.data['id']
    else:
        return Response({"Error": "Expected 'Customer ID' "})

    try:
        addbook = Address.objects.filter(customer_id=id)
        addbook.delete()
        return Response({"msg": "Address Deleted"})

    except Address.DoesNotExist as e:
        return Response({"status": False, "message": "Address does not exist"})




    #add product to the Wishlist
@api_view(['POST'])
def add_to_wishlist(request): 
    try: 
        wishlist_user = Wishlist.objects.get(user_id=request.data['id']) 
        user_instance = Customer.objects.get(id=request.data['id']) 
        product_instance = Product.objects.get(id=request.data['product_id']) 
        try: 
            wishlist = WishlistProduct.objects.get(userx=user_instance, 
                        Product=product_instance, wishlist=wishlist_user) 
        except WishlistProduct.DoesNotExist as e: 
            wishlist = WishlistProduct(userx=user_instance,Product=product_instance, wishlist=wishlist_user) 
            wishlist.save() 
        return Response({"msg": "Item added to the you Wishlist"}) 
 
    except Wishlist.DoesNotExist as e: 
        user_instance = Customer.objects.get(id=request.data['id']) 
        new_wishlist_user = Wishlist(user_id=user_instance) 
        new_wishlist_user.save() 
        user_instance = Customer.objects.get(id=request.data['id']) 
        product_instance = Product.objects.get(id=request.data['product_id']) 
        wishlist = WishlistProduct(userx=user_instance, 
                           Product=product_instance, wishlist=new_wishlist_user) 
        wishlist.save() 
        return Response({"msg": "Item added to the your Wishlist "})

#Remove product from  wishlist
@csrf_exempt
@api_view(['POST'])
def remove_from_wishlist(request):
    user_instance = Customer.objects.get(id=request.data['id'])
    wishlist_user = Wishlist.objects.get(user_id=user_instance)
    product_instance = Product.objects.get(id=request.data['product_id'])

    wishlist = WishlistProduct.objects.filter(
        userx=user_instance, Product=product_instance, wishlist=wishlist_user)
    wishlist.delete()
    return Response({"msg": "Item Removed From Wishlist"})


#Remove all product from  wishlist
@csrf_exempt
@api_view(['POST'])
def empty_wishlist(request):
    user_instance = Customer.objects.get(id=request.data['id'])
    wishlist_user = Wishlist.objects.get(user_id=user_instance)

    wishlist = WishlistProduct.objects.filter(
        userx=user_instance, wishlist=wishlist_user)
    wishlist.delete()
    return Response({"msg": "All Item Removed From Wishlist"})


#view cart of the user
@api_view(['POST'])
def get_wishlist(request):
    user_instance = Customer.objects.get(id=request.data['id'])
    query_set = WishlistProduct.objects.filter(userx=user_instance)
    print(request.data)
    Product_data = []
    result = []
    for item in query_set:
        Product_data.append({
            'product_name': item.Product.title,
            'product_price': item.Product.price,
            'product_id' : item.Product.id,
            'product_image': str(item.Product.img),
            'product_discountoff':item.Product.discount_per,
            'product_isavailable':item.Product.instock,
            'product_mrp':item.Product.mrp,
        })

    result.append(
        {
            'wishlist_owner_id': request.data['id'],
            'product': Product_data
        }
    )
    return JsonResponse(result, safe=False)

@api_view(['POST'])
def user_details(request):
    email = request.data["email"]
    password = request.data["password"]
    # it will  match customer email address from Table
    customer = Customer.objects.get(email=email)

        # check password from table and assign a session or auth_token.
    if customer.check_password(password):
        refresh = RefreshToken.for_user(customer)
        return Response({"status": True, "is_admin": False, "refresh": str(refresh), "access": str(refresh.access_token), "loggedIn": str(customer.username), "id": customer.pk
        ,"Firstname":str(customer.first_name),"Lastname":str(customer.last_name),"Phone":str(customer.phone_number),"Email":str(customer.email)})
    else:
        return Response({"status": False})



@api_view(['POST'])
def search(request):
    keyword = request.data["keyword"]
    query_set = Product.objects.filter(title__icontains=keyword)[:30]
    #query_set = Product.objects.all().order_by('-id')[:10]
    serializer_object = ProductSerializer(query_set, many=True)

    return Response(serializer_object.data)


@api_view(['POST'])
def generate_otp(request):
    if 'number' in request.data:  # Checks whether the nuber is present in the request body
        # checks weather the number present in the request body is of 10-Digit
        if len(request.data['number']) == 10:
            number = request.data['number']
        else:
            return Response({"Error": "Mobile Number should be of 10-digits", "isOTPSent": False})
    else:
        return Response({"Error": "Expected phone number in request body not present", "isOTPSent": False})

    generatedOTP = generatingOTP(number)
    print("hi")
    # Generates the 4-Digit OTP
    if generatedOTP:
        data = OTP(phone_number=number, otp=generatedOTP)
        data.save()
        print(generatedOTP)
        return Response({"isOTPSent": True})
    else:
        return Response({"isOTPSent": False})


@api_view(['POST'])
def forgotpassotp(request):

    if 'number' in request.data:
        number = request.data['number']

    forgotOTP = forgotpassOTP(number)
    print("hi")
    # Generates the 4-Digit OTP
    if forgotOTP:
        data1 = OTP(phone_number=number, otp=forgotOTP)
        data1.save()
        print(forgotOTP)
        return Response({"isOTPSent": True})
    else:
        return Response({"isOTPSent": False})

@api_view(['PUT'])
def check_otp(request):
    # validations for Checking if the request.data has what we need
    if 'number' in request.data:
        numbers = request.data['number']

    if 'otp' in request.data:
        otp = request.data['otp']

    generatedOTP = OTP.objects.filter(phone_number=numbers).values_list('otp').order_by('-id')[:1]
    if generatedOTP[0][0] == otp:
        try:
            data = OTP.objects.get(phone_number=numbers,otp=otp)
            data.is_verfied = True
            data.save()

        except OTP.DoesNotExist as error:
            return Response({"Error": error})



        return Response({"checkStatus": True ,"number is verified":True })
    else:
        return Response({"checkStatus": False ,"number is verified":True })

#add_productUnavailbale requests
@api_view(['POST'])
def add_ProductUnavailable(request):
    if 'product_id' in request.data:
        product_id = request.data['product_id']
    else:
        return Response({"Error": "Expected 'Product ID' "})

    if 'mail_id' in request.data:
        mail_id = request.data['mail_id']
    else:
        return Response({"Error": "Expected 'Customers Mail ID' "})

    productunavailable = ProductUnavailable(Product=product_id,customer_mail_id=mail_id)
    productunavailable.save()
    return Response({"status": True, "message": "Product Unavailablity Informed successfully To Admin"})



@api_view(['POST'])
def generate_mail_otp(request):
    if 'mail' in request.data:  # Checks whether the nuber is present in the request body
        # checks weather the number present in the request body is of 10-Digit
        mailid = request.data['mail']
    else:
        return Response({"Error": "Expected Mail id in request body not present", "isOTPSent": False})

    generatedOTP = generatingmailOTP(mailid)
    print("hi")
    # Generates the 4-Digit OTP
    if generatedOTP:
        data = OTPmail(mailid=mailid, otp=generatedOTP)
        data.save()
        print(generatedOTP)
        return Response({"isOTPSent": True})
    else:
        return Response({"isOTPSent": False})


@api_view(['PUT'])
def check_mailotp(request):

    if 'mail' in request.data:
        mail = request.data['mail']

    if 'otp' in request.data:
        otpr = request.data['otp']

    generatedOTP = OTPmail.objects.filter(mailid=mail).values_list('otp').order_by('-id')[:1]
    if generatedOTP[0][0] == otpr:

        try:
            data = OTPmail.objects.get(mailid=mail,otp=otpr)

        except OTPmail.DoesNotExist as error:
            return Response({"Error": error})

        data.is_verfied = True
        data.save()
        return Response({"checkStatus": True})
    else:
        return Response({"checkStatus": False})


@api_view(['POST'])
def Requestbook(request):
    if 'book_name' in request.data:
        book_name = request.data['book_name']
    else:
        return Response({"Error": "Expected 'book_name' "})

    if 'book_type' in request.data:
        book_type = request.data['book_type']
    else:
        return Response({"Error": "Expected 'book_type' "})

    if 'book_relatedto' in request.data:
        book_relatedto = request.data['book_relatedto']
    else:
        return Response({"Error": "Expected 'book_relatedto' "})

    if 'book_desp' in request.data:
        book_desp = request.data['book_desp']
    else:
        return Response({"Error": "Expected 'Line1' "})

    if 'book_img' in request.data:
        book_img = request.data['book_img']

    if 'book_required' in request.data:
        book_required = request.data['book_required']
    else:
       return Response({"Error": "Expected 'book_required' "})

    if 'customer_name' in request.data:
        customer_name = request.data['customer_name']
    else:
        return Response({"Error": "Expected 'customer_name is not Provided' "})

    if 'author_name' in request.data:
        author_name = request.data['author_name']

    if 'customer_phone' in request.data:
        customer_phone = request.data['customer_phone']
    else:
        return Response({"Error": "Expected 'customer_phone  is not  Provided' "})

    if 'customer_mail_id' in request.data:
        customer_mail_id = request.data['customer_mail_id']
    else:
        return Response({"Error": "Expected 'customer_mail_id is not  Provided' "})

    if 'ispriority' in request.data:
        ispriority = request.data['ispriority']
    else:
        return Response({"Error": "Expected 'ispriority  is not  Provided' "})

    serializer_object = RequestbookSerializer(data=request.data)
    if serializer_object.is_valid():
        serializer_object.save()
        return Response({"status": True, "message": "Book Requested Successfully"})
    else:
        return Response(serializer_object.errors)


@api_view(['GET'])
@csrf_exempt
def get_pincode(request):
        query_set = Pincode.objects.all()
        serializer_object = PincodeSerializer(query_set, many=True)

        return Response(serializer_object.data)

@api_view(['POST'])
def partial_order(request):
    result = []
    user = request.data.get('id')
    address_id = request.data.get('address_id','')
    is_gift = request.data.get('isgift',False)
    if is_gift:
        gift_message = request.data.get('gift_message','')
        gift_from = request.data.get('gift_from','')
        gift_box = request.data.get('gift_box',False)

    cus = Customer.objects.get(id=user)
    qs_cart_items = CartProduct.objects.filter(user=user)
    if address_id:
        address_set = Address.objects.get(id=address_id)
    if not address_id or not address_set:
        address_set = Address.objects.filter(customer_id=user).first()

    total_products, cart_total_price = 0,0
    products = ""
    status = 1
    for item in qs_cart_items:
        cart_total_price += item.Product.price
        total_products = total_products + 1
        products = item.Product.title + ":" + \
            str(item.Product.price) +":"+str(item.Product.img) + ", " + products
    if is_gift:
        cart_total_price += 50
        if gift_box:
            cart_total_price += 30
    
    # for address2 in address_set:
    address =  address_set.line1 + ":" + address_set.line2 + ":" + ":" + address_set.city + ":" + address_set.addtype+ ":" +str(address_set.addpincode)
    contact_no = address_set.number
    contact_name = address_set.name
    order = EcomOrder(Order_placed_BY=cus,
                  total_products=total_products,
                  order_total = cart_total_price,
                  payment_mode= '',
                  products=products,
                  address= address,
                  gift_message =gift_message,
                  gift_from = gift_from,
                  contact_name=contact_name,
                  contact_no=contact_no,
                  order_status=status)
    order.save()
    result = {
        "order_id": order.id,
        "order_placed_by": order.Order_placed_BY.id,
        "total_products": order.total_products,
        "order_total": order.order_total,
        "date_of_ordering": order.date_of_ordering,
        "date_of_delivery": order.date_of_delivery,
        "address":order.address,
        "Contact_Name": order.contact_name,
        "Contact_Number": order.contact_no,
        "payment_mode":order.payment_mode,
        "products":order.products,
        "order_status":order.order_status,
        "order_completed": False
    }
    print(result)
    return Response(result)

@api_view(['POST'])
def place_order(request):
    query_set = CartProduct.objects.filter(user=request.data['id'])
    applied_coupon = Coupon.objects.get(code=request.data['code'])    
    address_set = Address.objects.filter(id = request.data['address_id'])
    gift_message = request.data['gift_message']
    gift_from = request.data['gift_from']
    result = []
    address_data = []
    order_total = 0
    total_products = 0
    status = 1
    products = ""
    giftby = " "
    giftmsg = " "
    for item in query_set:
        order_total = order_total + item.Product.price * item.product_quan + item.Product.bind_price
        total_products = total_products + 1
        giftby = item.gift_from 
        giftmsg = item.gift_message
        products = item.Product.title + ":" + \
            str(item.Product.price) +":"+str(item.Product.img) + ", " + products

    total_price = order_total + 10
    order_price = total_price

    print(order_price)
    # order_price.save()
    address = ""
    contact_no = ""
    contact_name = ""
    for address2 in address_set:
        address =  address2.line1 + ":" + address2.line2 + ":" + address2.line3+ ":" + address2.city + ":" + address2.addtype+ ":" +str(address2.addpincode)
        contact_no = address2.number
        contact_name = address2.name
    pay ="2"
    user_instance = Customer.objects.get(id=request.data['id'])
    order = EcomOrder(Order_placed_BY=user_instance,
                  total_products=total_products,
                  order_total =  order_price,
                  payment_mode= pay,
                  products=products,
                  address= address,
                  gift_message =giftmsg,
                  gift_from = giftby,
                  contact_name=contact_name,
                  contact_no=contact_no,
                  order_status=status)

    order.save()
    result.append({
        "order_id": order.id,
        "order_placed_by": order.Order_placed_BY.id,
        "total_products": order.total_products,
        "order_total": order.order_total,
        "date_of_ordering": order.date_of_ordering,
        "date_of_delivery": order.date_of_delivery,
        "address":order.address,
        "Contact_Name": order.contact_name,
        "Contact_Number": order.contact_no,
        "payment_mode":order.payment_mode,
        "products":order.products,
        "order_status":order.order_status,
        "order_completed": False
    })

    #query_set.delete()

    return JsonResponse(result, safe=False)


@api_view(['PUT'])
def complete_order(request):
    order_object = EcomOrder.objects.get(id=request.data['order_id'])
    query_set = CartProduct.objects.filter(user=request.data['id'])
    order_object.order_completed = True
    order_object.save()
    query_set.delete()
    return Response({"status": True, "message": "Order Dispatched"})


@api_view(['POST'])
def get_order_details(request):
    user_instance = Customer.objects.get(id=request.data['id'])
    order_object = EcomOrder.objects.filter(Order_placed_BY=user_instance)
    result = []

    for order in order_object:
        result.append({
            "order_id": str(order.id),
            "order_placed_by": order.Order_placed_BY.id,
            "ordered_products": order.products,
            "total_products": order.total_products,
            "order_price": order.order_total,
            "date_of_ordering": order.date_of_ordering,
            "date_of_delivery": order.date_of_delivery,
            "address":order.address,
            "Contact_Name": order.contact,
            "Contact_Number": order.contact_no,
            "order_completed": order.order_completed
        })

    return JsonResponse(result, safe=False)



@api_view(['GET'])
def get_order(request):
    order_object = EcomOrder.objects.filter(date_of_delivery = date.today()+timedelta(days = 1))
    result = []

    for order in order_object:
        result.append({
            "order_id": str(order.id),
            "order_placed_by": order.Order_placed_BY.id,
            "total_products": order.total_products,
            "order_price": order.order_total,
            "date_of_ordering": order.date_of_ordering,
            "date_of_delivery": order.date_of_delivery,
            "address":order.address,
            "Contact_Name": order.contact_name,
            "Contact_Number": order.contact_no,
            "order_status": order.order_status
        })

    return JsonResponse(result, safe=False)

@api_view(['GET'])
def get_pending_order(request):
    order_object = EcomOrder.objects.filter(date_of_delivery = date.today()+timedelta(days = 1)).exclude(a=True).filter(order_status=5)
    result = []

    for order in order_object:
        result.append({
            "order_id": str(order.id),
            "order_placed_by": order.Order_placed_BY.id,
            "total_products": order.total_products,
            "order_price": order.order_total,
            "date_of_ordering": order.date_of_ordering,
            "date_of_delivery": order.date_of_delivery,
            "address":order.address,
            "Contact_Name": order.contact_name,
            "Contact_Number": order.contact_no,
            "order_status": order.order_status
        })

    return JsonResponse(result, safe=False)

@api_view(['GET'])
def get_completed_order(request):
    order_object = EcomOrder.objects.filter(date_of_delivery = date.today()+timedelta(days = 1),order_status=5)
    result = []

    for order in order_object:
        result.append({
            "order_id": str(order.id),
            "order_placed_by": order.Order_placed_BY.id,
            "total_products": order.total_products,
            "order_price": order.order_total,
            "date_of_ordering": order.date_of_ordering,
            "date_of_delivery": order.date_of_delivery,
            "address":order.address,
            "Contact_Name": order.contact_name,
            "Contact_Number": order.contact_no,
            "order_status": order.order_status
        })

    return JsonResponse(result, safe=False)

@api_view(['PUT'])
def postponed_order(request):
    if 'order_id' in request.data:
        order_id = request.data['order_id']
    else:
        return Response({"Error": "Expected 'order_id' "})

    order_object = EcomOrder.objects.get(id=order_id)
    order_object.date_of_delivery = date.today() + timedelta(days=2)
    order_object.save()
    return Response({"checkStatus": True})

@api_view(['GET'])
def get_paymentstatus(request):
    orderid = request.GET.get('order_id')
    order_object = EcomOrder.objects.get(id=orderid)
    order_status = order_object.order_status
    if order_status == "4":
        payment_status = order_object.payment_mode
        if payment_status == "2":
            payment_status = "Cash On Delivery"
            payemnt_to_collect = order_object.order_total
            order_object.order_status = 5
            order_object.save()

        else:
            payment_status = "Online Payment"
            payemnt_to_collect = "0"
            order_object.order_status = 5
            order_object.save()

        return Response({"Payment Mode": payment_status,"Payment_to_collect":payemnt_to_collect})
    elif order_status == "1":
        return Response({"order_status": "PLEASE SCAN THE 1st qr Code"})
    elif order_status == "2":
        return Response({"order_status": "PLEASE SCAN THE 1st qr Code"})
    elif order_status == "3":
        return Response({"order_status": "PLEASE SCAN THE 2nd qr Code"})
    elif order_status == "5":
        return Response({"order_status": "PLEASE SCAN THE 4 th Code"})
    elif order_status == "6":
        return Response({"order_status": "Order has Been cancelled By the User"})
    else:
        return Response({"order_status": " Order Delivery Failed"})


@api_view(['GET'])
def order_dispatched(request):
    order_id = request.GET.get('order_id')
    order_object = EcomOrder.objects.get(id=order_id)
    order_status = order_object.order_status
    if order_status == "2":
        order_object.order_status = 3
        order_object.save()
        return Response({"order_status": "Order Dispatched Succesfully"})
    elif order_status == "1":
        return Response({"order_status": "Order Dispatched Already"})
    elif order_status == "3":
        return Response({"order_status": "Order Dispatched Already"})
    elif order_status == "4":
        return Response({"order_status": "Order Dispatched Already"})
    elif order_status == "3":
        return Response({"order_status": "Order Dispatched Already"})
    elif order_status == "6":
        return Response({"order_status": "Order has Been cancelled By the User"})
    else:
        return Response({"order_status": " Order Delivery Failed"})


@api_view(['GET'])
def order_outfor_Delivery(request):
    order_id = request.GET.get('order_id')
    order_object = EcomOrder.objects.get(id=order_id)
    order_status = order_object.order_status
    if order_status == "3":
        order_object.order_status = 4
        order_object.save()
        return Response({"order_status": "Order Out for Delivery"})
    elif order_status == "2":
        return Response({"order_status": "PLease Scan the 1 ST QR CODE First"})
    elif order_status == "1":
        return Response({"order_status": "PLease Scan the 1 ST QR CODE First"})
    elif order_status == "4":
        return Response({"order_status": "PLease Scan the NEXT QR CODE"})
    elif order_status == "5":
        return Response({"order_status": "PLease Scan the LAST QR CODE "})
    elif order_status == "6":
        return Response({"order_status": "Order has Been cancelled By the User"})
    else:
        return Response({"order_status": " Order Delivery Failed"})

@api_view(['GET'])
def order_Delivered(request):
    order_id = request.GET.get('order_id')
    order_object = EcomOrder.objects.get(id=order_id)
    order_status = order_object.order_status
    if order_status == "5":
        order_object.order_status = 7
        order_object.save()
        return Response({"order_status": "Order Delivered Successfully"})
    elif order_status == "2":
        return Response({"order_status": "PLease Scan the 1stQR CODE First"})
    elif order_status == "1":
        return Response({"order_status": "PLease Scan the 1st QR CODE First"})
    elif order_status == "3":
        return Response({"order_status": "PLease Scan the 2nd  QR CODE"})
    elif order_status == "4":
        return Response({"order_status": "PLease Scan the 3rd  QR CODE "})
    elif order_status == "6":
        return Response({"order_status": "Order has Been cancelled By the User"})
    else:
        return Response({"order_status": " Order Delivery Failed"})



















#attendance
@api_view(['POST'])
def mark_present(request):
    if 'emp_id' in request.data:
        emp_id = request.data['emp_id']
    else:
        return Response({"Error": "Expected 'emp_id' "})

    Status= "HD"
    emp_instance = Customer.objects.get(id=request.data['emp_id'])

    emp = Attendance(emp_id=emp_instance,status = Status,date = datetime.date.today() )
    try:
        emp.save()
        return Response({"Attendance Status": True,"Attendance marked":"Logged in  for  the Today"})
    except IntegrityError as e:
        return Response({"Attendance Status": False ,"Attendance marked":"Absent for  the Day"})

@api_view(['PUT'])
def signoff_for_the_day(request):
    if 'emp_id' in request.data:
        emp_id = request.data['emp_id']
    else:
        return Response({"Error": "Expected 'emp_id' "})

    Status= "P"
    emp = Attendance.objects.get(emp_id=request.data['emp_id'],date=datetime.date.today())
    emp.status= Status
    emp.exit_time = datetime.datetime.now()
    try:
        emp.save()
        return Response({"Attendance Status": True,"Attendance marked":"Present for  the Day"})
    except IntegrityError as e:
        return Response({"Attendance Status": True,"Attendance marked":"Absent for  the Day"})
