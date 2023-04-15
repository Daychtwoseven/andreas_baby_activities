from django.contrib.auth.models import User
from django.db import models
import uuid


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)


class Person(models.Model):
    name = models.CharField(max_length=100)
    role = models.ForeignKey(Role, models.RESTRICT)
    birthdate = models.DateField(auto_now=False)
    date_created = models.DateTimeField(auto_now_add=True)


class Activities(models.Model):
    TYPE_CHOICES = (
        ('short_activity', 'Short Activity'),
        ('long_activity', 'Long Activity')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    interval = models.CharField(max_length=100)
    description = models.TextField(null=True)


class ActivityLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activity = models.ForeignKey(Activities, models.RESTRICT)
    comment = models.TextField(null=True)
    start_time = models.DateTimeField(auto_now_add=False, null=True)
    end_time = models.DateTimeField(auto_now_add=False, null=True)
    persons = models.ManyToManyField(Person)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, models.RESTRICT)
