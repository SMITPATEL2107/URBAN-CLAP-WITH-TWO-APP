from django.urls import path,include
from user import views

urlpatterns = [
    
    path("",views.HomePage,name="homepage"),
    path("registerpage/",views.RegisterPage,name="registerpage"),
    path("register/",views.RegisterUser,name="registeruser"),
    path("loginuser/",views.LoginUser,name="loginuser"),
    path("about/",views.About,name="about"),
    path("login/",views.Login,name="login"),
    path("booknow",views.BookPage,name="booknow"),
    path("insert/",views.AddressInsert,name="insert"),
    path("blog/",views.Blog,name="blog")   
]