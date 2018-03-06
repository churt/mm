# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Location(models.Model):
    """
    Location of a Mechanic or Driver
    """
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    code = models.CharField(max_length=15)

    class Meta:

        app_label = 'location'