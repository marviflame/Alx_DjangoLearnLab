from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Welcome to the polls.")

# Create your views here.
