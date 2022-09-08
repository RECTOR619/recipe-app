from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField(max_length = 150)
    price = models.DecimalField(decimal_places= 2, max_digits=100)
    image = models.ImageField(upload_to = "recipe/recipes/")
    date_created = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) :
        return self.name

