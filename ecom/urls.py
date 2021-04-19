from django.urls import path
from . import views




urlpatterns = [
    path("home", views.index, name="index"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("Login",views.login,name="login"),
]
