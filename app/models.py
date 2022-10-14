from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class vehicle_registration(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    vehiclenumber = models.CharField(max_length=240, null=True)
    vehicletype = models.CharField(max_length=240, null=True)
    vehiclemodal = models.CharField(max_length=240, null=True)
    vehicledescription = models.EmailField(max_length=240, null=True)
    def __str__(self):
        return self.vehiclenumber



class designation(models.Model):
    designation = models.CharField(max_length=100)
    def __str__(self):
        return self.designation


class useroradminregistration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,null=True, blank=True)
    firstname = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    def __str__(self):
        return self.firstname


