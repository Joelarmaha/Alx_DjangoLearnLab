from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """Test suite for Book API endpoints."""

    def setUp(self):
        """Initialize test data."""
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass123')

        # Create an author
        self.author = Author.objects.create(name="George Orwell")

        # Create a book
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        # API client
        self.client = APIClient()

        # Endpoints
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])

    # -----------------------------
    # Read (List & Detail)
    # -----------------------------
    def test_list_books(self):
        """Test retrieving all books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data[0])
        self.assertEqual(response.data[0]['title'], "1984")

    def test_retrieve_single_book(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")

    # -----------------------------
    # Create (Authenticated only)
    # -----------------------------
    def test_create_book_authenticated(self):
        """Test creating a new book when authenticated."""
        self.client.login(username='testuser', password='testpass123')
        data = {
            "title": "Animal Farm",
            "publication_year": 1945,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Test creating a book without authentication."""
        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -----------------------------
    # Update (Authenticated only)
    # -----------------------------
    def test_update_book_authenticated(self):
        """Test updating a book when authenticated."""
        self.client.login(username='testuser', password='testpass123')
        data = {
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Nineteen Eighty-Four")

    def test_update_book_unauthenticated(self):
        """Test updating a book without authentication."""
        data = {
            "title": "Changed Title",
            "publication_year": 1949,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -----------------------------
    # Delete (Authenticated only)
    # -----------------------------
    def test_delete_book_authenticated(self):
        """Test deleting a book when authenticated."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_delete_book_unauthenticated(self):
        """Test deleting a book without authentication."""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -----------------------------
    # Filtering, Searching, Ordering
    # -----------------------------
    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(f"{self.list_url}?title=1984")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "1984")

    def test_search_books_by_author(self):
        """Test searching books by author's name."""
        response = self.client.get(f"{self.list_url}?search=Orwell")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication year."""
        # Add another book for ordering test
        Book.objects.create(
            title="Animal Farm",
            publication_year=1945,
            author=self.author
        )
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))

