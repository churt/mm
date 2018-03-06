# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from client.models import BaseClient
from vehicle.models import Vehicle

class Driver(BaseClient):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    class Meta:
        app_label = 'driver'
