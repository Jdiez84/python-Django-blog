from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(cats):
    return HttpResponse ("<em> My Second App<em>")

def help(request):
    helpdict= { 'help_insert':'help page'}
    return render(request,'appTwo/help.html',context=helpdict)
