from django.db import models
import uuid
# Create your models here.

class Customers(models.Model):
    Customersname = models.CharField(max_length=20)
    Customersnumber  = models.IntegerField()
    Email = models.EmailField()
    Add = models.CharField(max_length=50)
#    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    #uuid for will generate a random uuid 
    
    def __str__(self):
        return self .Customersname #method just tells Django what to print when it needs to print out an instance
    
    