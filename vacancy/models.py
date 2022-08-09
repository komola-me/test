from django.db import models
from author.models import Author
from helpers.models import BaseModel
# Create your models here.

class Tag(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)


class Vacancy(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='vacancy')
    slug = models.CharField(max_length=128, unique=True)
    job_position = models.CharField(max_length=128)
    content = models.TextField()
    published_date = models.DateTimeField(null=True)
    tag = models.ManyToManyField(Tag, related_name='vacancy')

    location = models.CharField(max_length=128)
    salary = models.PositiveBigIntegerField(default=0)

    is_premium = models.BooleanField(default=False)
