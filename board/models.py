from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from acc.models import User
from django.utils import timezone
# Create your models here.

class Board(models.Model):
    subject = CharField(max_length=50)
    writer = CharField(max_length=30)
    content = TextField()
    likey = IntegerField(default=0)
    up = ManyToManyField(User)  # 좋아요한 게시글 지운다고 유저 삭제 안됨 그러니 n:n
    c_time = models.DateTimeField()


    def __str__(self):
        return self.subject

    def summary(self):
        return self.content[:20] + "..."

class Reply(models.Model):
    subject = ForeignKey(Board, on_delete=CASCADE)
    replyer = CharField(max_length=100)
    comment = TextField()
    pic = ImageField()