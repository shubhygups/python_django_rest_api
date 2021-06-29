from django.db import models


# Create your models here.

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    top_speed = models.IntegerField()
    fuel_type = models.CharField(max_length=10)
    car_type = models.CharField(max_length=10)
    price = models.IntegerField()

    class Meta:
        unique_together = ('car_name', 'brand_name',)
