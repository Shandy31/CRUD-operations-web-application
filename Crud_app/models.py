from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length= 256, default='NA')
    gender = models.CharField(max_length= 10, default='NA')
    age = models.IntegerField(default= 0,blank=True, null=True)
    phone_no = models.BigIntegerField(max_length=10,blank=True, null=True)
    DR_preferred = models.CharField(max_length= 256,default='NA')
    
