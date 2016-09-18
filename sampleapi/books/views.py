from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from .models import Author, Book


def index(request):
    return HttpResponse("Hello, world")


def books(request):
    data = serializers.serialize('json', Book.objects.all())
    return HttpResponse(data)

def authors(request):
    data = serializers.serialize('json', Author.objects.all())
    return HttpResponse(data)