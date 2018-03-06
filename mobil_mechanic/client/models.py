# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from location.models import Location
from rating.models import Rating


class BaseClient(models.Model):
    """
    Base model for a Mechanic and Driver
    """
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'client'