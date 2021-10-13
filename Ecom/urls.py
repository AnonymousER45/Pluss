from django.urls import path, include
from . import views

app_name = "Ecom"

urlpatterns = [
    path("",views.Index,name="index"),
    path("category1/<int:myid>",views.Category1,name="Category1"),
    path("category2/<int:myid>",views.Category2,name="Category2"),
    path("category3/<int:myid>",views.Category3,name="Category3"),
    path("category4/<int:myid>",views.Category4,name="Category4"),
    path("category5/<int:myid>",views.Category5,name="Category5"),
    path("category6/<int:myid>",views.Category6,name="Category6"),
    path("category7/<int:myid>",views.Category7,name="Category7"),
    path("category8/<int:myid>",views.Category8,name="Category8"),
    path("category9/<int:myid>",views.Category9,name="Category9"),
    path("productdetails/<int:id>",views.Productdetails,name="Productdetails"),
    path("showall",views.showall,name="showall"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("policies",views.policies,name="policies"),
    path("cart",views.cart,name="cart"),
    path("wishlist",views.wishlist,name="wishlist"),
    path("requestbook",views.requestbook,name="requestbook"),
    path("myorders",views.myorders,name="myorders"),
    path("orders_details/<int:order_id>",views.orders_details,name="orders_details"),
    path("myaccount",views.myaccount,name="myaccount"),
    path("mycart",views.mycart,name="mycart"),
    path("myaddressbook",views.myaddressbook,name="myaddressbook"),
    # path("myaddressbook2",views.myaddressbook2,name="myaddressbook2"),
    path("payment/<int:order_id>",views.payment,name="payment"),
    path("orderplaced/<int:order_id>",views.orderplaced,name="orderplaced"),
    path("ordercancelation",views.ordercancelation,name="ordercancelation"),
    path("returnandexchange",views.returnandexchange,name="returnandexchange"),
    path("faq",views.faq,name="faq"),
    path("contactus",views.contactus,name="contactus"),
    path("privacy",views.privacy,name="privacy"),
    path("termsandcondition",views.termsandcondition,name="termsandcondition"),
    path("showalldemo",views.showalldemo,name="showalldemo"),
    path("edit_address",views.edit_address,name="edit_address"),
    path("add_address",views.add_address,name="add_address"),
    path("addressbook",views.addressbook,name="addressbook"),
    path("personal_info",views.personal_info,name="personal_info"),


]
