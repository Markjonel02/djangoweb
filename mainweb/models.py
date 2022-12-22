#import the standard  django model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class CreateNewList(models.Model):
 #c auto_increment_id = models.AutoField(primary_key=True)
  name = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
  contact = models.IntegerField()
  email = models.EmailField()
  address = models.TextField(max_length=50)
  
  def __str__(self):
    return self.name
  
  