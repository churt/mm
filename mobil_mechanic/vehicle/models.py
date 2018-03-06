# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from driver.models import Driver

class Vehicle(models.Model):

    VEHICLE_TYPE_CHOICES = (
        ('COUPE', 'Coupe'),
        ('SEDAN', 'Sedan'),
        ('SUV','SUV'),
        ('V_SERIES', 'V Series'),
        ('HYBRID', 'Hybrid'),
    )

    type = models.CharField(max_length=15, choices=VEHICLE_TYPE_CHOICES)
    year = models.IntegerField()
    make = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    # owner = models.ForeignKey(Driver, on_delete=models.CASCADE)

    class Meta:

        app_label = 'vehicle'