from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from hashids import Hashids
#import smtplib
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Accounts.models import Customer
#from . utils.otp_utils import generateOTP, generatingOTP
from django.conf import settings
from django.shortcuts import render
from django.db import IntegrityError


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
    else:
        return Response({"Error": "Last Name not Provided"})

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

    customer = Customer(email=email)
    customer.username = user_name
    customer.phone_number = phone_number
    customer.first_name = fname
    customer.last_name = lname
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
        return Response({"status": True, "is_admin": False, "refresh": str(refresh), "access": str(refresh.access_token), "loggedIn": str(customer.username), "id": customer.pk})
    else:
        return Response({"status": False})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
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





