from django.db import models
from Admin.models import*

# Create your models here.
class tbl_shop(models.Model):
    shop_name=models.CharField(max_length=30)
    shop_email=models.CharField(max_length=30)
    shop_contact=models.CharField(max_length=30)
    shop_address=models.CharField(max_length=30)
    shop_password=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    shop_photo=models.FileField(upload_to='Assets/File/user')
    shop_proof=models.FileField(upload_to='Assets/File/user')
    shop_status=models.IntegerField(default=0)

class tbl_pet(models.Model):
    pet_name=models.CharField(max_length=30)
    pet_photo=models.FileField(upload_to='Assets/File/user')
    pet_email=models.CharField(max_length=30)
    pet_password=models.CharField(max_length=30)
    pet_dob=models.DateField()
    pet_bio=models.CharField(max_length=30)
    breed=models.ForeignKey(tbl_breed,on_delete=models.CASCADE)