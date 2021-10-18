from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField, IntegerField, TextField
# Create your models here.

class User(AbstractUser):
    userpic = models.ImageField(upload_to="usr/%y", blank=True) #블랭크가 마이그래이트 해도 오류없이 유저픽 나중에 넣게 해줌
    nickname = CharField(max_length=30, blank = True)
    comment = TextField(blank = True)
    point = IntegerField(default=0)

    pass #엡스트랙유저의 속성만 상속받아옴 다른일은 안일어남
