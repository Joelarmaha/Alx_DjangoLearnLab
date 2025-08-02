from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

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
