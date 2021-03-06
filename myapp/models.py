from django.db import models
from datetime import datetime

# Create your models here.

class Email(models.Model):
        user_email = models.EmailField(null=True)
        def __str__(self):
                return self.user_email


class Food(models.Model):
    food_name = models.CharField(blank=True, max_length=100, null=True)

    def __str__(self):
        return self.food_name

class Client(models.Model):
        name = models.CharField(max_length=20, null=True)
        email = models.OneToOneField(Email, on_delete=models.CASCADE)
        food = models.ForeignKey(Food, on_delete=models.CASCADE)
        

        def __str__(self):
            return self.name




    
    
    
