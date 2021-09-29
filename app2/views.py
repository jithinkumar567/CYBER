from djangoproject2.settings import TEMPLATES
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test1fun(request):
    return HttpResponse('hello cyber square')
    
def samplefun(request):
    return render(request,'test.html')
