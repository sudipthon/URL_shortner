from rest_framework import serializers

from .models import URL,Counter




import string
import itertools

counter = itertools.count()
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

def get_short_url():
    counter,created = Counter.objects.get_or_create(pk=1)
    if created:
        counter.count = +1
        counter.save()
    return base62_encode(next(counter.count))


class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(read_only=True)
    class Meta:
        model = URL
        fields = ('original_url', 'short_url')


    def create(self, validated_data):
        original_url = validated_data['original_url']
        short_url = get_short_url()
        return URL.objects.create(original_url=original_url, short_url=short_url)