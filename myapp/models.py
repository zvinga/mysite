from django.db import models

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

    def __str__(self):
        return self.name
