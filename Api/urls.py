from django.urls import path, include
from Api import views

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #otp sms
    path('generate_otp/', views.generate_otp),  # Generates the OTP
    path('forgotpass_otp/', views.forgotpassotp),  # Generates the OTP
    path('check_otp/', views.check_otp),# Checks the OTP Generated OTP


    #otp mail
    path('generate_mailotp/', views.generate_mail_otp),  # Generates the OTP
    path('check_mail_otp/', views.check_mailotp),
    # Register Normal Customer
    path('register_customer/', views.register_customer),

    # Updates the registered customers
    path('update_customer/', views.update_customer),

    # Customer Login
    path('customer_login/', views.customer_login),
    path('user_details/', views.user_details),
    path('user_details2/', views.user_details2),

     # User change password
    path('change_password/', views.change_password),

    # Staff Login
    path('staff_login/', views.staff_login),

    # reset password through email
    path('password_reset/', views.password_reset),

    #get products
    path('get_products/',views.get_products),
    path('get_product_by_id/',views.get_product_by_id),
    path('get_products_by_category/',views.get_Products_by_Category),
    path('get_product_by_subcat/',views.get_Products_by_SubCategory),
    path('get_product_by_medium/',views.get_Products_by_medium),
    path('get_product_by_filter/',views.get_Products_by_filter),
    path('get_new_arrivals/',views.get_new_arrivals),
    path('get_bestseller/',views.get_new_bestseller),
    path('search/', views.search),
    path('add_ProductUnavailable',views.add_ProductUnavailable),

    #get banner dynamically
    path('get_home_banners/',views.get_home_banners),

    path('search/',views.search),
    path('search2/',views.search2),
    path('search3/',views.search3),


    #get categories
    path('get_category/',views.get_Category),
    #get categories
    path('get_subcategory/',views.get_SubCategory),

    #add to cart
    path('add_to_cart/',views.add_to_cart),

    #remove to cart
    path('remove_from_cart/',views.remove_from_cart),
    path('empty_cart/',views.empty_cart),

    #get_cart_details
    path('get_cart_details/',views.get_cart_details),

    #add address
    path('add_address/',views.add_address),
    #remove address
    path('remove_address/',views.remove_address),
    #remove all address
    path('remove_all_address/',views.remove_all_address),

    #update address
    path('update_address/',views.update_address),

    #get_address
    path('get_address/<int:id>',views.get_address),

    #add to wishlist
    path('add_to_wishlist/',views.add_to_wishlist),
    #remove produt from wislist
    path('remove_from_wishlist/',views.remove_from_wishlist),
    #remove all product from wishlist
    path('empty_wishlist/',views.empty_wishlist),
    #get wishlist
    path('get_wishlist/',views.get_wishlist),


    path('token/', TokenObtainPairView.as_view(), name= 'token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    #Request book
    path('request_book/',views.Requestbook),

    #order
    path('place_order/',views.place_order),
    path('complete_order/',views.complete_order),
    path('get_order_details/',views.get_order_details),

    path('returnexchangeorder/',views.RETURNEXCHNAGE_order),
    path('refund_bankdetails/',views.Refund_bankdetails),
    path('refund_upidetails/',views.Refund_upidetails),



    path('get_todays_order/',views.get_order),
    path('get_pending_order/',views.get_pending_order),
    path('get_completed_order/',views.get_completed_order),
    path('postponed_order/',views.postponed_order),
    path('get_paymentstatus/',views.get_paymentstatus),
    path('order_dispatched/',views.order_dispatched),

    path('order_delivering/',views.order_Delivered),
    path('order_outfor_Delivery',views.order_outfor_Delivery),
    #get products
    path('get_pincode/',views.get_pincode),

    #attendance
    path('mark_present/',views.mark_present),
    path('signoff/',views.signoff_for_the_day),


    path('online_pay/',views.start_onlinepayment, name="start_onlinepayment"),
    path('handlepayment/',views.handlepayment, name="handlepayment"),
    path('handlepayments/',views.handlepayments, name="handlepayments"),

]
