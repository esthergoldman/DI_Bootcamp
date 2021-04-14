from django.contrib import admin
from .models import Gif #import the Gif model
from .models import Category 
# Register your models here.
admin.site.register(Gif),
admin.site.register(Category),
