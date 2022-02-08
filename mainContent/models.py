from django.db import models

# Create your models here.

class poolDetails(models.Model):
    
    name = models.CharField(max_length=100)
    rollNo = models.CharField(max_length=100)
    stloc = models.CharField(max_length=100)
    dest = models.CharField(max_length=100)
    poolDate = models.DateField()
    poolTime = models.TimeField()
    mode = models.CharField(max_length=11)
    maxPPL = models.IntegerField()
    poolId = models.IntegerField()
    count = models.IntegerField()
 
class addMembers(models.Model):
    poolId = models.IntegerField()
    name = models.CharField(max_length=100)
    roll_no =  models.CharField(max_length=100)