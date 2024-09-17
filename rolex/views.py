from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def rolex_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('This is video')
