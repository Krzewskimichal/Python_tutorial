# Generated by Django 2.1.7 on 2019-03-19 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sandbox', '0007_library'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='builtinfunction',
        ),
        migrations.RemoveField(
            model_name='library',
            name='dictionarymethosd',
        ),
        migrations.RemoveField(
            model_name='library',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='library',
            name='listmethods',
        ),
        migrations.RemoveField(
            model_name='library',
            name='setmethods',
        ),
        migrations.RemoveField(
            model_name='library',
            name='stringmethods',
        ),
        migrations.RemoveField(
            model_name='library',
            name='tuplemethods',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
    ]