from django.db import models
from django.db.models.signals import pre_delete, post_delete #add these two used to give signal 
from django.utils import timezone
# Create your models here.

    #---- PRODUCT MANAGEMENT MODEL ----
class Product_crud(models.Model):

  sizes = (
    ('20 x 20','20 x 20'),
    ('20 x 60','20 x 60'),
    ('30 x 30','30 x 30'),
    ('30 x 60','30 x 60'),
    ('40 x 40','40 x 40'),    
    ('60 x 30','60 x 30'),
    ('n/a','N/A')
)
  categories = (
    ('adhesive','Adhesive'),
    ('porcelain','Porcelain'),
    ('ceramic','Ceramic'),
    ('skimcoat','Skimcoat'),
    ('sanitaryware ','Sanitary ware')
)
  status = (
    ('available','Available'),
    ('notavailable','Not Available'),
  )
  ItemName = models.CharField(max_length=50,null=False)
  Brand = models.CharField(max_length=50,null=False)
  Sizes = models.CharField(max_length=50,choices=sizes,null=True,default='12 x 30')
  Category  = models.CharField( max_length=50,choices=categories,default='Adhesive',null=False)
  Price = models.DecimalField(max_digits=5,decimal_places=2,null=False,)
  Current_Stock = models.IntegerField(null=False)
  Max_Stock = models.IntegerField(null=False)
  Status = models.CharField(max_length=50,null=False,choices=status)
  Image  = models.ImageField(upload_to='allimg',null=True,blank=True)
  Date_Added = models.DateTimeField(default=timezone.now) 
  
 
 # this Model used to copy all the records after deleting on database "In short Archive"  
class product_archive(models.Model):
  ItemName = models.CharField(max_length=50)
  Brand = models.CharField(max_length=50,null=False)
  Sizes = models.CharField(max_length=50,null=True,blank=True)
  Category  = models.CharField(max_length=50)
  Price = models.DecimalField(max_digits=5,decimal_places=2)
  Current_Stock = models.IntegerField(null=False)
  Max_Stock = models.IntegerField(null=False)
  Status = models.CharField(max_length=50,null=False)
  Delete_at = models.DateTimeField(default=timezone.now)
 
  def __str__(self):
    return self.ItemName


def to_archive(sender, instance, **kwargs):
  # this will copy the data from main model to archive model
  archive_record = product_archive(ItemName=instance.ItemName,Brand=instance.Brand ,
                                   Sizes=instance.Sizes, Category=instance.Category,
                                   Price=instance.Price, Current_Stock=instance.Current_Stock,
                                   Max_Stock=instance.Max_Stock, Status=instance.Status
                                   )
  archive_record.save()
  
pre_delete.connect(to_archive, sender=Product_crud)


def del_archive(sender,instance, **kwargs):
  # this permanently deleted from archive model this is "opdtional"
  product_archive.objects.filter(ItemName=instance.ItemName,Brand=instance.Brand ,
                                   Sizes=instance.Sizes, Category=instance.Category,
                                   Price=instance.Price, Current_Stock=instance.Current_Stock,
                                   Max_Stock=instance.Max_Stock, Status=instance.Status).delete(),
  
post_delete.connect(del_archive, sender=product_archive)
#  --- End of Product Management ---