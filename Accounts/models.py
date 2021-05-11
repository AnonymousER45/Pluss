from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

Address_type = (
    ('H', 'Home'),
    ('W', 'Office/Work'),
    ('O', 'Other')
)
# Custom User Which Can Login using Email address and password
class Customer(AbstractUser):
    phone_number = models.IntegerField(null=True, blank=True)
    Cust_Name = models.CharField(max_length=20)
    password = models.CharField(max_length=64)
    # email address is Unique for every user
    email = models.EmailField(_('email address'), unique=True)
    pincode = models.IntegerField(null=True,blank=True)
    
    USERNAME_FIELD = 'email'   # uses Email  field to Login
    REQUIRED_FIELDS = ['username']



# Address Model for storing multiple address of the user
class Address(models.Model):
    id = models.AutoField
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='Addresses')
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    line1 = models.CharField(max_length=30)
    line2 = models.CharField(max_length=25)
    line3 = models.CharField(max_length=25,blank=True,null=True)
    addtype = models.CharField(max_length=10,choices=Address_type,default='Home')
    addpincode = models.DecimalField(max_digits=6,decimal_places=0)


