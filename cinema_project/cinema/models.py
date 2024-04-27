from django.db import models



# Create your models here.
from django.contrib.auth.models import User

class cinema(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ImageField(upload_to='note_images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100)
    year_of_release=models.IntegerField()
    duration=models.TextField()
    cast = models.CharField(max_length=100)
    crew = models.CharField(max_length=100)
    rating = models.IntegerField()
 


    def _str_(self):
        return self.title