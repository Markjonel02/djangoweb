#import the standard  django model
from django.db import models #add transaction to the model class 
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_delete #add these two used to give signal 
from django.db.models import Q # use to search name , object contains a ltter you want to search

# Create your models here.
  #---- CUSTOMERS PROFILE MODEL ----
class  Customers_crud(models.Model):
 # auto_increment_id = models.AutoField(primary_key=True)
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
  
 
 # this Model used to copy all the records after deleting on database "In short Archive"  
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


# searching for itemes on table uisng "__iexact" this is used for search an exact name 
# you can also use "__icontains" this is use for searching a letter within a table
# you can also use "__istartwith" this will search a first letter of an item in the table


#  --- End of Product Management ---



# --- usermanagement start --- 
class UserAdmin(models.Model):
  Name = models.CharField(max_length=50)
  Username = models.OneToOneField(User, on_delete=models.CASCADE)
  Password = models.CharField(max_length=50)
  UserType = models.CharField(max_length=50)
  is_active = models.BooleanField(default=True)
  
# --- usermanagement end --- 



# ====== adhesive Uploading Model ========

class PhotoUP(models.Model):
  sizes = (
    ('12 x 30','12 x 30'),
    ('247 x 97','247 x 97'),
    ('20 x 30','20 x 30')
)
  categories = (
    ('adhesive','Adhesive'),
    ('porcelain','Porcelain'),
    ('ceramic','Ceramic'),
    ('skimcoat','Skimcoat'),
    ('sanitaryware ','Sanitary ware')
)
  
  Itemname = models.CharField(max_length=50)
  Size     = models.CharField(max_length=50,choices=sizes,blank=True,null=True)
  #Description = models.TextField(max_length=100,blank=True, null=True)
  Category = models.CharField(max_length=50,choices=categories,)
  Image    = models.ImageField(upload_to='uploadedimg',null=True, blank=True)
  Updload_at = models.DateTimeField(auto_now_add=True)
  #Updated_at = models.DateTimeField(auto_now_add=True ,default=timezone.now)
  
  def __str__(self):
    return self.Itemname
  

  # ======= model for porcelain =========
class PhotoUPporcelain(models.Model):
  P_sizes = (
    ('12 x 30','12 x 30'),
    ('247 x 97','247 x 97'),
    ('20 x 30','20 x 30')
)
  P_categories = (
    ('adhesive','Adhesive'),
    ('porcelain','Porcelain'),
    ('ceramic','Ceramic'),
    ('skimcoat','Skimcoat'),
    ('sanitaryware ','Sanitary ware')
)
  
  Itemname_p = models.CharField(max_length=50)
  Size_p     = models.CharField(max_length=50,choices=P_sizes,blank=True,null=True)
  #Description = models.TextField(max_length=100,blank=True, null=True)
  Category_p = models.CharField(max_length=50,choices=P_categories,)
  Image_p    = models.ImageField(upload_to='porcelain_img',null=True, blank=True)
  Updload_at = models.DateTimeField(auto_now_add=True)
  #Updated_at = models.DateTimeField(auto_now_add=True ,default=timezone.now)
  
  def __str__(self):
    return self.Itemname_p
  
#  ====   Ceramic photouploading Model ======
  
class PhotoUPCeramic(models.Model):
  C_sizes = (
    ('12 x 30','12 x 30'),
    ('247 x 97','247 x 97'),
    ('20 x 30','20 x 30')
)
  C_categories = (
    ('adhesive','Adhesive'),
    ('porcelain','Porcelain'),
    ('ceramic','Ceramic'),
    ('skimcoat','Skimcoat'),
    ('sanitaryware ','Sanitary ware')
)
  
  Itemname_c = models.CharField(max_length=50)
  Size_c     = models.CharField(max_length=50,choices=C_sizes,blank=True,null=True)
  #Description = models.TextField(max_length=100,blank=True, null=True)
  Category_c = models.CharField(max_length=50,choices=C_categories,)
  Image_c    = models.ImageField(upload_to='ceramic_img',null=True, blank=True)
  Updload_at = models.DateTimeField(auto_now_add=True)
  #Updated_at = models.DateTimeField(auto_now_add=True ,default=timezone.now)
  
  def __str__(self):
    return self.Itemname_c
  
  
  # ===== End of ceramic model =====
  
  
  
  
  
  
  
  
# --- End of Photo Uploading Model ---