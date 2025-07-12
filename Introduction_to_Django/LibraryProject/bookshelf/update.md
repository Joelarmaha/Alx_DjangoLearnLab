from bookshelf.models import Book

# Retrieve the book with the title "1984"
book = Book.objects.get(title="1984")

# Update the title to "Nineteen Eighty-Four"
book.title = "Nineteen Eighty-Four"

# Save the changes to the database
book.save()

# Confirm the update by printing the updated title
print("Updated Title:", book.title)

