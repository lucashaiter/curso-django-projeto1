from django.shortcuts import render
from django.http import HttpResponse

# HTTP Request
def home_view(request):
    # return HTTP Response
    return HttpResponse('HTTP RESPONSE - HOME')

def sobre_view(request):
    return HttpResponse('HTTP RESPONSE - SOBRE')

def contato_view(request):
    return HttpResponse('HTTP RESPONSE - CONTATO')
