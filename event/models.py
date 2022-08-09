from django.db import models

from helpers.models import BaseModel
from author.models import Author


# Create your models here.
class Tag(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)


class Event(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='event')
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    price = models.IntegerField(default=0)
    
    tag = models.ManyToManyField(Tag, related_name='event')

    is_premium = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)
