from django.db import models
from django.contrib import admin

class Car(models.Model):
    Name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
class CarAdmin(admin.ModelAdmin):
    list_display = ('Name', 'model', 'year', 'price')