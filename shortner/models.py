from django.db import models

# Create your models here.
class Shortner(models.Model):
    original_url = models.URLField(max_length=1000)
    short_url = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.original_url
