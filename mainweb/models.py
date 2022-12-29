#import the standard  django model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class  Customers_crud(models.Model):
 #c auto_increment_id = models.AutoField(primary_key=True)
  CustomersName = models.CharField(max_length=20)
  ContactNumber = models.IntegerField()
  CustomersEmail = models.EmailField()
  CustomersAdd = models.CharField(max_length=50)
  
  def __str__(self):
    return self.CustomersName
  
  