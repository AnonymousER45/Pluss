from django.urls import path, include
from Accounts import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # path('signup', views.SignupPage,name="signup"),
    path('Register', views.registerPage,name="register"),
    path('Login',views.Login,name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
