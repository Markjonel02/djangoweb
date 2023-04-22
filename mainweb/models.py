#import the standard  django model
from django.db import models #add transaction to the model class 
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_delete #add these two used to give signal 
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin ,BaseUserManager #se
from django.utils.translation import gettext_lazy as _
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
  Product_category  =( 
                      ('adhesive', 'Adhesive'),
                      ('porcelain', 'Porcelain'),
                       ('ceramic', 'Ceramic'),
                      ('skimcoat', 'Skimcoat'),
                      ('sanitaryware', 'sanitaryware'),
                      )
  
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
#  --- End of Product Management ---

# --- usermanagement start --- 

class CustomUserManagement(BaseUserManager):
  def create_superuser(self, email, user_name, first_name, password, **other_fields ):
    other_fields.setdefault('is_staff', True)
    other_fields.setdefault('is_superuser', True)
    other_fields.setdefault('is_active', True)
    #validation of staff and superuser
    if other_fields.get('is_staff')is not True:
      raise ValueError('superuser must be assign to is_staff=True')
    if other_fields.get('is_superuser')is not True:
      raise ValueError('must be assign to is_superuser=True')
    
    return self.create_user(email, user_name, first_name, password, **other_fields)
 
  def create_user(self, email, user_name, first_name, password, **other_fields):
    
    if not email:
      raise ValueError(_('you must provide email address!'))
    email = self.normalize_email(email)
    user  = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
    user.set_password(password)
    user.save()
    return user
  
class UserManagement(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, unique=True)
    is_staff = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=False)
    
    objects = CustomUserManagement()
  
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['first_name','email']
    
    def __str__(self):
      return self.user_name
    
    
    

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
  Image    = models.ImageField(upload_to='allimg',null=True, blank=True)
  Updload_at = models.DateTimeField(auto_now_add=True)
  #Updated_at = models.DateTimeField(auto_now_add=True ,default=timezone.now)
  
  def __str__(self):
    return self.Itemname  
# --- End of Photo Uploading Model ---


