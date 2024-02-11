from django.shortcuts import render,HttpResponse
from . models import URL
import string

import itertools
from django.utils.text import slugify
from django.contrib.sites.shortcuts import get_current_site

from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import URLSerializer
from rest_framework.decorators import api_view

# Create your views here.

# counter = itertools.count()
# chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

# def base62_encode(num):
#     return "".join(chars[digit] for digit in base62_digits(num))

# def base62_digits(num):
#     if num < 62:
#         yield num
#     else:
#         quotient, remainder = divmod(num, 62)
#         yield from base62_digits(quotient)
#         yield remainder

# def get_short_url():
#     return base62_encode(next(counter))


# @api_view(['GET','POST'])
@api_view(['POST'])
def home(request):
    print(request.data)
    if request.method == "POST":
        serializer=URLSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data,status=201)
            except Exception as e:
                print(e)  # Print any database exceptions
        else:
            return Response(serializer.errors)
    # url=URL.objects.all()
    # serializer=URLSerializer(url,many=True)
    # return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def redirect(request,short_url):
    url_details=URL.objects.get(short_url=short_url)
    
    serializer=URLSerializer(url_details)
    # return redirect(url_details.original_url)
    return Response(serializer.data)
  