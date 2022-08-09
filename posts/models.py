from statistics import mode
from django.db import models
from helpers.models import BaseModel
from author.models import Author

CREATED = 'created'
MODERATION = 'moderation'
PUBLISHED = 'published'
POST_STATUS = (
    (CREATED, 'created'),
    (MODERATION, 'moderation'),
    (PUBLISHED, 'published')
)

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='category/')
    icon = models.ImageField(upload_to='category/')

    post_count = models.IntegerField(default=0)
    follower_count = models.IntegerField(default=0)


class Post(BaseModel):
    title = models.CharField(max_length=128, verbose_name='Post Nomi: ')
    slug = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    description = models.CharField(max_length=128)
    image = models.ImageField(upload_to='posts/')

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    
    published_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=15, choices=POST_STATUS)
    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    
    is_popular = models.BooleanField(default=False)

