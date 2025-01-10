from django.db import models

# Create your models here.
class MovieReview(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    release_year = models.IntegerField()
    rating = models.FloatField()
    runtime = models.IntegerField()
    content = models.TextField()
    cast = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title