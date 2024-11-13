from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=1500)
    
    content = models.TextField()
    
    published_date = models.DateTimeField()
    
    featured_image = models.ImageField(upload_to="images/", default="images/default.jpg")