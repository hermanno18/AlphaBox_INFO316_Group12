from django.db import models
from .others_models import setting
class Utilisateur(models.Model):
	UserName=models.CharField(max_length=50,unique=True)
	Email   =models.EmailField(max_length=254)
	Password=models.CharField(max_length=50)
	

# Create your models here.
