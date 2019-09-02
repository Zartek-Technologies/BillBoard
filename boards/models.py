from django.db import models
from django.urls import reverse
from boards.choices import *

# Create your models here.
class BillBoard(models.Model):    
    boardId = models.CharField(max_length=20, unique=True)
    imglink = models.ImageField(upload_to='board_pics', null=False)
    facingDirection = models.CharField(choices=DIRECTION_CHOICES, default="North", max_length=50)    
    height = models.IntegerField()
    width = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.CharField(max_length=100)
    sqfeetSize = models.IntegerField()
    backLight = models.BooleanField()
    available = models.BooleanField()

    def __str__(self):
        return self.boardId

# class contact(models.Model):
#     BillBoardId=models.CharField(max_length=50)
#     Name=models.CharField(max_length=50)
#     City=models.CharField(max_length=50)