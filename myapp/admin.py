from django.contrib import admin
from myapp import models


# Register your models here.
admin.site.register(models.Email)
admin.site.register(models.Client)
admin.site.register(models.Food)
