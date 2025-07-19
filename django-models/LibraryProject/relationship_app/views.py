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
    
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm  # You should have a BookForm defined

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Adjust this to your actual listing page
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form, 'action': 'Add'})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form, 'action': 'Edit'})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {'book': book})


    
