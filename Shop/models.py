from django.db import models
from Shop.models import *
from Guest.models import *
from datetime import datetime
# Create your models here.
class tbl_product(models.Model):
    product_name=models.CharField(max_length=30)
    product_description=models.CharField(max_length=30)
    product_photo=models.FileField(upload_to='Assets/File/user')
    product_price=models.CharField(max_length=30)
    product_postdate=models.DateTimeField(auto_now_add=True)
    shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE)
    