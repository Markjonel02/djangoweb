from django.db import models
from ProductManagement.models import Product_crud
# Create your models here.
class CartQuantity(models.Model):
    product_id = models.IntegerField(null=False)
    name = models.CharField(max_length=50,null=False)
    size = models.CharField(max_length=15,null=False)
    quantity = models.IntegerField(null=False,)
    total_price = models.DecimalField(max_digits=12,decimal_places=2,null=True)