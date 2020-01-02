from django.db import models
from django.utils import timezone

import datetime

from ckeditor.fields import RichTextField


def user_directory_path(instance, filename):   
    return 'user_{0}/{1}'.format(instance.author.id, filename) 

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    birth_date = models.DateField()
    place_of_birth = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    slug = models.SlugField()
    date_published = models.DateTimeField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to=user_directory_path, null=True)
    tags = models.CharField(max_length=500)
    body = models.TextField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.date_published:
            self.date_published = timezone.now()
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    
    def __str__(self):
        return "{} - {}".format(str(self.author), self.title)
    
    def was_published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'date_published'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
