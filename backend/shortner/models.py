from django.db import models

# Create your models here.


import string

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

def base62_encode(num):
    return "".join(chars[digit] for digit in base62_digits(num))

def base62_digits(num):
    if num < 62:
        yield num
    else:
        quotient, remainder = divmod(num, 62)
        yield from base62_digits(quotient)
        yield remainder

def get_short_url(pk):
    
    return base62_encode(pk)









class URL(models.Model):
    original_url = models.URLField(max_length=1000)
    short_url = models.CharField(max_length=100)

    def __str__(self):
        return self.original_url
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.short_url:
            self.short_url = get_short_url(self.pk)
            super().save(update_fields=['short_url'])
    