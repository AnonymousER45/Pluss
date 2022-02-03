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
from Ecom.models import Product ,Category,Cart,CartProduct,Wishlist,WishlistProduct,subCategory,Banner,ProductUnavailable,Requestbook,EcomOrder,Exchange_return,Refund_bankdetails,Refund_upidetails
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
from django.db.models import Q

import environ
from . import Checksum

env = environ.Env()
environ.Env.read_env()



def lookahead(iterable):
    """Pass through all values from the given iterable, augmented by the
    information if there are more values to come after the current one
    (True), or if it is the last value (False).
    """
    # Get an iterator and pull the first value.
    it = iter(iterable)
    last = next(it)
    # Run the iterator to exhaustion (starting from the second value).
    for val in it:
        # Report the *previous* value (more to come).
        yield last, True
        last = val
    # Report the last value.
    yield last, False


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
    customer.dob = "2021-05-10"
    customer.gender = "Other"
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


    if 'dob' in request.data:
        new_dob = request.data['dob']
    else:
        return Response({"Error": "Date of Birth Not Provided"})

    if 'gender' in request.data:
        new_gender = request.data['gender']
    else:
        return Response({"Error": "gender details Not Provided"})


    try:
        customer = Customer.objects.get(email=email)
        customer.username = new_user_name
        customer.phone_number = new_phone_number
        customer.first_name = new_fname
        customer.last_name = new_lname
        customer.dob = new_dob
        customer.gender = new_gender
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
        return Response({"status": True, "is_admin": False, "refresh": str(refresh), "access": str(refresh.access_token), "loggedIn": str(customer.username), "Firstname":str(customer.first_name), "id": customer.pk,"pincode":str(customer.pincode)})
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

    searchAdv(keyword);
    if query_set.exists():
            serializer_object = ProductSerializer(query_set, many=True)
    else :
        query_set = Product.objects.filter(Q(title__icontains=keyword) | Q(medium__icontains=keyword) | Q(slug__icontains=keyword) | Q(desp__icontains=keyword) )
        if query_set.exists():
            serializer_object = ProductSerializer(query_set, many=True)
        else :
            query_set = Product.objects.filter(Q(desp__icontains=keyword))
            serializer_object = ProductSerializer(query_set, many=True)
    return Response(serializer_object.data)


@api_view(['POST'])
@csrf_exempt
def search3(request):
    if 'keyword' in request.data:
        keyword = request.data['keyword']
    else:
        return Response({"Error":"Something went Wrong PLz TRy again"})

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
    if query_set.exists():
            serializer_object = ProductSerializer(query_set, many=True)
    else :
        query_set = Product.objects.filter(Q(title__icontains=keyword) | Q(medium__icontains=keyword) | Q(slug__icontains=keyword) | Q(desp__icontains=keyword) )
        if query_set.exists():
            serializer_object = ProductSerializer(query_set, many=True)
        else :
            query_set = Product.objects.filter(Q(desp__icontains=keyword))
            serializer_object = ProductSerializer(query_set, many=True)


    return Response(serializer_object.data)

# get search product
@api_view(['POST'])
@csrf_exempt
def search2(request):
        if 'keyword' in request.data:
            keyword = request.data['keyword']
        else:
            return Response({"Error": "Somethings went Wrong Plz Try again"})

        query_set = Product.objects.filter(Q(title__icontains=keyword) | Q(medium__icontains=keyword) | Q(slug__icontains=keyword) | Q(desp__icontains=keyword) )
        if query_set.exists():
            serializer_object = ProductSerializer(query_set, many=True)
        else :
            query_set = Product.objects.filter(Q(desp__icontains=keyword))
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
    delivery_charge=0
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

#add product to the cart
@api_view(['POST'])
def add_to_cart(request):
    try:
        cart_user = Cart.objects.get(user_id=request.data['id'])
        user_instance = Customer.objects.get(id=request.data['id'])
        product_instance = Product.objects.get(id=request.data['product_id'])
        #is_binding = request.data['is_binding']
        qs = CartProduct.objects.filter(user=user_instance, Product=product_instance)
        if qs.exists() :
            cartproduct = CartProduct.objects.get(user=user_instance, Product=product_instance,cart=cart_user)
            cartproduct.product_quan += 1
            #cartproduct.is_binding = is_binding
            cartproduct.save()
            return Response({"msg": "Quantity updated"})
        else:
            cart = CartProduct(user=user_instance,Product=product_instance, cart=cart_user)
            cart.save()
            return Response({"msg": "Item added to the Cart"})

    except Cart.DoesNotExist as e:
        user_instance = Customer.objects.get(id=request.data['id'])
        new_cart_user = Cart(user_id=user_instance)
        new_cart_user.save()
        user_instance = Customer.objects.get(id=request.data['id'])
        product_instance = Product.objects.get(id=request.data['product_id'])
        cart = CartProduct(user=user_instance,
                           Product=product_instance, cart=new_cart_user)
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
        wishlist = WishlistProduct(userx=user_instance,
        Product=product_instance, wishlist=wishlist_user)
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
        ,"Firstname":str(customer.first_name),"Lastname":str(customer.last_name),"Phone":str(customer.phone_number),"Email":str(customer.email),"dob":str(customer.dob),"gender":str(customer.gender)})
    else:
        return Response({"status": False})


@api_view(['POST'])
def user_details2(request):
    id = request.data["id"]
    customer = Customer.objects.get(id=id)
    return Response({"id": customer.pk ,"Firstname":str(customer.first_name),"Lastname":str(customer.last_name),"Phone":str(customer.phone_number),"Email":str(customer.email),"dob":str(customer.dob),"gender":str(customer.gender)})




