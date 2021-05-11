from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.Index,name="index"),
    path("category1",views.Category1,name="Category1"),
    path("category2",views.Category2,name="Category2"),
    path("productdetails",views.Productdetails,name="Productdetails"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("policies",views.policies,name="policies"),
    path("cart",views.cart,name="cart"),
    path("wishlist",views.wishlist,name="wishlist"),
       
]
