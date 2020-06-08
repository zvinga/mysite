from django.db import models
from datetime import datetime

# Create your models here.

class Student(models.Model):

    chosse=[
            ('male','male'),
            ('female','female'),
            ('other','other')
    ]
    name = models.CharField(max_length=40, null=True, blank=True, unique=True, help_text='name please')
    age = models.IntegerField(null=True, default='18')
    gendre = models.CharField(null=True, max_length=10, choices=chosse)
    ''' #x1 = models.BigIntegerField()
    #x2 = models.AutoField()
    #x3=  models.BigAutoField() 
    x4 = models.BooleanField(name="check",null=True)
    x41 = models.BooleanField()
    x5 = models.DateField()   #timeField /datetimeField(deufault=datetime.now) '''
    x1 = models.EmailField(name="Emaile", max_length=254, null=True)
    x2 = models.FileField(upload_to="myapp/upload", max_length=100, null=True)
    x3 = models.ImageField(upload_to="myapp/upload", null=True)
    x4 = models.TextField(null=True)
    

    

    
    


    def __str__(self):
        return self.name
