from django.db import models
from django.utils import timezone

class Obituary(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    submission_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

