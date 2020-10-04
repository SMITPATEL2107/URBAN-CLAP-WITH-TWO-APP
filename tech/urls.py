from django.urls import path,include
from tech import views

urlpatterns = [
    
    path("",views.Register,name="register"),
    path("registertech/",views.RegisterTech,name="registertech"),
    path("loginpage/",views.Loginpage,name="loginpage"),
    path("logintech/",views.LoginTech,name="logintech"),
    path("alldata/",views.AllData,name="alldata"),
    path("accept/<int:pk>",views.Accept,name="accept"),
    path("conform/<int:pk>",views.Conform,name="conform"),
    path("decline/<int:pk>",views.Decline,name="decline"),
    path("Notconform/<int:pk>",views.Notconform,name="notconform")
]