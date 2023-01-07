#import the standard  django model
from django.db import models #add transaction to the model class 
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_delete #add these two used to give signal 
# Create your models here.

#---- CUSTOMERS PROFILE MODEL ----
class  Customers_crud(models.Model):
 #c auto_increment_id = models.AutoField(primary_key=True)
  CustomersName = models.CharField(max_length=20)
  ContactNumber = models.IntegerField()
  CustomersEmail = models.EmailField()
  CustomersAdd = models.CharField(max_length=50)
  
  def __str__(self):
    return self.CustomersName
  
#---- PRODUCT MANAGEMENT MODEL ----
class Product_crud(models.Model):
  ItemName = models.CharField(max_length=50)
  Size = models.CharField(max_length=50,null=True,blank=True)
  Category  = models.CharField(max_length=50)
  Price = models.DecimalField(max_digits=5,decimal_places=2)
  Stock = models.IntegerField(null=True,blank=True)
  
class product_archive(models.Model):
  ItemName = models.CharField(max_length=50)
  Size = models.CharField(max_length=50,null=True,blank=True)
  Category  = models.CharField(max_length=50)
  Price = models.DecimalField(max_digits=5,decimal_places=2)
  Stock = models.IntegerField(null=True,blank=True)
  Delete_at = models.DateTimeField(auto_now_add=True)
 
  def __str__(self):
    return self.ItemName


def to_archive(sender, instance, **kwargs):
  # this will copy the data from main model to archive model
  archive_record = product_archive(ItemName=instance.ItemName, Size=instance.Size, Category=instance.Category, Price=instance.Price, Stock=instance.Stock)
  archive_record.save()
  
pre_delete.connect(to_archive, sender=Product_crud)


def del_archive(sender,instance, **kwargs):
  # this permanently deleted from archive model this is "opdtional"
  product_archive.objects.filter(ItemName=instance.ItemName, Size=instance.Size, Category=instance.Category, Price=instance.Price, Stock=instance.Stock).delete()
  
post_delete.connect(del_archive, sender=product_archive)
