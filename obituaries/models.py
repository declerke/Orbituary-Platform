from django.core.exceptions import ValidationError
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

    def clean(self):
        super().clean()
        if self.date_of_birth and self.date_of_death and self.date_of_death < self.date_of_birth:
            raise ValidationError({
                'date_of_death': 'Date of passing cannot be before date of birth.',
            })

    def __str__(self):
        return self.name
