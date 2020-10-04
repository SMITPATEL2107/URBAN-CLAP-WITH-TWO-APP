from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique= True)
    password = models.CharField(max_length = 20)
    otp = models.IntegerField(default = 459)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)

class customer(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    fullname=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)

class Main(models.Model):
    address=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    phone=models.CharField(max_length=13)
    email=models.EmailField(max_length=50)