from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for these fields
    list_filter = ('author', 'publication_year')
    
    # Enable search capabilities for these fields
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin class
admin.site.register(Book, BookAdmin)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Display these fields in the list view
    list_display = ['email', 'username', 'date_of_birth', 'is_staff']
    
    # Add custom fields to the edit screens
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    # Add custom fields to the 'Add User' screen
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)