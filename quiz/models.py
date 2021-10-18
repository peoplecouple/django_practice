from django.db import models
from django.db.models.fields import IntegerField, TextField
from django.db.models.fields.related import ManyToManyField
from acc.models import User

# Create your models here.

class Quiz(models.Model):
    question = TextField()
    answer = TextField()
    solver = ManyToManyField(User, blank=True)
    point = IntegerField()