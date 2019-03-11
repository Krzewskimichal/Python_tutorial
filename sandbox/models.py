from django.db import models


class BuiltInFunction(models.Model):
    name = models.CharField(max_length=128)
    definition = models.CharField(max_length=128)
