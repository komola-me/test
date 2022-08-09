from django.db import models
from helpers.models import BaseModel
from posts.models import Post
from author.models import Author

# Create your models here.
class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comment')
    slug = models.CharField(max_length=128, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

