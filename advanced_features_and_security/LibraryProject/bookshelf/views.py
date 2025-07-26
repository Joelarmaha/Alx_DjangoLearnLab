from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from .models import Article
from .forms import ArticleForm

@permission_required('article_app.can_view', raise_exception=True)
def book_list(request):
    articles = Article.objects.all()
    return render(request, 'article_app/article_list.html', {'articles': articles})

@permission_required('article_app.can_create', raise_exception=True)
def books(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'article_app/article_form.html', {'form': form})

@permission_required('article_app.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'article_app/article_form.html', {'form': form})

@permission_required('article_app.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

# bookshelf/views.py

from django.shortcuts import render
from .models import Book
from .forms import ExampleForm

def search_books(request):
    form = BookSearchForm(request.GET or None)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = Book.objects.filter(title__icontains=query)  # ✅ Safe ORM usage

    return render(request, 'bookshelf/book_list.html', {'form': form, 'results': results})

from django.http import HttpResponse

def secure_view(request):
    response = HttpResponse("Secure Content")
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self'"
    return response


# Create your views here.

