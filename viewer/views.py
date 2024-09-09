from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello(request):
    return HttpResponse("Hello, world!")


def hello2(request, s):
    return HttpResponse(f"Hello, {s} world!")


def hello3(request):
    s = request.GET.get('s', '')
    return HttpResponse(f"Hello, {s} world!")


def hello4(request):
    s = request.GET.get('s', '')
    context = {'adjectives': [s, 'beautiful', 'nice', 'wonderful']}
    return render(request, template_name='hello.html', context=context)


def add(request, num1, num2):
    return HttpResponse(f"{num1} + {num2} = {num1 + num2}")


def add2(request):
    num1 = int(request.GET.get('num1', 0))
    num2 = int(request.GET.get('num2', 0))
    return HttpResponse(f"{num1} + {num2} = {num1 + num2}")
