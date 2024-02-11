from django.db import models

# Create your models here.

class Counter(models.Model):
    count = models.IntegerField(default=0)


class URL(models.Model):
    original_url = models.URLField(max_length=1000)
    short_url = models.CharField(max_length=100)

    def __str__(self):
        return self.original_url
