from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
numeric = RegexValidator(r'^\d{1,11}$')
GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
class Customerprofile(models.Model):
   
    
    customer_Fname = models.CharField(max_length=50,null=False)
    customer_Middlename = models.CharField(max_length=50,null=True)
    customer_Lname = models.CharField(max_length=50,null=False)
    sex = models.CharField(max_length=50,choices=GENDER_CHOICES,null=False)
    email = models.EmailField(max_length=50,null=False,unique=True)
    address = models.CharField(max_length=100,null=False)
    contactnumber = models.CharField(max_length=11,validators=[numeric],null=False)
    
    def __str__(self):
        return self.email
    
    