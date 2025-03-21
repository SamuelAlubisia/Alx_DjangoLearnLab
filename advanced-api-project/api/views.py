from django.shortcuts import render

# Create your views here.
from rest_framework import generics,permissions, serializers, filters # type: ignore
from .models import Book
from .serializers import BookSerializer # type: ignore
from datetime import datetime  # Import datetime module
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated # type: ignore
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
from django_filters import rest_framework  # type: ignore


# Get the current year dynamically
CURRENT_YEAR = datetime.now().year

# Custom Permission: Allow only authenticated users to modify books
class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Allow anyone to read (GET, HEAD, OPTIONS).
    - Allow only authenticated users to create, update, or delete.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # Allow GET, HEAD, OPTIONS
            return True
        return request.user and request.user.is_staff  # Only admins can modify

# Create your views here.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serialzier_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # No login required
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] 

# Filtering by title, author, and publication year
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching in title and author
    search_fields = ['title', 'author']

    # Ordering by title or publication year
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # No login required

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serialzier_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Login required

    def perform_create(self, serializer):
        """Ensure book title is unique and publication year is valid before saving."""
        title = serializer.validated_data.get('title')
        publication_year = serializer.validated_data.get('publication_year')

        if Book.objects.filter(title=title).exists():
            raise serializers.ValidationError({"title": "A book with this title already exists."})

        if publication_year > CURRENT_YEAR:  # Prevents future dates
            raise serializers.ValidationError({"publication_year": "Publication year cannot be in the future."})

        serializer.save()  # Save the book after validation

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Login required
  # Only admins can update books

    def perform_update(self, serializer):
        """Ensure publication year is valid before updating."""
        publication_year = serializer.validated_data.get('publication_year', None)

        if publication_year and publication_year > CURRENT_YEAR:
            raise serializers.ValidationError({"publication_year": f"Publication year cannot be in the future )."})

        serializer.save()  # Save the updated book

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Login required