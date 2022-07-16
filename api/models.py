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
