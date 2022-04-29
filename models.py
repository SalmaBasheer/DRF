import email
from pickletools import UP_TO_NEWLINE

from django.db import models

# Create your models here.
class user(models.Model):
    userid=models.IntegerField(primary_key=True)
    username=models.TextField(default='')
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    
def __str__(self):
    return self.name






     
class Blogpost(models.Model):
    blogid=models.IntegerField(primary_key=True)
    Title=models.TextField(max_length=200)
    Body=models.TextField(max_length=200)
    createdAT=models.DateTimeField
    updtaedAT=models.DateTimeField
    user=models.ForeignKey(user,on_delete=models.CASCADE)

def __str__(self):
    return self.name 

class  Meta:
        ordering = ['created']
    

        
