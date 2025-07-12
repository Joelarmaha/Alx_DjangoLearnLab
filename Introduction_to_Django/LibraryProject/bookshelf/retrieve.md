from bookshelf.models import Book

# Retrieve the book with title "1984"
book = Book.objects.get(title="1984")

# Display all attributes of the retrieved book
print("Title:", book.title)
print("Author:", book.author)
print("Publication Year:", book.publication_year)
