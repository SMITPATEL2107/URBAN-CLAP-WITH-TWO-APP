from django.db import models
from user.models import User
#from user.models import *

# Create your models here.


class technician(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    fullname=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)

class Emailconform(models.Model):
    email=models.EmailField(max_length=50)
    role=models.CharField(max_length=50,default="none")

class Emailnotconform(models.Model):
    noemail=models.EmailField(max_length=50)
    norole=models.CharField(max_length=50,default="none")
    
