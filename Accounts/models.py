from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


#from django.utils.translation import ugettext_lazy as _

Address_type = (
    ('H', 'Home'),
    ('W', 'Office/Work'),
    ('O', 'Other')
)
# Custom User Which Can Login using Email address and password
class Customer(AbstractUser):
    phone_number = models.IntegerField(null=True, blank=True)
    pincode = models.IntegerField(blank=False,null=False,default=421501)
    # email address is Unique for every user
    email = models.CharField(max_length=50,blank=False,null=False,unique=True)

    USERNAME_FIELD = 'email'   # uses Email  field to Login
    REQUIRED_FIELDS = ['username']


class Attendance(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    status = models.CharField(max_length=2,choices=(('P','Present'),('A','Absent'),('HD','Half Day')),default='A')
    entry_time = models.DateTimeField(default = datetime.now)
    exit_time = models.DateTimeField(blank=True,default = datetime.now)
    emp_id  = models.ForeignKey(Customer,limit_choices_to={'is_staff': True}, on_delete=models.DO_NOTHING, default=1)
    def __str__(self):
        return "{0} {1} {2} {3} {4} ".format(self.emp_id.id,self.emp_id.username,self.date,self.status,self.entry_time)



# Address Model for storing multiple address of the user
class Address(models.Model):
    id = models.AutoField
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='Addresses')
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    line1 = models.CharField(max_length=30)
    line2 = models.CharField(max_length=25)
    line3 = models.CharField(max_length=25,blank=True,null=True)
    addtype = models.CharField(max_length=10,choices=Address_type,default='Home')
    addpincode = models.DecimalField(max_digits=6,decimal_places=0)
    isdeafault = models.BooleanField(default=False)
    number = models.IntegerField(default=7756078806)

    def __str__(self):
        return self.name



class OTP(models.Model):
    phone_number = models.IntegerField()
    otp = models.CharField(max_length=4)
    is_verfied = models.BooleanField(default=False)

class OTPmail(models.Model):
    mailid = models.EmailField(max_length=254)
    otp = models.CharField(max_length=4)
    is_verfied = models.BooleanField(default=False)



# Discount Coupon for user

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.FloatField(max_length=15)
    valid_from = models.DateTimeField(default=datetime.now)
    valid_to = models.DateTimeField(blank=False,null=False,default=None)

    def __str__(self):
        return self.code


class Pincode(models.Model):
    pincode = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.pincode

