from django.db import models
from django.utils import timezone
import datetime

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
    date_published = models.DateTimeField()
    tags = models.CharField(max_length=500)

    def __str__(self):
        return "{} - {}".format(str(self.author), self.title)
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)