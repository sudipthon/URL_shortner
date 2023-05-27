from django.shortcuts import render,HttpResponse,redirect
from . models import Shortner
import random, string
# Create your views here.

def index(request):
    b='NmUuVPhQZWxCXYIfGy5bBpk0gD7TJqMHLOiwenF43S1l2sodzrKvaR6A9cEjt8'

    uid=''
    context={}
    if request.method == "POST":
        page='shortened'
        url = request.POST.get('link')
        for i in range(6):
            uid+=random.choice(b)
        shortner=Shortner(original_url=url,short_url=uid)
        shortner.save()
        context={'shortened_url':uid,'page':page}
        return render(request,"index.html",context)

    return render(request,"index.html",context)

def redirector(request,pk):
    # pk=pk[22:]
    url_details=Shortner.objects.get(short_url=pk)
    return redirect(url_details.original_url)
    # context={'url':url_details.original_url}
    # return render(request,'index.html',context)