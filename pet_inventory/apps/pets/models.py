from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    age = models.IntegerField()
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name