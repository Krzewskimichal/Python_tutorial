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


class Library(models.Model):
    stringmethods = models.ForeignKey(StringMethods, on_delete='CASCADE')
    listmethods = models.ForeignKey(ListMethods, on_delete='CASCADE')
    dictionarymethosd = models.ForeignKey(DictionaryMethods, on_delete='CASCADE')
    tuplemethods = models.ForeignKey(TupleMethods, on_delete='CASCADE')
    setmethods = models.ForeignKey(SetMethods, on_delete='CASCADE')
    keywords = models.ForeignKey(Keywords, on_delete='CASCADE')
    builtinfunction = models.ForeignKey(BuiltInFunction, on_delete='CASCADE')
