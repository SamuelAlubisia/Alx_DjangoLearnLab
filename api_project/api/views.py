from django.shortcuts import render
from rest_framework import generics, viewsets # type: ignore
from .serializers import BookSerializer   # type: ignore
from .models import Book
# Import necessary modules for authentication and permissions
from rest_framework.permissions import IsAuthenticated,IsAdminUser # type: ignore
# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# BookViewSet: Handles CRUD operations for Book model
# Authentication: Uses token-based authentication
# Permissions: Restricts access to authenticated users only
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
