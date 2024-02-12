from . models import URL
from rest_framework.response import Response
from .serializers import URLSerializer
from rest_framework.decorators import api_view




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
 

@api_view(['GET'])
def redirect(request,short_url):
    url_details=URL.objects.get(short_url=short_url)
    
    serializer=URLSerializer(url_details)
    return Response(serializer.data)
  