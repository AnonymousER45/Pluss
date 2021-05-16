from .models import Customer,Address
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect
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
        form = CustomerCreationForm(request.POST)
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
            
            return redirect('Login')
        fm = CustomerCreationForm()
        context = {'form':fm}
        return render(request, 'accounts/signup.html',context)

    else:
        fm = CustomerCreationForm()
        context={'form':fm}
        return render(request,'accounts/signup.html',context)

def Login(request):
    return render(request,'account/login.html') 

"""
form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('first_name')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/signup.html', context)
def register_customer(request):
    if 'username' in request.data:
        user_name = request.data['username']
    else:
        return Response({"Error": "Username Not Provided"})

    if 'email' in request.data:
        email = request.data['email']
    else:
        return Response({"Error": "Email Not Provided"})

    if 'number' in request.data:
        phone_number = request.data['number']
    else:
        return Response({"Error": "Contact Number Not Provided"})
    
    if 'pincode' in request.data:
        pincode = request.data['pincode']
    else:
        return Response({"Error": "Contact Number Not Provided"})

    if 'password' in request.data:
        password = request.data['password']
    else:
        return Response({"Error": "Password Not Provided"})

    customer = Customer(email=email)
    customer.username = user_name
    customer.phone_number = phone_number
    customer.pincode = pincode
    customer.set_password(password)

    try:
        customer.save()
        return Response({"registerStatus": True, "IntegrityError": False})
    except IntegrityError as e:
        return Response({"registerStatus": False, "IntegrityError": True})

"""