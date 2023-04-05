from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6, decimal_places=2
    )  # for monatary used decimalField instead of float due to rounding issue
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)  # updates the date


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField(null=True)
