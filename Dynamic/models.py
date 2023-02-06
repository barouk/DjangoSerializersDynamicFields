from django.db import models

# Create your models here.



class TestModel(models.Model):
    field1= models.CharField(max_length=20, null=True , blank=True)
    field2= models.CharField(max_length=20, null=True , blank=True)
    field3 = models.CharField(max_length=20, null=True, blank=True)