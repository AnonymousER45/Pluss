from .models import Customer,Address
from Ecom.models import Wishlist,WishlistProduct
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .forms import  CustomerCreationForm


"""
 phone_number = models.IntegerField(null=True, blank=True)
    Cust_Name = models.CharField(max_length=20)
    # email address is Unique for every user
    email = models.EmailField(_('email address'), unique=True)
    pincode = models.IntegerField(null=True,blank=True)

"""

def registerPage(request):
    context = {}
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            phone_number = request.POST['phone']
            Password = request.POST['Password']
            Pincode = request.POST['pincode']
            cus = Customer(username=name,email=email,phone_number=phone_number,pincode=Pincode)
            cus.set_password(Password)
            cus.save()
            user=authenticate(username=email,password=Password)
            login(request,user)
            new_wishlist_user = Wishlist(user_id=user)
            new_wishlist_user.save()
            return redirect('Ecom:index')
        except:
            print("Enter all the required Fields")
            return render(request, 'accounts/register.html',context)


    return render(request, 'accounts/register.html',context)


# def registerPage(request):
#     context = {}
#     if request.method == 'POST':
#         form = CustomerCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email= form.cleaned_data['email']
#             raw_password = form.cleaned_data['password']
#             phone = form.cleaned_data['phone_number']
#             username = form.cleaned_data['username']
#             pincode = form.cleaned_data['pincode']
#             Customer.email = email
#             Customer.Cust_Name = username
#             Customer.phone_number = phone
#             Customer.pincode = pincode
#             Customer.set_password(raw_password)
#             Customer.save()
#             user=authenticate(username= username, password= raw_password)
#             login(request,user)
#             return redirect('Ecom:index')


#     else:
#         fm = CustomerCreationForm()
#         context={'form':fm}
#         return render(request,'accounts/signup.html',context)


#def Login(request):
   # return render(request,'account/login.html')


def Login(request):
    if request.method=="POST":
        # Get the post parameters
        try:
            username=request.POST['username']
            password=request.POST['password']
        # username = "ghodvinde03@gmail.com"
        # password = "Loveyou3000"
            user=authenticate(username= username, password= password)
            login(request,user)
            return redirect('Ecom:index')
        except:
            print("Enter all the required Fields")
            return render(request, 'accounts/login.html')

    return render(request,'accounts/login.html')
        #return redirect("index")
#     """if user is not None:
#             login(request, user)
#             messages.success(request, "Successfully Logged In")
#             return redirect("index")
#         else:
#             messages.error(request, "Invalid credentials! Please try again")
#             return render(request,'accounts/signup.html')

#       #return render(request,'accounts/login.html')
#     """

# """
# form = CreateUserForm()
# 		if request.method == 'POST':
# 			form = CreateUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('first_name')
# 				messages.success(request, 'Account was created for ' + user)

# 				return redirect('login')


# 		context = {'form':form}
# 		return render(request, 'accounts/signup.html', context)
# def register_customer(request):
#     if 'username' in request.data:
#         user_name = request.data['username']
#     else:
#         return Response({"Error": "Username Not Provided"})

#     if 'email' in request.data:
#         email = request.data['email']
#     else:
#         return Response({"Error": "Email Not Provided"})

#     if 'number' in request.data:
#         phone_number = request.data['number']
#     else:
#         return Response({"Error": "Contact Number Not Provided"})

#     if 'pincode' in request.data:
#         pincode = request.data['pincode']
#     else:
#         return Response({"Error": "Contact Number Not Provided"})

#     if 'password' in request.data:
#         password = request.data['password']
#     else:
#         return Response({"Error": "Password Not Provided"})

#     customer = Customer(email=email)
#     customer.username = user_name
#     customer.phone_number = phone_number
#     customer.pincode = pincode
#     customer.set_password(password)

#     try:
#         customer.save()
#         return Response({"registerStatus": True, "IntegrityError": False})
#     except IntegrityError as e:
#         return Response({"registerStatus": False, "IntegrityError": True})

# """



def logout_view(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect('Ecom:index')


