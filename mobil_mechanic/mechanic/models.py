# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from client.models import BaseClient

class Mechanic(BaseClient):

    rates = models.TextField()

    class Meta:

        app_label = 'mechanic'