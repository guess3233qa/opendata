#coding=utf8
from django.http import HttpResponse
from django.shortcuts import render_to_response , render
from poll import views

def here(request):
    return HttpResponse('Mom, I am here')

def abc(request):
	return render(request,'abc.html')

def menu(request):
    print (request.GET.get('key'))
    return render(request, 'menu.html')

