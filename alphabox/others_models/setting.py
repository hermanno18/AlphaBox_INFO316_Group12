from django.db import models

# Create your models here.

class Seting(models.Model):
    
    gameLang = models.CharField(max_length=15)
    gameTimer = models.CharField(max_length=100)
    gameOthersMembers =  models.CharField(max_length=100)