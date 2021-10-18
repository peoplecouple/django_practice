from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from acc.models import User
# Create your models here.

class Topic(models.Model):
    subject = CharField(max_length=100)
    writer = CharField(max_length=100)
    writer_pic = ImageField()
    comment = TextField()
    voter = ManyToManyField(User, blank=True)
    c_time = DateTimeField(null=True)

    def __str__(self):
        return self.subject

class Choice(models.Model):
    subject = ForeignKey(Topic, on_delete=CASCADE)
    pic = ImageField(upload_to="vote")
    name = CharField(max_length=100)
    cuser= ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name