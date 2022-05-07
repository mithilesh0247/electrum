from django.db import models

# Create your models here.
class  Movie(models.Model):
    title=models.CharField(max_length=100)
    releasedYear =models.DateField(blank=True)
    rating=models.CharField(max_length=10)
    id=models.IntegerField(primary_key=True)
    genres=models.CharField(max_length=100)
    def __str__(self):
        return self.movietitle
