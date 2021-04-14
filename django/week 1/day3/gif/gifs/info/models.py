from django.db import models
import datetime

# Create your models here.
class Gif(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField(max_length=200)
    uploader_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Category {self.name}'
 
class Category(models.Model):
    name = models.CharField(max_length=50)
    gifs = models.ManyToManyField(Gif,related_name='categories', blank=True)

    def __str__(self):
        return f'Category {self.name}'
# related_name is to retrieve the categories from a post

