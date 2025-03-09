from django.urls import path, include
from api.views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter # type: ignore

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]
