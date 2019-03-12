from django.db import models
from django.contrib.auth.models import User


class BuiltInFunction(models.Model):
    name = models.CharField(max_length=128)
    definition = models.TextField()


class UserFeature(models.Model):
    level = models.IntegerField(default=1)
    user = models.OneToOneField(User, on_delete='CASCADE')


class Exams(models.Model):
    task = models.CharField(max_length=512)
    answer = models.CharField(max_length=512)
