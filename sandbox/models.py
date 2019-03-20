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
    lesson = models.SmallIntegerField(default=1)


class StringMethods(models.Model):
    name = models.CharField(max_length=128)
    definition = models.TextField()


class ListMethods(models.Model):
    name = models.CharField(max_length=128)
    definition = models.TextField()


class DictionaryMethods(models.Model):
    name = models.CharField(max_length=128)
    definition = models.TextField()


class TupleMethods(models.Model):
    name = models.CharField(max_length=128)
    definition = models.TextField()


class SetMethods(models.Model):
    name = models.CharField(max_length=128)
    definition = models.TextField()


class Keywords(models.Model):
    name = models.CharField(max_length=128)
    definition = models.TextField()


class Messenger(models.Model):
    from_user = models.ForeignKey(User, related_name='+', on_delete="CASCADE")
    to_user = models.ForeignKey(User, related_name='+', on_delete="CASCADE")
    time = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True)
    message_title = models.CharField(max_length=128)
