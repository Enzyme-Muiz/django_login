from django.db import models
from multiselectfield import MultiSelectField




# Create your models here.
class Tutorial(models.Model):
	tutorial_title= models.CharField(max_length=200)
	tutorial_content= models.TextField()
	tutorial_published= models.DateTimeField("date published")

	def __str__(self):
		return self.tutorial_title



class miRNA(models.Model):
	name= models.CharField(max_length=100)
	location= models.TextField(max_length=20)

class image_upload(models.Model): 
	COUNTRY_CHOICES = (
    ('Mubaarak','Mubaarak'),
    ('Nabeel','Nabeel'),
    ('Abdul-Mujeeb','Abdul-Mujeeb'),
   
    )
	
	name = models.CharField(max_length=50, choices= COUNTRY_CHOICES, blank=True) 
	Img = models.ImageField(upload_to='images/') 
	
	def __str__(self): 
		return self.name
	

