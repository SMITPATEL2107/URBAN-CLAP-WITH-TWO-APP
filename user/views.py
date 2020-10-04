from django.shortcuts import render
from .models import *
from random import randint
from user.utils import *

# Create your views here.

def HomePage(request):
    return render(request,("user/main.html"))

def RegisterPage(request):
    return render(request,("user/registeruser.html"))

def Login(request):
    return render(request,("user/loginuser.html"))

def About(request):
    return render(request,("user/about.html"))

def BookPage(request):
    return render(request,("user/booknow.html"))

def Blog(request):
    return render(request,("user/blog.html"))

def RegisterUser(request):
    try:
        print("--------------1---------------")
        fullname=request.POST['fname']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        reapeatpassword=request.POST['reapeatpassword']
        user = User.objects.filter(email=email)
        if user:
            print("--------------2---------------")
            message = 'This email already exists'
            return render(request,("user/registeruser.html"), {'message': message})
        else:
            if password == reapeatpassword:
                print("--------------3---------------")
                otp = randint(100000, 9999999)
                newuser = User.objects.create(
                    email=email, password=password,otp=otp)
                newtech = customer.objects.create(user_id=newuser, fullname=fullname,phone=phone)
                return render(request,("user/loginuser.html"))
            else:
                print("--------------4---------------")
                message = "Password and confirm password doesn't match"
                return render(request,("user/registeruser.html"),{'message': message})
    
    except Exception as e1:
        print("Registration print---->",e1)

def LoginUser(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    print(user)
    if user:
        print("---enter-----")
        if user[0].password == password:
            custo = customer.objects.filter(user_id=user[0])
            request.session['email']=user[0].email
            return render(request,("user/userpage.html"))
        else:

            message = "Your password is incorrect or user doesn't exist"
            return render(request, ("user/loginuser.html"), {'message': message})
    else:
        message = "user doesn't exist"
        return render(request, ("user/loginuser.html"), {'message': message})

def AddressInsert(request):
    try:
        print("-------1---------")
        address=request.POST['add']
        role=request.POST['role']
        phone=request.POST['phone']
        email=request.POST['email']
        newmain=Main.objects.create(address=address,phone=phone,email=email,role=role)
        user=Main.objects.get(email=email)
        if user:
            print("------2----------")
            email_subject="request has been send"
            sendmail(email_subject,"mail_template",email,{'email':email,'phone':phone})
            return render(request,("user/thanks.html"))
        else:
            return render(request,("user/sorry.html"))
    
    except Exception as e2:
        print("error is-----",e2)
    