from django.db import models

# Create your models here.
class Book(models.Model):
   title = models.CharField(max_length=150, unique=True)
   author = models.CharField(max_length=120)
   price = models.DecimalField(max_digits=10, decimal_places=2, default= 10.00)

   def __str__(self):
       return f"{self.title} by {self.author}"