from django.urls import path, include
from Accounts import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.registerPage,name="register"),
    path('Login',views.Login,name="Login"),
    path("logout/",views.logout_view, name="logout"),
]


