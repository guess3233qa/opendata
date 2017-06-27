from django.shortcuts import render , render_to_response
from django.http import HttpRequest , HttpResponse
from .models import menu
from django.template import loader

# Create your views here.

def hello(request):
    print(isinstance(request, HttpRequest))
    print(request.path)
    print(request.method)
    print(request.GET.get('key'))
    foods = menu.foods
    return render_to_response('menu.html',locals())
    if request.GET.get('key') != None :
        return request.GET.get('key')

