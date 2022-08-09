from django.db import models

from helpers.models import BaseModel

USER = 'user'
COMPANY = 'company'
AUTHOR = 'author'
LENTA = 'lenta'

USER_TYPE = (
    (USER, 'user'),
    (COMPANY, 'company'),
    (AUTHOR, 'author'),
    (LENTA, 'lenta')
)

# Create your models here.
class Author(BaseModel):
    first_name = models.CharField(max_length=128, verbose_name='Ism: ')
    last_name = models.CharField(max_length=128, verbose_name='Familya: ')
    slug = models.CharField(max_length=128, unique=True)
    username = models.CharField(max_length=128, verbose_name='Username: ')
    avatar = models.ImageField(upload_to='author/')
    user_type = models.CharField(max_length=15, choices=USER_TYPE)

    bio = models.TextField()

    content = models.TextField()
    post_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    follower_count = models.IntegerField(default=0)

    is_top = models.BooleanField(default=False)
