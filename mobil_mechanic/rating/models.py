# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Rating(models.Model):
    RATING_CHOICES = (
        (
            1, 'Poor'
        ),
        (
            2, 'Below Average'
        ),
        (
            3, 'Average'
        ),
        (
            4, 'Good'
        ),
        (
            5, 'Excellent'
        )
    )
    rating = models.CharField(max_length=1, choices=RATING_CHOICES,
                              default=3)
    client = models.ForeignKey(User, on_delete=models.CASCADE)