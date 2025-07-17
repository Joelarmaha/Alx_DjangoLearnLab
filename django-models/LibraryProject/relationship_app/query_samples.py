import os
import django

# Setup Django if running as a standalone script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")  # Replace with your project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# -------- QUERY EXAMPLES -------- #

# 1. Query all books by a specific author
author_name = "John Doe"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with the name '{author_name}'.")

# 2. List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library.name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with the name '{library_name}'.")

# 3. Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian found for the library '{library_name}'.")
