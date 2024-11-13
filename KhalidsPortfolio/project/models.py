from django.db import models

# Create your models here.

class Project(models.Model):
    
    title = models.CharField(max_length=1500)
    description = models.TextField() 
    
    statusChoices= models.TextChoices("status ", "Done inprogress notstarted fail")
    status   = models.CharField(max_length=100, choices=statusChoices.choices, default=statusChoices.Done)
    
    technology_use = models.CharField(max_length=1500)

    date_created = models.DateTimeField()

    image = models.ImageField(upload_to="images/" , default="images/default.jpg")