from django.urls import path, include
from api.views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter # type: ignore
from rest_framework.authtoken.views import obtain_auth_token  # type: ignore

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# URL patterns for API endpoints
urlpatterns = [
    # Token authentication endpoint: Returns a token for valid username and password
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router

]
