from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.FloatField(null=False)

