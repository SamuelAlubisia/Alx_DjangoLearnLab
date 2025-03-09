from django.shortcuts import render
from rest_framework import generics, viewsets # type: ignore
from .serializers import BookSerializer   # type: ignore
from .models import Book
# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
