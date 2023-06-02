from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
ROLE_CHOICES=[
    ('cashier','Cashier'),
    ('admin','Admin')
]
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50,null=False,unique=True)
    first_name = models.CharField(max_length=50,null=False)
    last_name  = models.CharField(max_length=50,null=False)
    role = models.CharField(max_length=50,choices=ROLE_CHOICES,default='Cashier')
    email = models.EmailField(max_length=40)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','email',]
    
    def __str__(self):
        return self.username

    