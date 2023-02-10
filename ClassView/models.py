from django.db import models

# Create your models here.
class User1(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    email =models.EmailField(max_length=100)

    def __str__(self):
        return self.name