from django.db import models

# Create your models here.
class Project(models.Model):
	link = models.CharField(max_length=40)
	rasim = models.ImageField(upload_to='media')
	nomi = models.CharField(max_length=20)
	tafsiya = models.CharField(max_length=200)
	

class Banner(models.Model):
	rasim = models.ImageField(upload_to='media')
	