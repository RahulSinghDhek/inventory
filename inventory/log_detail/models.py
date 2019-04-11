from django.db import models

# Create your models here.

from django.db import models

# class Users(models.Model):
#     name = models.CharField(max_length=50)



class Item(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=20)
    product_code =  models.CharField(max_length=62)

class Varient(models.Model):
    name= models.CharField(max_length=10)
    selling_price = models.FloatField()
    cost_price= models.FloatField()
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, null=True, blank=True, on_delete=models.CASCADE, related_name='variant')

class Properties(models.Model):
    type = models.CharField(max_length=10)
    color = models.CharField(max_length=7)
    size = models.CharField(max_length=5)
    variant = models.OneToOneField(Varient,on_delete=models.CASCADE,related_name="properties")

# class LogData(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     item = models.ForeignKey(Item,null=True,blank=True,on_delete=models.CASCADE)
#     action = models.CharField(max_length=10)
#     #user = models.ForeignKey(Users,on_delete=models.CASCADE)
#     variant = models.ForeignKey(Varient,null=True,blank=True,on_delete=models.CASCADE)

class LogData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    item = models.CharField(max_length=50)
    action = models.CharField(max_length=10)
    user = models.CharField(max_length=50)
    variant = models.CharField(max_length=20)


