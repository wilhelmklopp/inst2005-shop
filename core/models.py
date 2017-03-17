from __future__ import unicode_literals

from django.db import models

# Create your models here.

# second hand clothes, so each item is unique


class Customer(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    email = models.EmailField()
    dob = models.DateField()


class Order(models.Model):
    buyer = models.ForeignKey(Customer)
    total = models.FloatField()
    date = models.DateField()


class Product(models.Model):
    garment = models.CharField(max_length=1000)
    colour = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    material = models.CharField(max_length=1000)
    gender = models.CharField(max_length=100, null=True)
    condition = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    price = models.FloatField()
    feedback = models.CharField(max_length=10000, null=True)
    order = models.ForeignKey(Order, null=True)
