# Generated by Django 2.1.7 on 2019-03-20 09:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sandbox', '0009_exams_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(null=True)),
                ('from_user', models.OneToOneField(on_delete='CASCADE', related_name='+', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete='CASCADE', related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]