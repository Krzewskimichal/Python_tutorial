# Generated by Django 2.1.7 on 2019-03-20 10:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandbox', '0010_messenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messenger',
            name='from_user',
            field=models.ForeignKey(on_delete='CASCADE', related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]