from django.contrib import admin
from .models import Book

admin.site.register(Book)
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for easy navigation
    list_filter = ('publication_year', 'author')

    # Enable search functionality
    search_fields = ('title', 'author')
    from django.contrib import admin
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from .models import CustomUser
    from django.utils.translation import gettext_lazy as _

    class CustomUserAdmin(UserAdmin):
        model = CustomUser
        fieldsets = UserAdmin.fieldsets + (
            (_('Additional Info'), {'fields': ('date_of_birth', 'profile_photo')}),
        )
        add_fieldsets = UserAdmin.add_fieldsets + (
            (_('Additional Info'), {'fields': ('date_of_birth', 'profile_photo')}),
        )
        list_display = ['username', 'email', 'date_of_birth', 'is_staff']
        search_fields = ['username', 'email']

    admin.site.register(CustomUser, CustomUserAdmin)
