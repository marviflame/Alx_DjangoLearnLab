# from django.shortcuts import render

from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Hello, Welcome to the Polls.")


# Create your views here.
