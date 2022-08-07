from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Admin(models.Model):
        # REQUIRED_FIELDS = ('user',)
        # USERNAME_FIELD = 'email'
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin')

    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    mobileNumber = models.CharField(max_length=12)
    email = models.EmailField(max_length = 254,unique=True)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=225)
    pincode = models.CharField(max_length=7)

    start_date = models.DateTimeField(default=timezone.now)

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
    
    def __str__(self):
        return str(self.turfName)

class turfImages(models.Model):
    turfDetails = models.ForeignKey(turfDetails,on_delete=models.CASCADE)
    generalTurfImages =  models.ImageField(upload_to="images", blank=True,null = True)

    def __str__(self):
        return self.turfDetails.turfName

class GroundDetails(models.Model):
    turfId = models.ForeignKey(turfDetails,on_delete=models.CASCADE)
    groundName = models.CharField(max_length=225)
    openingTime = models.TimeField(blank=False,auto_now=False, auto_now_add=False)
    closingTime = models.TimeField(blank=False,auto_now=False, auto_now_add=False)
    
