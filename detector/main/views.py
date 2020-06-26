from django.shortcuts import render, redirect
import os
from django.conf import settings
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'main/main.html')

def upload(request):
    # print(request)
    if request.method == 'POST':
        if 'fileObj' in request.FILES:
            file = request.FILES['fileObj']
            filename = file._name

            fp = open('%s/%s' % (os.path.join(settings.BASE_DIR, 'media'), filename) , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            
    return HttpResponse(filename)
    # return redirect('main:index')

def resultView(request):
    if request.method == 'GET':
        # print(request.GET)
        # print(request.GET.get('name'))
        pass
    # fpath = os.path.join(settings.BASE_DIR, 'media')
    # preimage = mpimg.imread(os.path.join(fpath,request.GET.get('name')))
    # imagepath = os.path.join(fpath,request.GET.get('name'))
    imagepath = "/media/" + request.GET.get('name')
    return HttpResponse(imagepath)