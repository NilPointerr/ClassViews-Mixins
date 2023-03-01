from django.db import models
import uuid
# Create your models here.
class User1(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    email =models.EmailField(max_length=100)

    def __str__(self):
        return self.name
    
class Register(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    first_name = models.CharField(max_length=200,default='')
    last_name = models.CharField(max_length=200,default='')
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    re_password =models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
    