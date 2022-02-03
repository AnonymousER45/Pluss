from django.db import models
from rest_framework import serializers
from Ecom.models import Product , Category,subCategory,Banner,ProductUnavailable,Requestbook

from Accounts.models import Address,Pincode,Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["email"]




class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class subCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = subCategory
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class ProductUnavailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUnavailable
        fields = "__all__"


class RequestbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requestbook
        fields = "__all__"



class PincodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pincode
        fields = "__all__"
