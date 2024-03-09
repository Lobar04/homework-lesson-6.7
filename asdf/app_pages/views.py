from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

def first(request):
    return HttpResponse("<h1>Hello , this is first page</h1><br><a href='http://127.0.0.1:8000/page=2/'>if you want to go to the second page click on this link</a>")

def second(request):
    return HttpResponse("<h1>Hello , this is second page</h1><br><a href='http://127.0.0.1:8000/page=3/'>if you want to go to the third page click on this link</a>")


def third(request):
    return HttpResponse("<h1>Hello , this is third page</h1><br><a href='http://127.0.0.1:8000/page=4/'>if you want to go to the fourth page click on this link</a>")


def fourth(request):
    return HttpResponse("<h1>Hello , this is fourth page</h1><br><a href='http://127.0.0.1:8000/page=5/'>if you want to go to the fifth page click on this link</a>")


def fifth(request):
    return HttpResponse("<h1>Hello , this is fifth page</h1><br><a href='http://127.0.0.1:8000/page=1/'>if you want to go to the first page click on this link</a>")

def main(request):
    return HttpResponse("<h1>Hello</h1><br><a href='http://127.0.0.1:8000/page=1/'>if you want to go to the first page click on this link</a>")