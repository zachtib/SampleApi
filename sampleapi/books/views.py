from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from rest_framework import viewsets

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def index(request):
    return HttpResponse("Hello, world")
