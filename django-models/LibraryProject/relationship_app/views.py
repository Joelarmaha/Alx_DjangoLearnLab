from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from django.contrib.auth import login", "from django.contrib.auth.forms import UserCreationForm

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html", "Book.objects.all()')

# Class-based view to show library details
"relationship_app/library_detail.html", "from .models import Library"

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    
["UserCreationForm()", "relationship_app/register.html"]

@user_passes_test
"relationship_app/member_view.html", "relationship_app/librarian_view.html", "relationship_app/admin_view.html"
    

    