@api_view(['POST'])
def search(request):
    keyword = request.data["keyword"]
    SearchAdv(keyword);
    if query_set == null:
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
    for item,hasmore in lookahead(query_set):
        # product = {'title':item.title}
        order_total = order_total + item.Product.price
        total_products = total_products + 1
        lastComma = ""
        if hasmore:
            lastComma = ","
        #products = item.Product.title + ":" + str(item.Product.price) +":"+str(item.Product.img) if products == "" else products + lastComma + item.Product.title + ":" + str(item.Product.price) +":"+str(item.Product.img)
        products += item.Product.title + ":" + str(item.Product.price) +":"+str(item.Product.img) + lastComma
    total_price = order_total
    order_price = total_price

    print(order_price)
    # order_price.save()
    address = " "
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
                  gift_message =gift_message,
                  gift_from = gift_from,
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

    query_set.delete()

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
            "Contact_Name": order.contact_name,
            "Contact_Number": order.contact_no,
            "order_status": order.order_status,
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

@api_view(['POST'])
def RETURNEXCHNAGE_order(request):
    order_id = EcomOrder.objects.get(id=request.data['order_id'])
    orderplacedby = Customer.objects.get(id=request.data['id'])
    option = request.data['option']
    reason = request.data['reason']
    if 'comment' in request.data:
        comment = request.data['comment']
    else:
        return Response({"Error": "Expected 'comment' "})

    retrunexchange = Exchange_return(order_id=order_id,orderplacedby=orderplacedby,option=option,reason=reason,comment=comment)
    retrunexchange.save()
    return Response({"msg": "Return and Exchange Query is raised Successfully"})


@api_view(['POST'])
def Refund_bankdetails(request):
    returnid=request.data['return_id']
    recipent_name=request.data['recipent_name']
    account_number=request.data['account_number']
    ifsc_code=request.data['ifsc_code']
    bankdetails = Refund_bankdetails(returnid=returnid,recipent_name=recipent_name,account_number=account_number,ifsc_code=ifsc_code)
    bankdetails.save()
    return Response({"msg": "Successfully updated the Details of Bank for the return "})

@api_view(['POST'])
def Refund_upidetails(request):
    if 'return_id' in request.data:
        return_id = request.data['return_id']
    else:
        return Response({"Error": "Expected 'orderreturn_id' "})

    upidetails = Refund_bankdetails(returnid=return_id,recipent_name=request.data['recipent_name'],upi_id=request.data['upi_id'])
    upidetails.save()
    return Response({"msg": "Successfully updated the Details of Bank for the return "})






# @api_view(['GET'])
def start_onlinepayment(request,order_id):
    # request.data is coming from frontend
    #order_object = EcomOrder.objects.get(id=request.data['order_id'])
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


@api_view(['POST'])
def handlepayment(request):
    checksum = ""
    # the request.POST is coming from paytm
    form = request.POST

    response_dict = {}
    order = None  # initialize the order varible with None

    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            # 'CHECKSUMHASH' is coming from paytm and we will assign it to checksum variable to verify our paymant
            checksum = form[i]

        if i == 'ORDERID':
            # we will get an order with id==ORDERID to turn isPaid=True when payment is successful
            order = EcomOrder.objects.get(id=form[i])

    # we will verify the payment using our merchant key and the checksum that we are getting from Paytm request.POST
    verify = Checksum.verify_checksum(response_dict, env('MERCHANTKEY'), checksum)

    if verify:

        if response_dict['RESPCODE'] == '01':
            # if the response code is 01 that means our transaction is successfull
            print('order successful')
            # after successfull payment we will make isPaid=True and will save the order
            # order.order_completed = True
            orderid = response_dict['ORDERID']
            order_object = EcomOrder.objects.get(id=orderid)
            order_object.order_completed = True
            order_object.save()
            # we will render a template to display the payment status
            return render(request, 'payments/paymentstatus.html', {'response': response_dict})
            #return Response({'Response': response_dict})
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
            orderid = response_dict['ORDERID']
            order_object = EcomOrder.objects.get(id=orderid)
            order_object.order_status = 5
            order_object.save()
            return render(request, 'payments/paymentstatus.html', {'response': response_dict})
            #return Response({'response': response_dict})



@api_view(['POST'])
def handlepayments(request):
    checksum = ""
    # the request.POST is coming from paytm
    form = request.POST

    response_dict = {}
    order = None  # initialize the order varible with None

    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            # 'CHECKSUMHASH' is coming from paytm and we will assign it to checksum variable to verify our paymant
            checksum = form[i]

        if i == 'ORDERID':
            # we will get an order with id==ORDERID to turn isPaid=True when payment is successful
            order = EcomOrder.objects.get(id=form[i])

    # we will verify the payment using our merchant key and the checksum that we are getting from Paytm request.POST
    verify = Checksum.verify_checksum(response_dict, env('MERCHANTKEY'), checksum)

    if verify:

        if response_dict['RESPCODE'] == '01':
            # if the response code is 01 that means our transaction is successfull
            print('order successful')
            # after successfull payment we will make isPaid=True and will save the order
            # order.order_completed = True
            orderid = response_dict['ORDERID']
            order_object = EcomOrder.objects.get(id=orderid)
            order_object.order_completed = True
            order_object.save()
            # we will render a template to display the payment status
            return render(request, 'ecom/orderplaced.html', {'response': response_dict})
            #return Response({'Response': response_dict})
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
            orderid = response_dict['ORDERID']
            order_object = EcomOrder.objects.get(id=orderid)
            order_object.order_status = 5
            order_object.save()
            return render(request, 'ecom/orderfailed.html', {'response': response_dict})
            #return Response({'response': response_dict})












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
