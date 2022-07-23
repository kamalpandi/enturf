from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    mobileNumber = models.CharField(max_length=12)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=225)
    pincode = models.CharField(max_length=7)

    def __str__(self):
        return str(self.firstName)

class turfDetails(models.Model):
    admin = models.OneToOneField(Admin, on_delete=models.CASCADE)

    turfName = models.CharField(max_length=125)
    mobileNumber = models.CharField(max_length=12)
    openingTime = models.TimeField(auto_now=False, auto_now_add=False)
    cloasingTime = models.TimeField(auto_now=False, auto_now_add=False)
    addressOfTurf =  models.CharField(max_length=255)
    aminities = models.CharField(max_length=225)
    generalTurfImages =  models.ImageField(upload_to='images', blank=True,null = True)
    
    def __str__(self):
        return str(self.turfName)

