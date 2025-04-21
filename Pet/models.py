from django.db import models
from Pet.models import *
from Guest.models import *
# Create your models here.
class tbl_post(models.Model):
    post_photo=models.FileField(upload_to='Assets/File/user')
    post_description=models.CharField(max_length=30)
    pet=models.ForeignKey(tbl_pet,on_delete=models.CASCADE)

class tbl_comment(models.Model):
    post_comment=models.CharField(max_length=30)
    post=models.ForeignKey(tbl_post,on_delete=models.CASCADE)
    pet=models.ForeignKey(tbl_pet,on_delete=models.CASCADE,null=True)
    comment_date=models.DateTimeField()
class tbl_like(models.Model):
    post=models.ForeignKey(tbl_post,on_delete=models.CASCADE)
    pet=models.ForeignKey(tbl_pet,on_delete=models.CASCADE,null=True)

class tbl_grp(models.Model):
    group_name=models.CharField(max_length=30)
    group_description=models.CharField(max_length=30)
    group_photo=models.FileField(upload_to='Assets/File/user')
    group_date=models.DateField(auto_now_add=True)
    pet=models.ForeignKey(tbl_pet,on_delete=models.CASCADE,null=True)

class tbl_lostpet(models.Model):
    lostpet_name=models.CharField(max_length=30)
    lostpet_description=models.CharField(max_length=30)
    lostpet_photo=models.FileField(upload_to='Assets/File/user')
    lostpet_date=models.DateField(auto_now_add=True)
    lostpet_status=models.IntegerField(default=0)
    pet=models.ForeignKey(tbl_pet,on_delete=models.CASCADE,null=True)

class tbl_grpmembers(models.Model):
    grpmember_status=models.IntegerField(default=0)
    pet=models.ForeignKey(tbl_pet,on_delete=models.CASCADE)
    group=models.ForeignKey(tbl_grp,on_delete=models.CASCADE,null=True)
   
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=30)
    complaint_content=models.CharField(max_length=30)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_status=models.IntegerField(default=0)
    pet=models.ForeignKey(tbl_pet,on_delete=models.CASCADE)
    shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE,null=True)
    reply=models.CharField(max_length=30)
    complaint_status=models.IntegerField(default=0)
   
class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_pet,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_pet,on_delete=models.CASCADE,related_name="user_to",null=True)
    post = models.ForeignKey(tbl_post,on_delete=models.CASCADE,null=True)
    shop_from = models.ForeignKey(tbl_shop,on_delete=models.CASCADE,null=True,related_name="shop_from")
    shop_to = models.ForeignKey(tbl_shop,on_delete=models.CASCADE,null=True,related_name="shop_to")

class tbl_groupchat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_pet,on_delete=models.CASCADE)
    post = models.ForeignKey(tbl_post,on_delete=models.CASCADE,null=True)
    group = models.ForeignKey(tbl_grp,on_delete=models.CASCADE,null=True)

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=30)

class tbl_friends(models.Model):
    from_user = models.ForeignKey(tbl_pet, on_delete=models.CASCADE, related_name="from_user")
    to_user = models.ForeignKey(tbl_pet, on_delete=models.CASCADE, related_name="to_user")
    status = models.IntegerField(default=0)