from django.db import models

# Create your models here.

class contact_tble(models.Model):
    boardId=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)
    # Emailaddress=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    # Message=models.CharField(max_length=50)



