from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator
from Accounts.models import Customer,Address
from Ecom.models import Product
from datetime import datetime

OrderStatus_CHOICE = (
    ("1" , "Order placed"),
    ("2" , "Order  Shipping"),
    ("3" , "Order Dispatched"),
    ("4" , "Order Out For Delivery"),
    ("5" , "Order Delivery"),
    ("6" , "Order Cancelled"),
)

OrderReturnExchnage_CHOICE  = (
    ("1" , "Return"),
    ("2" , "Exchange"),
)


Payment_CHOICE  = (
    ("1" , "COD"),
    ("2" , "Online Payment"),
)

# Create your models here.
class Order(models.Model):
    user_id  = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    #address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    Products = models.ManyToManyField(Product, through='OrderProduct')
    giftmessage =models.TextField(null=True,blank=True)
    giftmessage_from = models.CharField(max_length=254,null=True,blank=True)
    ordercreated_time = models.DateTimeField(auto_now=True)
    orderstatus = models.CharField(choices=OrderStatus_CHOICE,default="1",max_length=15)
    payment = models.CharField(choices=OrderStatus_CHOICE,default="1",max_length=15)
    order_mrp = models.IntegerField(null=True, blank=True)
    order_saving = models.IntegerField(null=True, blank=True)
    order_delivery = models.IntegerField(null=True, blank=True)
    no_of_product = models.IntegerField(null=True, blank=True)
    coupons_discount = models.IntegerField(null=True, blank=True)
    order_total_amount = models.IntegerField(null=True, blank=True)



class OrderProduct(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quan = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class orderReturn(models.Model):
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_return_status = models.CharField(choices=OrderReturnExchnage_CHOICE,default="1",max_length=15)
    orderstatus = models.CharField(choices=OrderStatus_CHOICE,default="1",max_length=15)
    returnReason = models.TextField(null=True,blank=True)
    orderReturn_time = models.DateTimeField(auto_now=True)
    return_prodimg = models.ImageField(upload_to="uploads/returnProducts/",blank=True,null=True)

    def __str__(self):
        return self.user.username + self.Product.title

class OrderTracker(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    orderstatus = models.CharField(choices=OrderReturnExchnage_CHOICE,default="1",max_length=15)
    orderReturn_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username + self.Product.title

