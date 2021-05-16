from django.urls import path, include
from Api import views

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    # Register Normal Customer
    path('register_customer/', views.register_customer),

    # Updates the registered customers
    path('update_customer/', views.update_customer),


    # Customer Login
    path('customer_login/', views.customer_login),

     # User change password 
    path('change_password/', views.change_password),

    
    # reset password through email
    path('password_reset/', views.password_reset),
    

    path('token/', TokenObtainPairView.as_view(), name= 'token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   
]
