from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import *
from random import randint
from user.models import Main
from tech.utils import *

# Create your views here.

def Register(request):
    return render(request,("tech/register.html"))

def Loginpage(request):
    return render(request,("tech/login.html"))

def RegisterTech(request):
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
            return render(request,("tech/register.html"), {'message': message})
        else:
            if password == reapeatpassword:
                print("--------------3---------------")
                otp = randint(100000, 9999999)
                newuser = User.objects.create(
                    email=email, password=password, otp=otp)
                newtech = technician.objects.create(user_id=newuser, fullname=fullname,phone=phone)
                return render(request,("tech/login.html"))
            else:
                message = "Password and confirm password doesn't match"
                return render(request, ("tech/register.html"), {'message': message})

    except Exception as e1:
        print("Registration print---->",e1)

def LoginTech(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    print(user)
    if user:
        if user[0].password == password:
            custo = technician.objects.filter(user_id=user[0])
            request.session['email']=user[0].email
            #return render(request, 'techdata.html')
            return redirect('alldata')
        else:
            message = "Your password is incorrect or user doesn't exist"
            return render(request, ("tech/login.html"), {'message': message})
    else:
        message = "user doesn't exist"
        return render(request, ("tech/login.html"), {'message': message})

def AllData(request):
    alldata = Main.objects.all()
    cont={'alldata':alldata}
    return render(request,("tech/techdata.html"),cont)

def Accept(request,pk):
    #address=request.POST['address']
    getdata =Main.objects.get(pk=pk)
    return render(request,"tech/emailconform.html",{'key2':getdata})

def Conform(request,pk):
    email=request.POST['email']
    role=request.POST['role']
    
    new=Emailconform.objects.create(email=email,role=role)
    user=Emailconform.objects.filter(email=email)
    if user:
        email_subject="Request Conformed"
        sendmail1(email_subject,"mail_template1",email,{'email':email})
        ddata=Main.objects.get(pk=pk)
        ddata.delete()
        #data=Main.objects.get()
        #HttpResponseRedirect(reverse('alldata'))
        return redirect('alldata')
    else:
        return render(request,("tech/sorry.html")) 

def Decline(request,pk):
    #address=request.POST['address']
    getdata =Main.objects.get(pk=pk)
    return render(request,("tech/notconform.html"),{'key3':getdata})

def Notconform(request,pk):
    noemail=request.POST['email']
    norole=request.POST['role']
    
    notcon=Emailnotconform.objects.create(noemail=noemail,norole=norole)
    user=Emailnotconform.objects.filter(noemail=noemail)
    if user:
        email_subject="Request Conformed"
        sendmail2(email_subject,"mail_template1",noemail,{'email':noemail})
        ddata=Main.objects.get(pk=pk)
        ddata.delete()
        #data=Main.objects.get()
        #HttpResponseRedirect(reverse('alldata'))
        return redirect('alldata')
    else:
        return render(request,("tech/sorry.html")) 
