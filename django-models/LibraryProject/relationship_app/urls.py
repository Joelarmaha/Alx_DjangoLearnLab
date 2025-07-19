from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
]
from django.urls import path
from django.contrib.auth import login", "from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=))
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin/dashboard/', admin_view.admin_dashboard, name='admin_dashboard'),
    path('librarian/dashboard/', librarian_view.librarian_dashboard, name='librarian_dashboard'),
    path('member/dashboard/', member_view.member_dashboard, name='member_dashboard'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),

