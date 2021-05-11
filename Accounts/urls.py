from django.urls import path, include
from Accounts import views


urlpatterns = [
    path('', views.registerPage,name="register"),
    path('Login',views.Login,name="Login"),

]
