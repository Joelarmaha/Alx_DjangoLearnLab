from bookshelf.models import Book

# Retrieve the book with the title "Nineteen Eighty-Four"
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance from the database
book.delete()

# Confirm the deletion by retrieving all books and printing them
books = Book.objects.all()
print(books)
