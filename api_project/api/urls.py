from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Optional: keep the simple list view
    path('books/', BookList.as_view(), name='book-list'),

    # Add the router's URLs (CRUD endpoints)
    path('', include(router.urls)),
]


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token endpoint
    path('', include(router.urls)),
]
